library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity gamma_stream is
    generic (
        tdata_width_g : positive := 32;
        tuser_width_g : positive := 1;
        data_in_g     : positive := 12;
        data_out_g    : positive := 8
    );
    port (
        axis_aclk     : in std_logic;
        axis_arst     : in std_logic;
        gamma_in      : in std_logic_vector(15 downto 0);
        s_axis_tready : out std_logic;
        s_axis_tvalid : in std_logic;
        s_axis_tdata  : in std_logic_vector(tdata_width_g - 1 downto 0);
        s_axis_tlast  : in std_logic;
        s_axis_tuser  : in std_logic_vector(tuser_width_g - 1 downto 0);
        m_axis_tready : in std_logic;
        m_axis_tvalid : out std_logic;
        m_axis_tdata  : out std_logic_vector(tdata_width_g - 1 downto 0);
        m_axis_tlast  : out std_logic;
        m_axis_tuser  : out std_logic_vector(tuser_width_g - 1 downto 0)
    );
end entity;

architecture rtl of gamma_stream is

    signal zero_padding              : std_logic_vector(data_in_g - data_out_g - 1 downto 0) := (others => '0');
    signal r_s_axis_tlast            : std_logic;
    signal r_m_axis_tready           : std_logic;
    signal r_s_axis_tuser            : std_logic_vector(tuser_width_g - 1 downto 0);
    signal r_tdata, g_tdata, b_tdata : std_logic_vector(data_out_g - 1 downto 0);

begin

    m_axis_tdata <= x"00" & b_tdata & g_tdata & r_tdata;

    gamma_inst_r : entity work.gamma
        generic map(
            data_in_g  => data_in_g,
            data_out_g => data_out_g
        )
        port map(
            clk      => axis_aclk,
            reset    => axis_arst,
            dv_in    => s_axis_tvalid,
            gamma_in => gamma_in,
            data_in  => s_axis_tdata(7 downto 0) & zero_padding,
            dv_out   => m_axis_tvalid,
            data_out => r_tdata
        );
    gamma_inst_g : entity work.gamma
        generic map(
            data_in_g  => data_in_g,
            data_out_g => data_out_g
        )
        port map(
            clk      => axis_aclk,
            reset    => axis_arst,
            dv_in    => s_axis_tvalid,
            gamma_in => gamma_in,
            data_in  => s_axis_tdata(15 downto 8) & zero_padding,
            dv_out   => open,
            data_out => g_tdata
        );
    gamma_inst_b : entity work.gamma
        generic map(
            data_in_g  => data_in_g,
            data_out_g => data_out_g
        )
        port map(
            clk      => axis_aclk,
            reset    => axis_arst,
            dv_in    => s_axis_tvalid,
            gamma_in => gamma_in,
            data_in  => s_axis_tdata(23 downto 16) & zero_padding,
            dv_out   => open,
            data_out => b_tdata
        );

    process (axis_aclk)
    begin
        if rising_edge(axis_aclk) then
            if axis_arst = '1' then
                r_m_axis_tready <= '0';
                r_s_axis_tlast  <= '0';
                r_s_axis_tuser  <= "0";
            else
                r_m_axis_tready <= m_axis_tready;
                s_axis_tready   <= r_m_axis_tready;
                r_s_axis_tuser  <= s_axis_tuser;
                m_axis_tuser    <= r_s_axis_tuser;
                r_s_axis_tlast  <= s_axis_tlast;
                m_axis_tlast    <= r_s_axis_tlast;
            end if;
        end if;
    end process;
end architecture;