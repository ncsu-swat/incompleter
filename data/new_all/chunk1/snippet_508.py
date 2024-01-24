# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77589004/problem-execute-calculations-in-a-nested-loop-typeerror-numpy-float64-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from numpy import mean
  _l_(418060)

except ImportError:
  pass
try:
  import math
  _l_(418062)

except ImportError:
  pass

values = [5, 2, 3, 4, 0]
_l_(418063)

mean = _c_(418066, _n_(418064, "mean", lambda: mean), _n_(418065, "values", lambda: values))
_l_(418067)

for x in _n_(418068, "values", lambda: values):
  _l_(418089)

  values_subtraction_mean = _n_(418069, "x", lambda: x) - _n_(418070, "mean", lambda: mean)
  _l_(418071)
  _c_(418074, _n_(418072, "print", lambda: print), _n_(418073, "values_subtraction_mean", lambda: values_subtraction_mean))
  _l_(418075)
  #2.2, -0.8, 0.2, 1.2, -2.8

  for y in _n_(418076, "values_subtraction_mean", lambda: values_subtraction_mean):
    _l_(418088)

    result = _c_(418082, _n_(418077, "sum", lambda: sum), _c_(418081, _a_(418079, _n_(418078, "math", lambda: math), "sqrt"), _n_(418080, "y", lambda: y)))
    _l_(418083)
    _c_(418086, _n_(418084, "print", lambda: print), _n_(418085, "result", lambda: result))
    _l_(418087)