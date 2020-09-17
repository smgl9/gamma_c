from cocotb_test.run import run
import pytest
import os

def gamma_test():
    run(vhdl_sources=["../src/gamma.vhd"],
        simulation_args=["--vcd=func.vcd"],
        toplevel="gamma",
        module="gamma_testAlive",
        toplevel_lang="vhdl"
    )
