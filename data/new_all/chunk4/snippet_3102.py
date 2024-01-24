# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45996311/trying-to-sum-up-nested-lists-but-receive-error-typeerror-unsupported-operand-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count = 0
_l_(619764)
lista=[[] for q in _c_(619766, _n_(619765, "range", lambda: range), 5)]
_l_(619767)
while _n_(619768, "count", lambda: count)<_c_(619771, _n_(619769, "len", lambda: len), _n_(619770, "lista", lambda: lista)):
    _l_(619785)

    try:
        import random
        _l_(619773)

    except ImportError:
        pass
    c=_c_(619776, _a_(619775, _n_(619774, "random", lambda: random), "randrange"), 1,7,1)
    _l_(619777)
    _c_(619782, _a_(619780, _n_(619778, "lista", lambda: lista)[_n_(619779, "count", lambda: count)], "append"), _n_(619781, "c", lambda: c))
    _l_(619783)
    count += 1
    _l_(619784)

_c_(619788, _n_(619786, "print", lambda: print), _n_(619787, "lista", lambda: lista))
_l_(619789)
total=_c_(619792, _n_(619790, "sum", lambda: sum), _n_(619791, "lista", lambda: lista))
_l_(619793)