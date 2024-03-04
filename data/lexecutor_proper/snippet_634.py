# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sinus2d(x, y):
    _l_(63888)

    aux = _c_(63882, _a_(63880, _n_(63879, "np", lambda: np), "sin"), _n_(63881, "x", lambda: x)) + _c_(63886, _a_(63884, _n_(63883, "np", lambda: np), "sin"), _n_(63885, "y", lambda: y))
    _l_(63887)
    return aux

xx, yy = _c_(63901, _a_(63890, _n_(63889, "np", lambda: np), "meshgrid"), _c_(63895, _a_(63892, _n_(63891, "np", lambda: np), "linspace"), 0,2*_a_(63894, _n_(63893, "np", lambda: np), "pi"),100), _c_(63900, _a_(63897, _n_(63896, "np", lambda: np), "linspace"), 0,2*_a_(63899, _n_(63898, "np", lambda: np), "pi"),100))
_l_(63902)
z = _c_(63906, _n_(63903, "sinus2d", lambda: sinus2d), _n_(63904, "xx", lambda: xx), _n_(63905, "yy", lambda: yy)) # Create the image on this grid
_l_(63907) # Create the image on this grid
try:
    import matplotlib.pyplot as plt
    _l_(63909)

except ImportError:
    pass
_c_(63913, _a_(63911, _n_(63910, "plt", lambda: plt), "imshow"), _n_(63912, "z", lambda: z), origin='lower', interpolation='none')
_l_(63914)
_c_(63917, _a_(63916, _n_(63915, "plt", lambda: plt), "show"))
_l_(63918)

z2 = _c_(63930, _n_(63919, "sinus2d", lambda: sinus2d), _c_(63924, _a_(63921, _n_(63920, "np", lambda: np), "linspace"), 0,2*_a_(63923, _n_(63922, "np", lambda: np), "pi"),100)[:,None], _c_(63929, _a_(63926, _n_(63925, "np", lambda: np), "linspace"), 0,2*_a_(63928, _n_(63927, "np", lambda: np), "pi"),100)[None,:])
_l_(63931)

condition = _n_(63932, "z", lambda: z)>0.6
_l_(63933)
z_new = _n_(63934, "z", lambda: z)[_n_(63935, "condition", lambda: condition)] # This will make your array 1D
_l_(63936) # This will make your array 1D

x_new = _n_(63937, "xx", lambda: xx)[_n_(63938, "condition", lambda: condition)]
_l_(63939)
y_new = _n_(63940, "yy", lambda: yy)[_n_(63941, "condition", lambda: condition)]
_l_(63942)
try:
    from scipy.interpolate import interp2d
    _l_(63944)

except ImportError:
    pass
interpolated = _c_(63949, _n_(63945, "interp2d", lambda: interp2d), _n_(63946, "x_new", lambda: x_new), _n_(63947, "y_new", lambda: y_new), _n_(63948, "z_new", lambda: z_new))
_l_(63950)

interpolated_grid = _c_(63958, _a_(63955, _c_(63954, _n_(63951, "interpolated", lambda: interpolated), _n_(63952, "xx", lambda: xx)[0], _n_(63953, "yy", lambda: yy)[:, 0]), "reshape"), _a_(63957, _n_(63956, "xx", lambda: xx), "shape"))
_l_(63959)

