# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
import random
from functions import gamma_f, gamma_fp
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
    in_data_norm = np.linspace(0, 1, num=2**12)
    vect_gamma_f = np.vectorize(gamma_f)
    out_data = vect_gamma_f(c_gamma,in_data)
    out_data_f = out_data*A_scan
    out_data_fnorm = vect_gamma_f(c_gamma,in_data_norm)
    out_data_disp = vect_gamma_f(1/c_gamma,in_data)
    out_data_disp_f =out_data_disp*A_disp
    out_data_disp_fnorm = vect_gamma_f(1/c_gamma,in_data_norm)
    
    # module out model
    vect_gamma_fp = np.vectorize(gamma_fp)
    # out_data_fp = vect_gamma_fp(out_data_f)
    out_data_fp = np.arange(0, 2**12, 1)
    for i in range(0,2**12):
        out_data_fp[i] = gamma_fp(out_data_f[i])
    # plot
    # plt.plot(out_data_fnorm)
    # plt.plot(out_data_disp_fnorm)
    # plt.show()
    # plt.plot(out_data_disp)
    # plt.show()
    # plt.plot(out_data)
    # plt.show()
    plt.plot(out_data_f)
    plt.plot(out_data_disp_f)
    plt.plot(out_data_fp)
    plt.show()
    plt.plot(abs(out_data_f-out_data_fp))
    plt.show()
    print(in_data.size)
    print(in_data.size)
    print(out_data.size)
    print(out_data_fp)

    # Random test
    for i in range(0,10):
        dv_in = random.randint(0, 1)
        gamma_in = random.randint(0, 1)
        data_in = random.randint(0, 2**12-1)
        dut.reset = reset
        dut.dv_in = dv_in
        dut.gamma_in = gamma_in
        dut.data_in = data_in
        yield Timer(20*Period)
        print(dut.data_out)
        print(data_in)
        print(gamma_f(c_gamma,data_in))
        print(abs(int(dut.data_out) - int(gamma_f(c_gamma,data_in))))
        if abs(int(dut.data_out) - out_data_fp[data_in])>1:
            raise TestFailure(
            "result is incorrect: %s != %s" % (str(int(dut.data_out)), int(gamma_f(c_gamma,data_in))))
        else:
            dut._log.info("Ok!")

