# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random

@cocotb.coroutine
def gen_clk(clk, period):
    while True:
        clk.value = 0
        yield Timer(period/2)
        clk.value = 1
        yield Timer(period/2)

@cocotb.test()
def gamma_testAlive(dut):
    Period = 10
    clk=dut.clk
    cocotb.fork(gen_clk(clk, Period))
    yield Timer(20*Period)
    reset = random.randint(0, 1)
    gamma_in = random.randint(0, 1)
    data_in = random.randint(0, 1)
    dut.reset = reset
    dut.gamma_in = gamma_in
    dut.data_in = data_in
    yield Timer(20*Period)
    print(dut.data_out)
    if int(dut.data_out) == int(dut.data_out):
        raise TestFailure(
        "result is incorrect: %s != %s" % str(dut.data_out))
    else:
        dut._log.info("Ok!")
