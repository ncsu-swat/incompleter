# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33321732/python-rookie-prob-type-error-mistake
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a=_c_(649333, _n_(649332, "input", lambda: input), "Enter your first number")
_l_(649334)
b=_c_(649336, _n_(649335, "input", lambda: input), "And your second one")
_l_(649337)
if _n_(649338, "a", lambda: a)>_n_(649339, "b", lambda: b):
    _l_(649358)

    if _n_(649340, "a", lambda: a)%_n_(649341, "b", lambda: b)==0:
        _l_(649348)

        _c_(649343, _n_(649342, "print", lambda: print), "YES")
        _l_(649344)
    else:
        _c_(649346, _n_(649345, "print", lambda: print), "NO")
        _l_(649347)
else:
    if _n_(649349, "b", lambda: b)%_n_(649350, "a", lambda: a)==0:
        _l_(649357)

        _c_(649352, _n_(649351, "print", lambda: print), "YES")
        _l_(649353)
    else :
        _c_(649355, _n_(649354, "print", lambda: print), "NO")
        _l_(649356)