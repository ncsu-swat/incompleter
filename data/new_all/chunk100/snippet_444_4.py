# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(47758)

except ImportError:
    pass
_c_(47760, _n_(47759, "print", lambda: print), 'Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:')
_l_(47761)
data_groupby = _c_(47765, _a_(47763, _n_(47762, "it", lambda: it), "groupby"), _n_(47764, "str1", lambda: str1))
_l_(47766)
for (key, group) in _n_(47767, "data_groupby", lambda: data_groupby):
    _l_(47778)

    _c_(47770, _n_(47768, "print", lambda: print), 'Key:', _n_(47769, "key", lambda: key))
    _l_(47771)
    _c_(47776, _n_(47772, "print", lambda: print), 'Group:', _c_(47775, _n_(47773, "list", lambda: list), _n_(47774, "group", lambda: group)))
    _l_(47777)
_c_(47780, _n_(47779, "print", lambda: print), '\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:')
_l_(47781)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47782)
str1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
_l_(47783)
data_groupby = _c_(47787, _a_(47785, _n_(47784, "it", lambda: it), "groupby"), _n_(47786, "str1", lambda: str1))
_l_(47788)
for (key, group) in _n_(47789, "data_groupby", lambda: data_groupby):
    _l_(47800)

    _c_(47792, _n_(47790, "print", lambda: print), 'Key:', _n_(47791, "key", lambda: key))
    _l_(47793)
    _c_(47798, _n_(47794, "print", lambda: print), 'Group:', _c_(47797, _n_(47795, "list", lambda: list), _n_(47796, "group", lambda: group)))
    _l_(47799)