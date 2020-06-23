from cocotb_test.run import run
import pytest
import os

def test_adder_vhdl():
    run(vhdl_sources=["../src/gamma.vhd"],
        simulation_args=["--vcd=func.vcd"],
        toplevel="gamma",
        module="cocotb",
        toplevel_lang="vhdl"
    )
