# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_nearest(array, values):
    _l_(64056)

    array = _c_(64038, _a_(64036, _n_(64035, "np", lambda: np), "asarray"), _n_(64037, "array", lambda: array))
    _l_(64039)

    # the last dim must be 1 to broadcast in (array - values) below.
    values = _c_(64043, _a_(64041, _n_(64040, "np", lambda: np), "expand_dims"), _n_(64042, "values", lambda: values), axis=-1) 
    _l_(64044) 

    indices = _c_(64051, _a_(64050, _c_(64049, _a_(64046, _n_(64045, "np", lambda: np), "abs"), _n_(64047, "array", lambda: array) - _n_(64048, "values", lambda: values)), "argmin"), axis=-1)
    _l_(64052)
    aux = _n_(64053, "array", lambda: array)[_n_(64054, "indices", lambda: indices)]
    _l_(64055)

    return aux


image = _c_(64059, _a_(64058, _n_(64057, "plt", lambda: plt), "imread"), 'example_3_band_image.jpg')
_l_(64060)

_c_(64064, _n_(64061, "print", lambda: print), _a_(64063, _n_(64062, "image", lambda: image), "shape")) # should be (nrows, ncols, 3)
_l_(64065) # should be (nrows, ncols, 3)

quantiles = _c_(64070, _a_(64067, _n_(64066, "np", lambda: np), "linspace"), 0, 255, num=2 ** 2, dtype=_a_(64069, _n_(64068, "np", lambda: np), "uint8"))
_l_(64071)

quantiled_image = _c_(64075, _n_(64072, "find_nearest", lambda: find_nearest), _n_(64073, "quantiles", lambda: quantiles), _n_(64074, "image", lambda: image))
_l_(64076)

_c_(64080, _n_(64077, "print", lambda: print), _a_(64079, _n_(64078, "quantiled_image", lambda: quantiled_image), "shape")) # should be (nrows, ncols, 3)
_l_(64081) # should be (nrows, ncols, 3)

