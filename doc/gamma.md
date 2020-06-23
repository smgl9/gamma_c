&nbsp;&nbsp;

# Entity: gamma
## Diagram
![Diagram](./gamma.svg "Diagram")
## Description
 Módulo para la codificación de imágenes capturadas con scanner
 Compresión de datos
## Generics and ports
### Table 1.1 Generics
| Generic name | Type    | Description     |
| ------------ | ------- | --------------- |
| g_data_in    | integer |  Data bits in   |
| g_data_out   | integer |  Data bits out  |
### Table 1.2 Ports
| Port name | Direction | Type                                    | Description                     |
| --------- | --------- | --------------------------------------- | ------------------------------- |
| clk       | in        | std_logic                               |  Reloj del sistema              |
| reset     | in        | std_logic                               |  Reset nivel alto               |
| dv_in     | in        | std_logic                               |  Data valid in                  |
| gamma_in  | in        | std_logic_vector(15 downto 0)           |  Configuración gamma. No usado  |
| data_in   | in        | std_logic_vector(g_data_in-1 downto 0)  |  Dato de entrada del ADC        |
| dv_out    | out       | std_logic                               |  Data valid de salida           |
| data_out  | out       | std_logic_vector(g_data_out-1 downto 0) |  Data out                       |
