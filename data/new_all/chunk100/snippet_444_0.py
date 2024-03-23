# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(47590)

except ImportError:
    pass
_c_(47592, _n_(47591, "print", lambda: print), 'Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:')
_l_(47593)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47594)
for (key, group) in _n_(47595, "data_groupby", lambda: data_groupby):
    _l_(47606)

    _c_(47598, _n_(47596, "print", lambda: print), 'Key:', _n_(47597, "key", lambda: key))
    _l_(47599)
    _c_(47604, _n_(47600, "print", lambda: print), 'Group:', _c_(47603, _n_(47601, "list", lambda: list), _n_(47602, "group", lambda: group)))
    _l_(47605)
_c_(47608, _n_(47607, "print", lambda: print), '\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:')
_l_(47609)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47610)
str1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
_l_(47611)
data_groupby = _c_(47615, _a_(47613, _n_(47612, "it", lambda: it), "groupby"), _n_(47614, "str1", lambda: str1))
_l_(47616)
for (key, group) in _n_(47617, "data_groupby", lambda: data_groupby):
    _l_(47628)

    _c_(47620, _n_(47618, "print", lambda: print), 'Key:', _n_(47619, "key", lambda: key))
    _l_(47621)
    _c_(47626, _n_(47622, "print", lambda: print), 'Group:', _c_(47625, _n_(47623, "list", lambda: list), _n_(47624, "group", lambda: group)))
    _l_(47627)