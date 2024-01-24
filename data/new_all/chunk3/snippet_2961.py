# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56913538/typeerror-with-scipy-optimize-when-minimizing-cost-func
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scipy.optimize import minimize
    _l_(550205)

except ImportError:
    pass

def func(W):
    _l_(550240)

    W = _c_(550208, _a_(550207, _n_(550206, "W", lambda: W), "reshape"), 1,9) #(1,9)
    _l_(550209) #(1,9)
    Y = _c_(550213, _a_(550212, _a_(550211, _n_(550210, "df0", lambda: df0), "values"), "reshape"), 49,1) #(49,1)
    _l_(550214) #(49,1)
    X = _c_(550218, _a_(550217, _a_(550216, _n_(550215, "df1", lambda: df1), "values"), "reshape"), 49,1) #(49,9)
    _l_(550219) #(49,9)
    Z = _c_(550225, _a_(550221, _n_(550220, "np", lambda: np), "dot"), _n_(550222, "X", lambda: X), _a_(550224, _n_(550223, "W", lambda: W), "T")) #(49, 1)
    _l_(550226) #(49, 1)
    Z = _c_(550231, _a_(550228, _n_(550227, "np", lambda: np), "abs"), _n_(550229, "Z", lambda: Z) - _n_(550230, "Y", lambda: Y)) #(49, 1)
    _l_(550232) #(49, 1)
    Cost = _c_(550236, _a_(550234, _n_(550233, "np", lambda: np), "sum"), _n_(550235, "Z", lambda: Z) ,axis=0, keepdims=True)
    _l_(550237)
    aux = _n_(550238, "Cost", lambda: Cost)[0][0]  #float
    _l_(550239)  #float
    return aux  #float

W = _c_(550243, _a_(550242, _n_(550241, "np", lambda: np), "array"), [2,3,4,5,6,7,8,9,10])
_l_(550244)
cons = ({'type': 'ineq', 'fun': _n_(550245, "W", lambda: W)[1]-_n_(550246, "W", lambda: W)[0]})
_l_(550247)

result = _c_(550252, _n_(550248, "minimize", lambda: minimize), _n_(550249, "func", lambda: func), x0=_n_(550250, "W0", lambda: W0), constraints=_n_(550251, "cons", lambda: cons), method="SLSQP")
_l_(550253)