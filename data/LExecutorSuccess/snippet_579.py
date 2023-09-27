# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11011756/is-there-any-pythonic-way-to-combine-two-dicts-adding-values-for-keys-that-appe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(1542270)

except ImportError:
    pass

A = _c_(1542272, _n_(1542271, "Counter", lambda: Counter), {'a':1, 'b':2, 'c':3})
_l_(1542273)
B = _c_(1542275, _n_(1542274, "Counter", lambda: Counter), {'b':3, 'c':4, 'd':5}) 
_l_(1542276) 
C = _c_(1542278, _n_(1542277, "Counter", lambda: Counter), {'a': 5, 'e':3})
_l_(1542279)
list_of_counts = [_n_(1542280, "A", lambda: A), _n_(1542281, "B", lambda: B), _n_(1542282, "C", lambda: C)]
_l_(1542283)

total = _c_(1542288, _n_(1542284, "sum", lambda: sum), _n_(1542285, "list_of_counts", lambda: list_of_counts), _c_(1542287, _n_(1542286, "Counter", lambda: Counter)))
_l_(1542289)

_c_(1542292, _n_(1542290, "print", lambda: print), _n_(1542291, "total", lambda: total))
_l_(1542293)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

total = _c_(1542295, _n_(1542294, "Counter", lambda: Counter))
_l_(1542296)
for count in _n_(1542297, "list_of_counts", lambda: list_of_counts):
    _l_(1542300)

    total += _n_(1542298, "count", lambda: count)
    _l_(1542299)
_c_(1542303, _n_(1542301, "print", lambda: print), _n_(1542302, "total", lambda: total))
_l_(1542304)
# Counter({'c': 7, 'a': 6, 'b': 5, 'd': 5, 'e': 3})

