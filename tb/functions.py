from fpbinary import FpBinary, OverflowEnum, RoundingEnum

def gamma_f(gamma,v_in):
    v_out=v_in**gamma
    return v_out

def gamma_fp(gamma):
    gamma_fp_value = FpBinary(int_bits=8, frac_bits=0, signed=False, value=gamma)
    return gamma_fp_value
