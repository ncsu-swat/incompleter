# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38968649/failure-to-scale-in-pyclipper-typeerror-zero-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sympy.geometry.polygon import Polygon
    _l_(400323)

except ImportError:
    pass
try:
    import pyclipper as pc
    _l_(400325)

except ImportError:
    pass

start_list = [(0, 2), (2, 2), (2, 0), (0, 0)]
_l_(400326)
scaled = _c_(400330, _a_(400328, _n_(400327, "pc", lambda: pc), "scale_to_clipper"), _n_(400329, "start_list", lambda: start_list))  # this works fine
_l_(400331)  # this works fine

as_poly = _c_(400334, _n_(400332, "Polygon", lambda: Polygon), *_n_(400333, "start_list", lambda: start_list))
_l_(400335)
new_list = [(_a_(400337, _n_(400336, "pt", lambda: pt), "x"), _a_(400339, _n_(400338, "pt", lambda: pt), "y")) for pt in _a_(400341, _n_(400340, "as_poly", lambda: as_poly), "vertices")]
_l_(400342)
assert _n_(400343, "new_list", lambda: new_list) == _n_(400344, "start_list", lambda: start_list)  # check that the lists are the same (this passes)
_l_(400345)  # check that the lists are the same (this passes)

fail_to_scale = _c_(400349, _a_(400347, _n_(400346, "pc", lambda: pc), "scale_to_clipper"), _n_(400348, "new_list", lambda: new_list))  # this fails
_l_(400350)  # this fails