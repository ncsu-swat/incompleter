# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = _c_(63048, _n_(63047, "range", lambda: range), 5)
_l_(63049)
_c_(63054, _n_(63050, "print", lambda: print), _c_(63053, _n_(63051, "list", lambda: list), _n_(63052, "a", lambda: a)))
_l_(63055)
[0, 1, 2, 3, 4]
_l_(63056)
_c_(63061, _n_(63057, "print", lambda: print), _c_(63060, _n_(63058, "list", lambda: list), _n_(63059, "a", lambda: a)))
_l_(63062)
[0, 1, 2, 3, 4]
_l_(63063)

b = _c_(63065, _n_(63064, "my_crappy_range", lambda: my_crappy_range), 5)
_l_(63066)
_c_(63071, _n_(63067, "print", lambda: print), _c_(63070, _n_(63068, "list", lambda: list), _n_(63069, "b", lambda: b)))
_l_(63072)
[0, 1, 2, 3, 4]
_l_(63073)
_c_(63078, _n_(63074, "print", lambda: print), _c_(63077, _n_(63075, "list", lambda: list), _n_(63076, "b", lambda: b)))
_l_(63079)
[]
_l_(63080)
try:
    import collections.abc
    _l_(63082)

except ImportError:
    pass
_c_(63087, _n_(63083, "isinstance", lambda: isinstance), _n_(63084, "a", lambda: a), _a_(63086, _a_(63085, collections, "abc"), "Sequence"))
_l_(63088)
True
_l_(63089)

_n_(63090, "a", lambda: a)[3]         # indexable
_l_(63091)         # indexable
3
_l_(63092)
_c_(63095, _n_(63093, "len", lambda: len), _n_(63094, "a", lambda: a))       # sized
_l_(63096)       # sized
5
_l_(63097)
3 in _n_(63098, "a", lambda: a)       # membership
_l_(63099)       # membership
True
_l_(63100)
_c_(63103, _n_(63101, "reversed", lambda: reversed), _n_(63102, "a", lambda: a))  # reversible
_l_(63104)  # reversible
_c_(63107, _a_(63106, _n_(63105, "a", lambda: a), "index"), 3)   # implements 'index'
_l_(63108)   # implements 'index'
3
_l_(63109)
_c_(63112, _a_(63111, _n_(63110, "a", lambda: a), "count"), 3)   # implements 'count'
_l_(63113)   # implements 'count'
1
_l_(63114)

