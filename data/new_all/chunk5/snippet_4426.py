# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57941113/typeerror-numpy-ndarray-with-scipy-optimize-minimize-numpy-ndarray-object-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
constraints = [
    {'type' : 'ineq', 'fun' : _n_(659290, "AA", lambda: AA)},
    {'type' : 'ineq', 'fun' : _n_(659291, "Ev", lambda: Ev)},
    {'type' : 'eq', 'fun' : _n_(659292, "Aeq", lambda: Aeq)},
    {'type' : 'eq', 'fun' : _n_(659293, "Beq", lambda: Beq)}
]
_l_(659294)
bnds = ((-5, 5))
_l_(659295)

z = _c_(659303, _n_(659296, "minimize", lambda: minimize), lambda z: _c_(659300, _n_(659297, "cost", lambda: cost), _n_(659298, "z", lambda: z),_n_(659299, "to", lambda: to)), x0=_n_(659301, "z0", lambda: z0), constraints=_n_(659302, "constraints", lambda: constraints), method='SLSQP')
_l_(659304)