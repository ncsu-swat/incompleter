# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72255624/getting-nameerror-name-count-even-is-not-defined-when-trying-to-get-the-odd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count_odd=0
_l_(364256)
for select in [321,13,42,9785,20,33,834,903,22]:
    _l_(364263)

    if _n_(364257, "select", lambda: select) % 2 == 0:
        _l_(364262)

        count_even=_n_(364258, "count_even", lambda: count_even) + 1
        _l_(364259)
    else:
        count_odd=  _n_(364260, "count_odd", lambda: count_odd) + 1
        _l_(364261)
_c_(364266, _n_(364264, "print", lambda: print), _n_(364265, "count_even", lambda: count_even))
_l_(364267)
_c_(364270, _n_(364268, "print", lambda: print), _n_(364269, "count_odd", lambda: count_odd))
_l_(364271)