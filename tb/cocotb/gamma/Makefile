

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

VHDL_SOURCES = $(WPWD)/../../../src/gamma.vhd
VHDL_SOURCES += $(WPWD)/../../../src/gamma_tables.vhd

TOPLEVEL := gamma
MODULE   := gamma_tb

include $(shell cocotb-config --makefiles)/Makefile.sim
