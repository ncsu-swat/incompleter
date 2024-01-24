# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32312371/typeerror-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import random
        _l_(694818)

except ImportError:
        pass
l = []
_l_(694819)
for i in _c_(694821, _n_(694820, "range", lambda: range), 0,8):
        _l_(694835)

        key = _c_(694824, _a_(694823, _n_(694822, "random", lambda: random), "randrange"), 33,126)
        _l_(694825)
        key = _c_(694828, _n_(694826, "chr", lambda: chr), _n_(694827, "key", lambda: key))
        _l_(694829)
        _c_(694833, _a_(694831, _n_(694830, "l", lambda: l), "append"), _n_(694832, "key", lambda: key))
        _l_(694834)
_c_(694840, _n_(694836, "print", lambda: print), _c_(694839, _a_(694837, " ", "join"), _n_(694838, "l", lambda: l)))
_l_(694841)
x = (_c_(694849, _n_(694842, "round", lambda: round), _c_(694848, _n_(694843, "sum", lambda: sum), [_c_(694846, _n_(694844, "ord", lambda: ord), _n_(694845, "c", lambda: c)) for c in _n_(694847, "l", lambda: l)]) / 8) - 32)
_l_(694850)
_c_(694853, _n_(694851, "print", lambda: print), _n_(694852, "x", lambda: x))
_l_(694854)
if _n_(694855, "l", lambda: l)[_n_(694856, "i", lambda: i)]:
        _l_(694862)

        [_c_(694859, _n_(694857, "ord", lambda: ord), _n_(694858, "c", lambda: c)) for c in _n_(694860, "x", lambda: x)]
        _l_(694861)