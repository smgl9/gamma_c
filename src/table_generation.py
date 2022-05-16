import numpy as np
from fxpmath import Fxp
import matplotlib.pyplot as plt

def gamma_f(gamma,v_in):
    v_out=v_in**gamma
    return v_out

def gamma_fp(gamma):
    gamma_fp_value = Fxp(gamma, signed=False, n_word=8, n_frac=0 ) # dtype='U8.0')
    return gamma_fp_value


get_bin = lambda x, n: format(x, 'b').zfill(n)

c_gamma=0.45
A_scan = 2**8/(2**12)**c_gamma 
in_data = np.arange(0, 2**12, 1)
vect_gamma_f = np.vectorize(gamma_f)
out_data = vect_gamma_f(c_gamma,in_data)
out_data_f = out_data*A_scan
out_data_fp = np.arange(0, 2**12, 1)

f=open("table.txt","w")
for i in range(0,2**12):
    out_data_fp[i] = gamma_fp(out_data_f[i])
    if (i<2**12-1):
        f.write('"'+ get_bin(out_data_fp[i],8)+'",')
    else:
        f.write('"'+ get_bin(out_data_fp[i],8)+'"')

f.close()