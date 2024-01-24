# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/24271752/why-do-i-get-a-nameerror-or-unboundlocalerror-from-using-a-named-exception
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
exc = None
_l_(380990)
try:
    _l_(380996)

    raise _n_(380991, "Exception", lambda: Exception)
    _l_(380992)
except _n_(380993, "Exception", lambda: Exception) as exc:
    _l_(380995)

    pass
    _l_(380994)
_c_(380999, _n_(380997, "print", lambda: print), _n_(380998, "exc", lambda: exc))
_l_(381000)