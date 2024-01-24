# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63789637/python-sympy-typeerror-cant-convert-expression-to-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy.functions import sin,cos
    _l_(390673)

except ImportError:
    pass
try:
    from sympy.abc import x
    _l_(390675)

except ImportError:
    pass
try:
    from sympy import series
    _l_(390677)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(390679)

except ImportError:
    pass
# Indsæt her funktionen f(x), variablen x, udviklingspunktet x0 og antal led n
_c_(390688, _n_(390680, "print", lambda: print), _c_(390687, _n_(390681, "series", lambda: series), _c_(390685, _a_(390683, _n_(390682, "math", lambda: math), "sqrt"), _n_(390684, "x", lambda: x)), _n_(390686, "x", lambda: x), x0=0, n=6))
_l_(390689)

N = _c_(390693, _n_(390690, "int", lambda: int), _c_(390692, _n_(390691, "input", lambda: input), "Antal summer(flere summer er mere præcist): "))
_l_(390694)
a = _c_(390698, _n_(390695, "int", lambda: int), _c_(390697, _n_(390696, "input", lambda: input), "Integrer fra: "))
_l_(390699)
b = _c_(390703, _n_(390700, "int", lambda: int), _c_(390702, _n_(390701, "input", lambda: input), "Integrer til: "))
_l_(390704)

# Vi anvender Midpoint metoden til integration og skriver funktionen ind, som skal integreres

def integrate(N, a, b):
    _l_(390735)

    def f(x):
        _l_(390713)

        aux = _c_(390711, _n_(390705, "series", lambda: series), _c_(390709, _a_(390707, _n_(390706, "math", lambda: math), "sqrt"), _n_(390708, "x", lambda: x)), _n_(390710, "x", lambda: x), x0=0, n=6)
        _l_(390712)
        return aux
    value=0
    _l_(390714)
    value=2
    _l_(390715)
    for n in _c_(390718, _n_(390716, "range", lambda: range), 1, _n_(390717, "N", lambda: N)+1):
        _l_(390727)

        value += _c_(390725, _n_(390719, "f", lambda: f), _n_(390720, "a", lambda: a)+((_n_(390721, "n", lambda: n)-(1/2))*((_n_(390722, "b", lambda: b)-_n_(390723, "a", lambda: a))/_n_(390724, "N", lambda: N))))
        _l_(390726)
    value2 = ((_n_(390728, "b", lambda: b)-_n_(390729, "a", lambda: a))/_n_(390730, "N", lambda: N))*_n_(390731, "value", lambda: value)
    _l_(390732)
    aux = _n_(390733, "value2", lambda: value2)
    _l_(390734)
    return aux

_c_(390737, _n_(390736, "print", lambda: print), "...................")
_l_(390738)
_c_(390740, _n_(390739, "print", lambda: print), "Her er dit svar: ")
_l_(390741)
_c_(390748, _n_(390742, "print", lambda: print), _c_(390747, _n_(390743, "integrate", lambda: integrate), _n_(390744, "N", lambda: N), _n_(390745, "a", lambda: a), _n_(390746, "b", lambda: b)))
_l_(390749)