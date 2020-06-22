library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity gamma is
  port (
    clk      : in std_logic;
    reset    : in std_logic;
    dv_in    : in std_logic;
    gamma_in : in std_logic_vector(15 downto 0);
    data_in  : in std_logic_vector(11 downto 0);
    dv_out   : out std_logic;
    data_out : out std_logic_vector(7 downto 0)
  );
end entity gamma;

architecture rtl of gamma is

  signal sdata_out : std_logic_vector(7 downto 0) := (others => '0');

begin

  data_out <= sdata_out;

end architecture rtl;