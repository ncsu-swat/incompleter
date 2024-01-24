# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50382699/typeerror-while-using-scipy-optimization-algorithms-with-rbf-kernel-in-gaussianp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(702058)

except ImportError:
    pass
try:
    from scipy.optimize import minimize,least_squares
    _l_(702060)

except ImportError:
    pass
try:
    from sklearn.gaussian_process import GaussianProcessRegressor
    _l_(702062)

except ImportError:
    pass
try:
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
    _l_(702064)

except ImportError:
    pass
try:
    from scipy.optimize import least_squares,rosen
    _l_(702066)

except ImportError:
    pass

def trust_region_optimizer(obj_func, initial_theta, bounds):
    _l_(702078)

    trust_region_method = _c_(702071, _n_(702067, "least_squares", lambda: least_squares), 1/_n_(702068, "obj_func", lambda: obj_func),_n_(702069, "initial_theta", lambda: initial_theta),_n_(702070, "bounds", lambda: bounds),method='trf')
    _l_(702072)
    aux = (_a_(702074, _n_(702073, "trust_region_method", lambda: trust_region_method), "x"),_a_(702076, _n_(702075, "trust_region_method", lambda: trust_region_method), "fun"))
    _l_(702077)
    return aux

X=_c_(702082, _a_(702081, _a_(702080, _n_(702079, "np", lambda: np), "random"), "random"), (10,4))
_l_(702083)
y=_c_(702087, _a_(702086, _a_(702085, _n_(702084, "np", lambda: np), "random"), "random"), (10,1))
_l_(702088)
kernel = _c_(702090, _n_(702089, "C", lambda: C), 1.0, (1e-5, 1e5)) * _c_(702092, _n_(702091, "RBF", lambda: RBF), 10.0)
_l_(702093)
gp = _c_(702099, _n_(702094, "GaussianProcessRegressor", lambda: GaussianProcessRegressor), kernel=_n_(702095, "kernel", lambda: kernel), optimizer = _c_(702098, _n_(702096, "trust_region_optimizer", lambda: trust_region_optimizer), _n_(702097, "rosen", lambda: rosen),[10,20,30,40], [0,100]), alpha =1.2, n_restarts_optimizer=10)
_l_(702100)
_c_(702105, _a_(702102, _n_(702101, "gp", lambda: gp), "fit"), _n_(702103, "X", lambda: X), _n_(702104, "y", lambda: y))
_l_(702106)