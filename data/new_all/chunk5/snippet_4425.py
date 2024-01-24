# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57941113/typeerror-numpy-ndarray-with-scipy-optimize-minimize-numpy-ndarray-object-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
constraints = [
    {'type' : 'ineq', 'fun' : _n_(690003, "AA", lambda: AA)},
    {'type' : 'ineq', 'fun' : _n_(690004, "Ev", lambda: Ev)},
    {'type' : 'eq', 'fun' : _n_(690005, "Aeq", lambda: Aeq)},
    {'type' : 'eq', 'fun' : _n_(690006, "Beq", lambda: Beq)}
]
_l_(690007)
bnds = ((-5, 5))
_l_(690008)

z = _c_(690016, _n_(690009, "minimize", lambda: minimize), lambda z: _c_(690013, _n_(690010, "cost", lambda: cost), _n_(690011, "z", lambda: z),_n_(690012, "to", lambda: to)), x0=_n_(690014, "z0", lambda: z0), constraints=_n_(690015, "constraints", lambda: constraints), method='SLSQP')
_l_(690017)