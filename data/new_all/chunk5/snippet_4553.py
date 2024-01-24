# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55657722/python-multiprocessing-errors-when-wrapped-inside-a-function-attributeerror-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from multiprocessing import Pool
  _l_(673062)

except ImportError:
  pass
try:
  import time
  _l_(673064)

except ImportError:
  pass

def test():
  _l_(673091)

  def _foo(my_number):
    _l_(673074)

    square = _n_(673065, "my_number", lambda: my_number) * _n_(673066, "my_number", lambda: my_number)
    _l_(673067)
    _c_(673070, _a_(673069, _n_(673068, "time", lambda: time), "sleep"), 1)
    _l_(673071)
    aux = _n_(673072, "square", lambda: square) 
    _l_(673073) 
    return aux 

  with _c_(673076, _n_(673075, "Pool", lambda: Pool)) as p:
    _l_(673086)

    r = _c_(673084, _n_(673077, "list", lambda: list), _c_(673083, _a_(673079, _n_(673078, "p", lambda: p), "imap"), _n_(673080, "_foo", lambda: _foo), _c_(673082, _n_(673081, "range", lambda: range), 30)))
    _l_(673085)
  _c_(673089, _n_(673087, "print", lambda: print), _n_(673088, "r", lambda: r))
  _l_(673090)

_c_(673093, _n_(673092, "test", lambda: test))
_l_(673094)