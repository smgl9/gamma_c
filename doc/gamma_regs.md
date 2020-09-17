&nbsp;&nbsp;

# Entity: gamma_regs
## Diagram
![Diagram](gamma_regs.svg "Diagram")
## Description
## Generics and ports
### Table 1.1 Generics
| Generic name   | Type                          | Description |
| -------------- | ----------------------------- | ----------- |
| AXI_ADDR_WIDTH | integer                       |             |
| BASEADDR       | std_logic_vector(31 downto 0) |             |
### Table 1.2 Ports
| Port name      | Direction | Type                                          | Description |
| -------------- | --------- | --------------------------------------------- | ----------- |
| axi_aclk       | in        | std_logic                                     |             |
| axi_aresetn    | in        | std_logic                                     |             |
| s_axi_awaddr   | in        | std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0) |             |
| s_axi_awprot   | in        | std_logic_vector(2 downto 0)                  |             |
| s_axi_awvalid  | in        | std_logic                                     |             |
| s_axi_awready  | out       | std_logic                                     |             |
| s_axi_wdata    | in        | std_logic_vector(31 downto 0)                 |             |
| s_axi_wstrb    | in        | std_logic_vector(3 downto 0)                  |             |
| s_axi_wvalid   | in        | std_logic                                     |             |
| s_axi_wready   | out       | std_logic                                     |             |
| s_axi_araddr   | in        | std_logic_vector(AXI_ADDR_WIDTH - 1 downto 0) |             |
| s_axi_arprot   | in        | std_logic_vector(2 downto 0)                  |             |
| s_axi_arvalid  | in        | std_logic                                     |             |
| s_axi_arready  | out       | std_logic                                     |             |
| s_axi_rdata    | out       | std_logic_vector(31 downto 0)                 |             |
| s_axi_rresp    | out       | std_logic_vector(1 downto 0)                  |             |
| s_axi_rvalid   | out       | std_logic                                     |             |
| s_axi_rready   | in        | std_logic                                     |             |
| s_axi_bresp    | out       | std_logic_vector(1 downto 0)                  |             |
| s_axi_bvalid   | out       | std_logic                                     |             |
| s_axi_bready   | in        | std_logic                                     |             |
| version_strobe | out       | std_logic                                     |             |
| version_value  | in        | std_logic_vector(31 downto 0)                 |             |
| gamma_strobe   | out       | std_logic                                     |             |
| gamma_value    | out       | std_logic_vector(15 downto 0)                 |             |
