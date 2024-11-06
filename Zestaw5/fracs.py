import math

def simplify(frac):
    if frac[1] == 0:
        raise ValueError('Cant divide by zero')
    nwd = math.gcd(frac[0], frac[1])
    return [frac[0] // nwd, frac[1] // nwd]

def add_frac(frac1, frac2):         # frac1 + frac2
    return simplify([frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]])

def sub_frac(frac1, frac2):         # frac1 - frac2
    return simplify([frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]])

def mul_frac(frac1, frac2):         # frac1 * frac2
    return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):         # frac1 / frac2
    return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):              # bool, czy dodatni
    return frac[0] * frac[1] > 0

def is_zero(frac):        # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    diff = sub_frac(frac1, frac2)
    if is_positive(diff):
        return 1
    elif is_zero(diff):
        return 0
    else:
        return -1

def frac2float(frac):               # konwersja do float
    return frac[0] / frac[1]
