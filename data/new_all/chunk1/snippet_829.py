# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69623498/typeerror-float-object-cannot-be-interpreted-as-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(417892)

except ImportError:
    pass

# Euclidean extended algorithm
def egcd(a, b):
    _l_(417910)

    if _n_(417893, "a", lambda: a) == 0:
        _l_(417909)

        aux = _n_(417894, "b", lambda: b), 0, 1
        _l_(417895)
        return aux
    else:
        d, x, y = _c_(417900, _n_(417896, "egcd", lambda: egcd), _n_(417897, "b", lambda: b) % _n_(417898, "a", lambda: a), _n_(417899, "a", lambda: a))
        _l_(417901)
        aux = _n_(417902, "d", lambda: d), _n_(417903, "y", lambda: y) - (_n_(417904, "b", lambda: b) // _n_(417905, "a", lambda: a)) * _n_(417906, "x", lambda: x), _n_(417907, "x", lambda: x)
        _l_(417908)
        return aux

"""
    Functions whcih calculate the CRT (
    return x in ' x = a mod n'.
"""

def chinese_remainder(a, n):
    _l_(417949)

    modulus = _c_(417916, _a_(417912, _n_(417911, "functools", lambda: functools), "reduce"), lambda a, b: _n_(417913, "a", lambda: a) * _n_(417914, "b", lambda: b), _n_(417915, "n", lambda: n))
    _l_(417917)
    multipliers = []
    _l_(417918)
    for N_i in _n_(417919, "n", lambda: n):
        _l_(417935)

        N = _n_(417920, "modulus", lambda: modulus) / _n_(417921, "N_i", lambda: N_i)
        _l_(417922)
        gcd, inverse, y = _c_(417926, _n_(417923, "egcd", lambda: egcd), _n_(417924, "N", lambda: N), _n_(417925, "N_i", lambda: N_i))
        _l_(417927)
        _c_(417933, _a_(417929, _n_(417928, "multipliers", lambda: multipliers), "append"), _n_(417930, "inverse", lambda: inverse) * _n_(417931, "N", lambda: N) % _n_(417932, "modulus", lambda: modulus))
        _l_(417934)

    result = 0
    _l_(417936)
    for multi, a_i in _c_(417940, _n_(417937, "zip", lambda: zip), _n_(417938, "multipliers", lambda: multipliers), _n_(417939, "a", lambda: a)):
        _l_(417946)

        result = (_n_(417941, "result", lambda: result) + _n_(417942, "multi", lambda: multi) * _n_(417943, "a_i", lambda: a_i)) % _n_(417944, "modulus", lambda: modulus)
        _l_(417945)
    aux = _n_(417947, "result", lambda: result)
    _l_(417948)
    return aux

FN = 1184749
_l_(417950)
FM = 8118474
_l_(417951)
FL = 5386565
_l_(417952)
HN = 8686891
_l_(417953)
HM = 6036033
_l_(417954)
HK = 6029230
_l_(417955)

n = [_n_(417956, "FN", lambda: FN), _n_(417957, "FM", lambda: FM), _n_(417958, "FL", lambda: FL)]
_l_(417959)
a = [_n_(417960, "HN", lambda: HN), _n_(417961, "HM", lambda: HM), _n_(417962, "HK", lambda: HK)]
_l_(417963)

d = _c_(417967, _n_(417964, "chinese_remainder", lambda: chinese_remainder), _n_(417965, "a", lambda: a), _n_(417966, "n", lambda: n))
_l_(417968)
number = _c_(417971, _n_(417969, "hex", lambda: hex), _n_(417970, "d", lambda: d))
_l_(417972)
_c_(417975, _n_(417973, "print", lambda: print), _n_(417974, "number", lambda: number))
_l_(417976)