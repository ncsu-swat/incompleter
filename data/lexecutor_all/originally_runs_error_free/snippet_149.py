# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000, 'e':3000}
_l_(1548189)
try:
    from collections import defaultdict
    _l_(1548191)

except ImportError:
    pass
try:
    from collections import OrderedDict
    _l_(1548193)

except ImportError:
    pass

groupedByValue = _c_(1548196, _n_(1548194, "defaultdict", lambda: defaultdict), _n_(1548195, "list", lambda: list))
_l_(1548197)
for key, value in _c_(1548202, _n_(1548198, "sorted", lambda: sorted), _c_(1548201, _a_(1548200, _n_(1548199, "stats", lambda: stats), "items"))):
    _l_(1548209)

    _c_(1548207, _a_(1548205, _n_(1548203, "groupedByValue", lambda: groupedByValue)[_n_(1548204, "value", lambda: value)], "append"), _n_(1548206, "key", lambda: key))
    _l_(1548208)

# {1000: ['a'], 3000: ['b', 'd', 'e'], 100: ['c']}

_n_(1548210, "groupedByValue", lambda: groupedByValue)[_c_(1548213, _n_(1548211, "max", lambda: max), _n_(1548212, "groupedByValue", lambda: groupedByValue))]
_l_(1548214)
# ['b', 'd', 'e']

