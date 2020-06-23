

TOPLEVEL_LANG ?= vhdl
SIM=ghdl
SIM_ARGS=--vcd=func.vcd

PWD=$(shell pwd)

ifeq ($(OS),Msys)
WPWD=$(shell sh -c 'pwd -W')
else
WPWD=$(shell pwd)
endif

PYTHONPATH := $(PWD):$(PYTHONPATH)

VHDL_SOURCES  = $(WPWD)/../../src/gamma_top.vhd
VHDL_SOURCES += $(WPWD)/../../src/gamma.vhd

TOPLEVEL := gamma_top
MODULE   := gamma_top_tb

include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim
