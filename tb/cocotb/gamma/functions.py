from fxpmath import Fxp
import numpy as np
import matplotlib.pyplot as plt

def gamma_f(gamma,v_in):
    v_out=v_in**gamma
    return v_out

def gamma_fp(gamma):
    gamma_fp_value = Fxp(gamma, signed=False, n_word=8, n_frac=0 ) # dtype='U8.0'
    return gamma_fp_value

def data_gen():
    c_gamma=0.45
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
    out_data_fp = np.arange(0, 2**12, 1)
    for i in range(0,2**12):
        out_data_fp[i] = gamma_fp(out_data_f[i])
    ##### plot
    # plt.plot(out_data_fnorm)
    # plt.plot(out_data_disp_fnorm)
    # plt.show()
    # plt.plot(out_data_disp)
    # plt.show()
    # plt.plot(out_data)
    # plt.show()
    # plt.plot(out_data_f)
    # plt.plot(out_data_disp_f)
    # plt.plot(out_data_fp)
    # plt.show()
    # plt.plot(abs(out_data_f-out_data_fp))
    # plt.show()
    # print(in_data.size)
    # print(in_data.size)
    # print(out_data.size)
    # print(out_data_fp)
    
    return out_data_fp
