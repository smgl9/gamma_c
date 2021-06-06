# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from functions import data_gen
import numpy as np
import matplotlib.pyplot as plt

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
    
    out_data_fp = data_gen()

    # Random test
    for i in range(0,100):
        reset = random.randint(0, 1)
        dv_in = random.randint(0, 1)
        gamma_in = 1
        data_in = random.randint(0, 2**12-1)
        dut.reset = reset
        dut.dv_in = dv_in
        dut.gamma_in = gamma_in
        dut.data_in = data_in
        yield Timer(20*Period)

        dut._log.info(str(int(dut.data_out)))
        dut._log.info(str(out_data_fp[data_in]))
        if abs(int(dut.data_out) - out_data_fp[data_in])>1 and reset==0 and dv_in ==1:
            raise TestFailure(
            "result is incorrect: %s != %s  data_in = %s" % (str(int(dut.data_out)), str(out_data_fp[data_in]),str(data_in)))
        elif reset==1 and int(dut.data_out)!=0: 
            raise TestFailure(
            "result is incorrect. Reset = %s  dv = %s" %(str(reset),str(dut.dv_out)))
        elif dv_in == 1 and reset ==0 and int(dut.dv_out)==1:
            dut._log.info("Ok!")


@cocotb.test()
def gamma_ramp_test(dut):
    Period = 10
    clk=dut.clk
    cocotb.fork(gen_clk(clk, Period))
    yield Timer(20*Period)
    
    out_data_fp = data_gen()

    # Random test
    for i in range(0,2**12):
        reset = 0
        dv_in = 1
        gamma_in = 1
        data_in = i
        dut.reset = reset
        dut.dv_in = dv_in
        dut.gamma_in = gamma_in
        dut.data_in = data_in
        yield Timer(20*Period)

        if abs(int(dut.data_out) - out_data_fp[data_in])>1 and reset==0 and dv_in ==1:
            raise TestFailure(
            "result is incorrect: %s != %s  data_in = %s" % (str(int(dut.data_out)), str(out_data_fp[data_in]),str(data_in)))
        elif reset==1 and int(dut.data_out)!=0: 
            raise TestFailure(
            "result is incorrect. Reset = %s  dv = %s" %(str(reset),str(dut.dv_out)))
        elif dv_in == 1 and reset ==0 and int(dut.dv_out)==1:
            dut._log.info("Ok!")
