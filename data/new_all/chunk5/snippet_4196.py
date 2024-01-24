# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61851719/unsupported-operand-type-error-while-evaluating-gradient-using-sympy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(656975)

except ImportError:
    pass
try:
    import numpy as np
    _l_(656977)

except ImportError:
    pass
try:
    import math
    _l_(656979)

except ImportError:
    pass
try:
    import sympy as sym
    _l_(656981)

except ImportError:
    pass

x,y = _c_(656984, _a_(656983, _n_(656982, "sym", lambda: sym), "symbols"), 'x y')
_l_(656985)

 #objective function
def objective(p):
    _l_(657013)

    x = _n_(656986, "p", lambda: p)[0]
    _l_(656987)
    y = _n_(656988, "p", lambda: p)[1]
    _l_(656989)
    aux = -(_n_(656990, "y", lambda: y)+47)*_c_(657000, _a_(656992, _n_(656991, "sym", lambda: sym), "sin"), _c_(656999, _a_(656994, _n_(656993, "sym", lambda: sym), "sqrt"), _c_(656998, _n_(656995, "abs", lambda: abs), (_n_(656996, "x", lambda: x)/2)+_n_(656997, "y", lambda: y)+47))) - _n_(657001, "x", lambda: x)*_c_(657011, _a_(657003, _n_(657002, "sym", lambda: sym), "sin"), _c_(657010, _a_(657005, _n_(657004, "sym", lambda: sym), "sqrt"), _c_(657009, _n_(657006, "abs", lambda: abs), _n_(657007, "x", lambda: x)-(_n_(657008, "y", lambda: y)+47))))
    _l_(657012)
    return aux

 #gradient wrt x
def gradient_1(p):
    _l_(657033)

    g0 = _c_(657021, _a_(657015, _n_(657014, "sym", lambda: sym), "diff"), _c_(657019, _n_(657016, "objective", lambda: objective), [_n_(657017, "x", lambda: x),_n_(657018, "y", lambda: y)]),_n_(657020, "x", lambda: x))
    _l_(657022)
    aux = _c_(657031, _a_(657028, _c_(657027, _a_(657024, _n_(657023, "g0", lambda: g0), "subs"), _n_(657025, "x", lambda: x),_n_(657026, "p", lambda: p)[0]), "subs"), _n_(657029, "y", lambda: y),_n_(657030, "p", lambda: p)[1])
    _l_(657032)
    return aux

#gradient wrt y
def gradient_2(p):
    _l_(657053)

    g1 = _c_(657041, _a_(657035, _n_(657034, "sym", lambda: sym), "diff"), _c_(657039, _n_(657036, "objective", lambda: objective), [_n_(657037, "x", lambda: x),_n_(657038, "y", lambda: y)]),_n_(657040, "y", lambda: y))
    _l_(657042)
    aux = _c_(657051, _a_(657048, _c_(657047, _a_(657044, _n_(657043, "g1", lambda: g1), "subs"), _n_(657045, "x", lambda: x),_n_(657046, "p", lambda: p)[0]), "subs"), _n_(657049, "y", lambda: y),_n_(657050, "p", lambda: p)[1])
    _l_(657052)
    return aux

#initial guess
x = [-450,-450]
_l_(657054)

#learning rate
alpha = 0.135
_l_(657055)

#initialization
iter = 0
_l_(657056)
e = 1000
_l_(657057)
grad = _c_(657060, _a_(657059, _n_(657058, "np", lambda: np), "array"), [])
_l_(657061)
error = _c_(657064, _a_(657063, _n_(657062, "np", lambda: np), "array"), [])
_l_(657065)

#gradient descent 
while _n_(657066, "e", lambda: e) > 0.000000001:
    _l_(657109)

    t = _c_(657069, _n_(657067, "objective", lambda: objective), _n_(657068, "x", lambda: x))
    _l_(657070)
    grad = [_c_(657073, _n_(657071, "gradient_1", lambda: gradient_1), _n_(657072, "x", lambda: x)),_c_(657076, _n_(657074, "gradient_2", lambda: gradient_2), _n_(657075, "x", lambda: x))]
    _l_(657077)
    change = _c_(657082, _a_(657079, _n_(657078, "np", lambda: np), "dot"), -_n_(657080, "alpha", lambda: alpha),_n_(657081, "grad", lambda: grad))
    _l_(657083)
    x = _c_(657088, _a_(657085, _n_(657084, "np", lambda: np), "add"), _n_(657086, "x", lambda: x),_n_(657087, "change", lambda: change))
    _l_(657089)
    e = _c_(657095, _n_(657090, "abs", lambda: abs), _c_(657093, _n_(657091, "objective", lambda: objective), _n_(657092, "x", lambda: x))-_n_(657094, "t", lambda: t))
    _l_(657096)
    error = _c_(657101, _a_(657098, _n_(657097, "np", lambda: np), "append"), _n_(657099, "error", lambda: error),_n_(657100, "e", lambda: e))
    _l_(657102)
    iter = _n_(657103, "iter", lambda: iter)+1
    _l_(657104)
    _c_(657107, _n_(657105, "print", lambda: print), "ITERATION NUMBER = ",_n_(657106, "iter", lambda: iter))
    _l_(657108)

#printing optimized values
_c_(657112, _n_(657110, "print", lambda: print), _n_(657111, "x", lambda: x))
_l_(657113)
#plotting error v/s iteration
i = _c_(657117, _a_(657115, _n_(657114, "np", lambda: np), "arange"), 1,_n_(657116, "iter", lambda: iter)+1)    
_l_(657118)    
_c_(657123, _a_(657120, _n_(657119, "plt", lambda: plt), "plot"), _n_(657121, "i", lambda: i),_n_(657122, "error", lambda: error))
_l_(657124)
_c_(657127, _a_(657126, _n_(657125, "plt", lambda: plt), "xlabel"), "Iterations")
_l_(657128)
_c_(657131, _a_(657130, _n_(657129, "plt", lambda: plt), "ylabel"), "Error") 
_l_(657132) 