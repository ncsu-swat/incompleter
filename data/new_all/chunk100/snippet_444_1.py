# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(47630)

except ImportError:
    pass
_c_(47632, _n_(47631, "print", lambda: print), 'Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:')
_l_(47633)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47634)
data_groupby = _c_(47638, _a_(47636, _n_(47635, "it", lambda: it), "groupby"), _n_(47637, "str1", lambda: str1))
_l_(47639)
for (key, group) in _n_(47640, "data_groupby", lambda: data_groupby):
    _l_(47651)

    _c_(47643, _n_(47641, "print", lambda: print), 'Key:', _n_(47642, "key", lambda: key))
    _l_(47644)
    _c_(47649, _n_(47645, "print", lambda: print), 'Group:', _c_(47648, _n_(47646, "list", lambda: list), _n_(47647, "group", lambda: group)))
    _l_(47650)
_c_(47653, _n_(47652, "print", lambda: print), '\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:')
_l_(47654)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47655)
str1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
_l_(47656)
for (key, group) in _n_(47657, "data_groupby", lambda: data_groupby):
    _l_(47668)

    _c_(47660, _n_(47658, "print", lambda: print), 'Key:', _n_(47659, "key", lambda: key))
    _l_(47661)
    _c_(47666, _n_(47662, "print", lambda: print), 'Group:', _c_(47665, _n_(47663, "list", lambda: list), _n_(47664, "group", lambda: group)))
    _l_(47667)