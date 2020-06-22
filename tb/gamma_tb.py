# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from functions import gamma_f

@cocotb.coroutine
def gen_clk(clk, period):
    while True:
        clk.value = 0
        yield Timer(period/2)
        clk.value = 1
        yield Timer(period/2)

@cocotb.test()
def gamma_testAlive(dut):
    c_gamma=0.45
    Period = 10
    clk=dut.clk
    cocotb.fork(gen_clk(clk, Period))
    yield Timer(20*Period)
    reset = 0
    for i in range(0,10):
        dv_in = random.randint(0, 1)
        gamma_in = random.randint(0, 1)
        data_in = random.randint(0, 100)
        dut.reset = reset
        dut.dv_in = dv_in
        dut.gamma_in = gamma_in
        dut.data_in = data_in
        yield Timer(20*Period)
        print(dut.data_out)
        print(data_in)
        print(gamma_f(c_gamma,data_in))
        print(abs(int(dut.data_out) - int(gamma_f(c_gamma,data_in))))
        if abs(int(dut.data_out) - int(gamma_f(c_gamma,data_in)))>1:
            raise TestFailure(
            "result is incorrect: %s != %s" % (str(int(dut.data_out)), int(gamma_f(c_gamma,data_in))))
        else:
            dut._log.info("Ok!")

