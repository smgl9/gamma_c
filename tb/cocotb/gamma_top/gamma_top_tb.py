# from fpbinary import FpBinary, OverflowEnum, RoundingEnum
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
from cocotb.clock import Clock
import random
import numpy as np
from cocotb.drivers.amba import AXI4LiteMaster
from cocotb.drivers.amba import AXIProtocolError

CLK_PERIOD_NS = 10

def setup_dut(dut):
    cocotb.fork(Clock(dut.clk, CLK_PERIOD_NS, units='ns').start())

def setup_dut_axi(dut):
    cocotb.fork(Clock(dut.axi_aclk, CLK_PERIOD_NS, units='ns').start())

@cocotb.test()
def gamma_top_test_axi_alive(dut):

    setup_dut(dut)
    setup_dut_axi(dut)
    # Reset
    dut.axi_aresetn <=  0
    dut.reset <= 0
    yield Timer(CLK_PERIOD_NS*2, units='ns')
    axim = AXI4LiteMaster(dut, "s_axi", dut.axi_aclk)
    yield Timer(CLK_PERIOD_NS * 10, units='ns')
    # setup_dut(dut)
    dut.axi_aresetn <= 1
    yield Timer(100*CLK_PERIOD_NS, units='ns')
    ADDRESS = 0x00
    DATA = 0xbebecafe

    yield Timer(CLK_PERIOD_NS * 10, units='ns')

    # value = yield axim.read(ADDRESS)
    # yield Timer(CLK_PERIOD_NS * 10, units='ns')

    # if value != DATA:
    #     # Fail
    #     raise TestFailure("Register at address 0x%08X should have been: \
    #                        0x%08X but was 0x%08X" % (ADDRESS, DATA, int(value)))
    # ADDRESS = 0x04
    # DATA = 0x1

    # value = yield axim.write(ADDRESS,DATA)
    # yield Timer(CLK_PERIOD_NS * 10, units='ns')

    # yield Timer(CLK_PERIOD_NS * 10, units='ns')

    # value = yield axim.read(ADDRESS)
    # yield Timer(CLK_PERIOD_NS * 10, units='ns')

    # if value != DATA:
    #     # Fail
    #     raise TestFailure("Register at address 0x%08X should have been: \
    #                        0x%08X but was 0x%08X" % (ADDRESS, DATA, int(value)))

