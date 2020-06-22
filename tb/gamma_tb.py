# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from functions import gamma_f, gamma
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
    c_gamma=0.45
    Period = 10
    clk=dut.clk
    cocotb.fork(gen_clk(clk, Period))
    yield Timer(20*Period)
    reset = 0
    # plot data
    # integer data input
    in_data = np.arange(0, 2**12, 1)
    # Adjust data out
    A_scan = 2**8/(2**12)**c_gamma 
    A_disp = 2**8/(2**12)**(1/c_gamma) 
    # normalized data input (0-1)
    in_data_f = np.linspace(0, 1, num=2**12)
    vect_gamma_f = np.vectorize(gamma_f)
    out_data = vect_gamma_f(c_gamma,in_data)
    out_data_fp = out_data*A_scan
    out_data_f = vect_gamma_f(c_gamma,in_data_f)
    out_data_disp = vect_gamma_f(1/c_gamma,in_data)
    out_data_disp_fp =out_data_disp*A_disp
    out_data_disp_f = vect_gamma_f(1/c_gamma,in_data_f)
    # plot
    plt.plot(out_data_f)
    plt.plot(out_data_disp_f)
    plt.show()
    plt.plot(out_data_disp)
    plt.show()
    plt.plot(out_data)
    plt.show()
    plt.plot(out_data_fp)
    plt.plot(out_data_disp_fp)
    plt.show()
    print(in_data)
    print(in_data)
    print(out_data)
    # Random test
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

