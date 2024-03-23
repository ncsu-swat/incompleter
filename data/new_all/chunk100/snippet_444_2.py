# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(47670)

except ImportError:
    pass
_c_(47672, _n_(47671, "print", lambda: print), 'Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:')
_l_(47673)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47674)
data_groupby = _c_(47678, _a_(47676, _n_(47675, "it", lambda: it), "groupby"), _n_(47677, "str1", lambda: str1))
_l_(47679)
for (key, group) in _n_(47680, "data_groupby", lambda: data_groupby):
    _l_(47691)

    _c_(47683, _n_(47681, "print", lambda: print), 'Key:', _n_(47682, "key", lambda: key))
    _l_(47684)
    _c_(47689, _n_(47685, "print", lambda: print), 'Group:', _c_(47688, _n_(47686, "list", lambda: list), _n_(47687, "group", lambda: group)))
    _l_(47690)
_c_(47693, _n_(47692, "print", lambda: print), '\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:')
_l_(47694)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47695)
data_groupby = _c_(47699, _a_(47697, _n_(47696, "it", lambda: it), "groupby"), _n_(47698, "str1", lambda: str1))
_l_(47700)
for (key, group) in _n_(47701, "data_groupby", lambda: data_groupby):
    _l_(47712)

    _c_(47704, _n_(47702, "print", lambda: print), 'Key:', _n_(47703, "key", lambda: key))
    _l_(47705)
    _c_(47710, _n_(47706, "print", lambda: print), 'Group:', _c_(47709, _n_(47707, "list", lambda: list), _n_(47708, "group", lambda: group)))
    _l_(47711)