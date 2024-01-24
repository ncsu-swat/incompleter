# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72094887/int-object-is-not-iterable-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n=100
_l_(581184)
try:
  from collections import OrderedDict
  _l_(581186)

except ImportError:
  pass

for i in _c_(581190, _n_(581187, "range", lambda: range), -_n_(581188, "n", lambda: n), _n_(581189, "n", lambda: n)):
  _l_(581208)

  if (_n_(581191, "i", lambda: i) % 3 == 0) or (_n_(581192, "i", lambda: i) % 5 == 0):
    _l_(581207)

    _c_(581195, _n_(581193, "print", lambda: print), _n_(581194, "i", lambda: i))
    _l_(581196)
  elif (_n_(581197, "i", lambda: i) % 3 == 0) and (_n_(581198, "i", lambda: i) % 5 ==0):
    _l_(581206)

    _c_(581201, _n_(581199, "print", lambda: print), _n_(581200, "i", lambda: i))
    _l_(581202)
  elif _n_(581203, "i", lambda: i) < 0:
    _l_(581205)

    pass
    _l_(581204)
_c_(581211, _n_(581209, "sum", lambda: sum), _n_(581210, "i", lambda: i))
_l_(581212)