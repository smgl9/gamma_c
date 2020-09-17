--! Módulo para la codificación de imágenes capturadas con scanner
--! Compresión de datos

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity gamma_top is
generic (
  G_DATA_IN : integer:=12; --! Data bits in
  G_DATA_OUT : integer:=8;  --! Data bits out
  AXI_ADDR_WIDTH : integer := 32
);
  port (
    clk      : in std_logic; --! Reloj del sistema
    reset    : in std_logic; --! Reset nivel alto
    dv_in    : in std_logic; --! Data valid in
    data_in  : in std_logic_vector(G_DATA_IN-1 downto 0); --! Dato de entrada del ADC
    dv_out   : out std_logic; --! Data valid de salida
    data_out : out std_logic_vector(G_DATA_OUT-1 downto 0); --! Data out
    -- Axi_lite
    axi_aclk      : in  std_logic;
    axi_aresetn   : in  std_logic;
    -- AXI Write Address Channel
    s_axi_awaddr  : in  std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0);
    s_axi_awprot  : in  std_logic_vector(2 downto 0);
    s_axi_awvalid : in  std_logic;
    s_axi_awready : out std_logic;
    -- AXI Write Data Channel
    s_axi_wdata   : in  std_logic_vector(31 downto 0);
    s_axi_wstrb   : in  std_logic_vector(3 downto 0);
    s_axi_wvalid  : in  std_logic;
    s_axi_wready  : out std_logic;
    -- AXI Read Address Channel
    s_axi_araddr  : in  std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0);
    s_axi_arprot  : in  std_logic_vector(2 downto 0);
    s_axi_arvalid : in  std_logic;
    s_axi_arready : out std_logic;
    -- AXI Read Data Channel
    s_axi_rdata   : out std_logic_vector(31 downto 0);
    s_axi_rresp   : out std_logic_vector(1 downto 0);
    s_axi_rvalid  : out std_logic;
    s_axi_rready  : in  std_logic;
    -- AXI Write Response Channel
    s_axi_bresp   : out std_logic_vector(1 downto 0);
    s_axi_bvalid  : out std_logic;
    s_axi_bready  : in  std_logic
  );
end entity gamma_top;

architecture rtl of gamma_top is


  
begin


end architecture rtl;