&nbsp;&nbsp;

# Entity: gamma_top
## Diagram
![Diagram](gamma_top.svg "Diagram")
## Description
 Módulo para la codificación de imágenes capturadas con scanner
 Compresión de datos
## Generics and ports
### Table 1.1 Generics
| Generic name   | Type    | Description     |
| -------------- | ------- | --------------- |
| G_DATA_IN      | integer |  Data bits in   |
| G_DATA_OUT     | integer |  Data bits out  |
| AXI_ADDR_WIDTH | integer |                 |
### Table 1.2 Ports
| Port name     | Direction | Type                                          | Description               |
| ------------- | --------- | --------------------------------------------- | ------------------------- |
| clk           | in        | std_logic                                     |  Reloj del sistema        |
| reset         | in        | std_logic                                     |  Reset nivel alto         |
| dv_in         | in        | std_logic                                     |  Data valid in            |
| data_in       | in        | std_logic_vector(G_DATA_IN-1 downto 0)        |  Dato de entrada del ADC  |
| dv_out        | out       | std_logic                                     |  Data valid de salida     |
| data_out      | out       | std_logic_vector(G_DATA_OUT-1 downto 0)       |  Data out                 |
| axi_aclk      | in        | std_logic                                     |                           |
| axi_aresetn   | in        | std_logic                                     |                           |
| s_axi_awaddr  | in        | std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0) |                           |
| s_axi_awprot  | in        | std_logic_vector(2 downto 0)                  |                           |
| s_axi_awvalid | in        | std_logic                                     |                           |
| s_axi_awready | out       | std_logic                                     |                           |
| s_axi_wdata   | in        | std_logic_vector(31 downto 0)                 |                           |
| s_axi_wstrb   | in        | std_logic_vector(3 downto 0)                  |                           |
| s_axi_wvalid  | in        | std_logic                                     |                           |
| s_axi_wready  | out       | std_logic                                     |                           |
| s_axi_araddr  | in        | std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0) |                           |
| s_axi_arprot  | in        | std_logic_vector(2 downto 0)                  |                           |
| s_axi_arvalid | in        | std_logic                                     |                           |
| s_axi_arready | out       | std_logic                                     |                           |
| s_axi_rdata   | out       | std_logic_vector(31 downto 0)                 |                           |
| s_axi_rresp   | out       | std_logic_vector(1 downto 0)                  |                           |
| s_axi_rvalid  | out       | std_logic                                     |                           |
| s_axi_rready  | in        | std_logic                                     |                           |
| s_axi_bresp   | out       | std_logic_vector(1 downto 0)                  |                           |
| s_axi_bvalid  | out       | std_logic                                     |                           |
| s_axi_bready  | in        | std_logic                                     |                           |
