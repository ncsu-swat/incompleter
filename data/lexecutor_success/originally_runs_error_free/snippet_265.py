# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def myfunc(x):
  _l_(1544762)

  try:
    _l_(1544761)

    _c_(1544754, _n_(1544753, "x", lambda: x))
    _l_(1544755)
  except _n_(1544756, "TypeError", lambda: TypeError):
    _l_(1544760)

    raise _c_(1544758, _n_(1544757, "Exception", lambda: Exception), "Not callable")
    _l_(1544759)

