# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61370217/sympy-bisection-method-typeerror-cannot-determine-truth-value-of-relational
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy import plot_implicit, latex, lambdify, Float
    _l_(531794)

except ImportError:
    pass
try:
    from sympy.abc import x
    _l_(531796)

except ImportError:
    pass
try:
    from sympy.parsing.latex import parse_latex
    _l_(531798)

except ImportError:
    pass

eq = _c_(531800, _n_(531799, "input", lambda: input), "Latex equation: ")    
_l_(531801)    
raw_equation = _c_(531808, _a_(531807, _c_(531806, _a_(531805, _c_(531804, _a_(531803, _n_(531802, "eq", lambda: eq), "replace"), "=0", ""), "replace"), "= 0", ""), "replace"), "e", "E")
_l_(531809)
equation = _c_(531812, _n_(531810, "parse_latex", lambda: parse_latex), "y = " + _n_(531811, "raw_equation", lambda: raw_equation))
_l_(531813)
f = _c_(531820, _n_(531814, "lambdify", lambda: lambdify), _n_(531815, "x", lambda: x), _c_(531819, _n_(531816, "parse_latex", lambda: parse_latex), _a_(531818, _n_(531817, "self", lambda: self), "__raw_equation")), 'numpy')
_l_(531821)

# Bisection
a = 0 # start interval
_l_(531822) # start interval
b = 1 # end interval
_l_(531823) # end interval

eps = _n_(531824, "a", lambda: a) - _n_(531825, "b", lambda: b)
_l_(531826)
r = None
_l_(531827)
nlimit = 8
_l_(531828)
for n in _c_(531831, _n_(531829, "range", lambda: range), _n_(531830, "nlimit", lambda: nlimit)):
    _l_(531875)

    c = (_n_(531832, "a", lambda: a) + _n_(531833, "b", lambda: b)) / 2
    _l_(531834)
    fd = {_n_(531835, "a", lambda: a): _c_(531838, _n_(531836, "f", lambda: f), _n_(531837, "a", lambda: a)), _n_(531839, "b", lambda: b): _c_(531842, _n_(531840, "f", lambda: f), _n_(531841, "b", lambda: b)), _n_(531843, "c", lambda: c): _c_(531846, _n_(531844, "f", lambda: f), _n_(531845, "c", lambda: c))}
    _l_(531847)
    solved = False
    _l_(531848)
    for v in [_n_(531849, "a", lambda: a), _n_(531850, "b", lambda: b), _n_(531851, "c", lambda: c)]:
        _l_(531862)

        if _n_(531852, "fd", lambda: fd)[_n_(531853, "v", lambda: v)] == 0:
            _l_(531861)

            r = _c_(531857, _a_(531854, "Iterations: {} - Result: {}", "format"), _n_(531855, "n", lambda: n) + 1, _n_(531856, "v", lambda: v))
            _l_(531858)
            solved = True
            _l_(531859)
            break
            _l_(531860)
    if _n_(531863, "solved", lambda: solved):
        _l_(531865)

        break
        _l_(531864)
    if _n_(531866, "fd", lambda: fd)[_n_(531867, "a", lambda: a)]*_n_(531868, "fd", lambda: fd)[_n_(531869, "c", lambda: c)] > 0:
        _l_(531874)

        b = _n_(531870, "c", lambda: c)
        _l_(531871)
    else:  # Opposite sign b and c
        a = _n_(531872, "c", lambda: c)
        _l_(531873)
...
_l_(531876)