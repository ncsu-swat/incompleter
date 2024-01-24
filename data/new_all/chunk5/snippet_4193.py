# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61851719/unsupported-operand-type-error-while-evaluating-gradient-using-sympy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(652383)

except ImportError:
    pass
try:
    import numpy as np
    _l_(652385)

except ImportError:
    pass
try:
    import math
    _l_(652387)

except ImportError:
    pass
try:
    import sympy as sym
    _l_(652389)

except ImportError:
    pass

x,y = _c_(652392, _a_(652391, _n_(652390, "sym", lambda: sym), "symbols"), 'x y')
_l_(652393)

 #objective function
def objective(p):
    _l_(652421)

    x = _n_(652394, "p", lambda: p)[0]
    _l_(652395)
    y = _n_(652396, "p", lambda: p)[1]
    _l_(652397)
    aux = -(_n_(652398, "y", lambda: y)+47)*_c_(652408, _a_(652400, _n_(652399, "sym", lambda: sym), "sin"), _c_(652407, _a_(652402, _n_(652401, "sym", lambda: sym), "sqrt"), _c_(652406, _n_(652403, "abs", lambda: abs), (_n_(652404, "x", lambda: x)/2)+_n_(652405, "y", lambda: y)+47))) - _n_(652409, "x", lambda: x)*_c_(652419, _a_(652411, _n_(652410, "sym", lambda: sym), "sin"), _c_(652418, _a_(652413, _n_(652412, "sym", lambda: sym), "sqrt"), _c_(652417, _n_(652414, "abs", lambda: abs), _n_(652415, "x", lambda: x)-(_n_(652416, "y", lambda: y)+47))))
    _l_(652420)
    return aux

 #gradient wrt x
def gradient_1(p):
    _l_(652441)

    g0 = _c_(652429, _a_(652423, _n_(652422, "sym", lambda: sym), "diff"), _c_(652427, _n_(652424, "objective", lambda: objective), [_n_(652425, "x", lambda: x),_n_(652426, "y", lambda: y)]),_n_(652428, "x", lambda: x))
    _l_(652430)
    aux = _c_(652439, _a_(652436, _c_(652435, _a_(652432, _n_(652431, "g0", lambda: g0), "subs"), _n_(652433, "x", lambda: x),_n_(652434, "p", lambda: p)[0]), "subs"), _n_(652437, "y", lambda: y),_n_(652438, "p", lambda: p)[1])
    _l_(652440)
    return aux

#gradient wrt y
def gradient_2(p):
    _l_(652461)

    g1 = _c_(652449, _a_(652443, _n_(652442, "sym", lambda: sym), "diff"), _c_(652447, _n_(652444, "objective", lambda: objective), [_n_(652445, "x", lambda: x),_n_(652446, "y", lambda: y)]),_n_(652448, "y", lambda: y))
    _l_(652450)
    aux = _c_(652459, _a_(652456, _c_(652455, _a_(652452, _n_(652451, "g1", lambda: g1), "subs"), _n_(652453, "x", lambda: x),_n_(652454, "p", lambda: p)[0]), "subs"), _n_(652457, "y", lambda: y),_n_(652458, "p", lambda: p)[1])
    _l_(652460)
    return aux

#initial guess
x = [-450,-450]
_l_(652462)

#learning rate
alpha = 0.135
_l_(652463)

#initialization
iter = 0
_l_(652464)
e = 1000
_l_(652465)
grad = _c_(652468, _a_(652467, _n_(652466, "np", lambda: np), "array"), [])
_l_(652469)
error = _c_(652472, _a_(652471, _n_(652470, "np", lambda: np), "array"), [])
_l_(652473)

#gradient descent 
while _n_(652474, "e", lambda: e) > 0.000000001:
    _l_(652517)

    t = _c_(652477, _n_(652475, "objective", lambda: objective), _n_(652476, "x", lambda: x))
    _l_(652478)
    grad = [_c_(652481, _n_(652479, "gradient_1", lambda: gradient_1), _n_(652480, "x", lambda: x)),_c_(652484, _n_(652482, "gradient_2", lambda: gradient_2), _n_(652483, "x", lambda: x))]
    _l_(652485)
    change = _c_(652490, _a_(652487, _n_(652486, "np", lambda: np), "dot"), -_n_(652488, "alpha", lambda: alpha),_n_(652489, "grad", lambda: grad))
    _l_(652491)
    x = _c_(652496, _a_(652493, _n_(652492, "np", lambda: np), "add"), _n_(652494, "x", lambda: x),_n_(652495, "change", lambda: change))
    _l_(652497)
    e = _c_(652503, _n_(652498, "abs", lambda: abs), _c_(652501, _n_(652499, "objective", lambda: objective), _n_(652500, "x", lambda: x))-_n_(652502, "t", lambda: t))
    _l_(652504)
    error = _c_(652509, _a_(652506, _n_(652505, "np", lambda: np), "append"), _n_(652507, "error", lambda: error),_n_(652508, "e", lambda: e))
    _l_(652510)
    iter = _n_(652511, "iter", lambda: iter)+1
    _l_(652512)
    _c_(652515, _n_(652513, "print", lambda: print), "ITERATION NUMBER = ",_n_(652514, "iter", lambda: iter))
    _l_(652516)

#printing optimized values
_c_(652520, _n_(652518, "print", lambda: print), _n_(652519, "x", lambda: x))
_l_(652521)
#plotting error v/s iteration
i = _c_(652525, _a_(652523, _n_(652522, "np", lambda: np), "arange"), 1,_n_(652524, "iter", lambda: iter)+1)    
_l_(652526)    
_c_(652531, _a_(652528, _n_(652527, "plt", lambda: plt), "plot"), _n_(652529, "i", lambda: i),_n_(652530, "error", lambda: error))
_l_(652532)
_c_(652535, _a_(652534, _n_(652533, "plt", lambda: plt), "xlabel"), "Iterations")
_l_(652536)
_c_(652539, _a_(652538, _n_(652537, "plt", lambda: plt), "ylabel"), "Error") 
_l_(652540) 