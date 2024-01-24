# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73453914/i-am-getting-this-error-if-l-2-0-typeerror-unsupported-operand-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = 'one two three four five six'
_l_(365838)
l = _c_(365841, _a_(365840, _n_(365839, "s", lambda: s), "split"))
_l_(365842)
i = 0
_l_(365843)
l1 = []
_l_(365844)
while _n_(365845, "i", lambda: i) < _c_(365848, _n_(365846, "len", lambda: len), _n_(365847, "l", lambda: l)):
    _l_(365865)

    if _n_(365849, "l", lambda: l) % 2 == 0:
        _l_(365862)

        _c_(365854, _a_(365851, _n_(365850, "l1", lambda: l1), "append"), _n_(365852, "l", lambda: l)[_n_(365853, "i", lambda: i)])
        _l_(365855)
    else:
        _c_(365860, _a_(365857, _n_(365856, "l1", lambda: l1), "append"), _n_(365858, "l", lambda: l)[_n_(365859, "i", lambda: i)][::-1])
        _l_(365861)
    i = _n_(365863, "i", lambda: i)+1
    _l_(365864)

output = _c_(365868, _a_(365866, ' ', "join"), _n_(365867, "l1", lambda: l1))
_l_(365869)
_c_(365872, _n_(365870, "print", lambda: print), _n_(365871, "output", lambda: output))
_l_(365873)