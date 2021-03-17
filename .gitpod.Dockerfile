FROM ghdl/vunit:llvm

RUN apt-get update
RUN apt-get install python3-dev

RUN pip3 install numpy
RUN pip3 install fpbinary
RUN pip3 install cocotb

