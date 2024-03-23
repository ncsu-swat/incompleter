# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(47714)

except ImportError:
    pass
_c_(47716, _n_(47715, "print", lambda: print), 'Iterate over characters of a string and display\nconsecutive keys and groups from the iterable:')
_l_(47717)
str1 = 'AAAAJJJJHHHHNWWWEERRRSSSOOIIU'
_l_(47718)
data_groupby = _c_(47722, _a_(47720, _n_(47719, "it", lambda: it), "groupby"), _n_(47721, "str1", lambda: str1))
_l_(47723)
for (key, group) in _n_(47724, "data_groupby", lambda: data_groupby):
    _l_(47735)

    _c_(47727, _n_(47725, "print", lambda: print), 'Key:', _n_(47726, "key", lambda: key))
    _l_(47728)
    _c_(47733, _n_(47729, "print", lambda: print), 'Group:', _c_(47732, _n_(47730, "list", lambda: list), _n_(47731, "group", lambda: group)))
    _l_(47734)
_c_(47737, _n_(47736, "print", lambda: print), '\nIterate over elements of a list and display\nconsecutive keys and groups from the iterable:')
_l_(47738)
str1 = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8]
_l_(47739)
data_groupby = _c_(47743, _a_(47741, _n_(47740, "it", lambda: it), "groupby"), _n_(47742, "str1", lambda: str1))
_l_(47744)
for (key, group) in _n_(47745, "data_groupby", lambda: data_groupby):
    _l_(47756)

    _c_(47748, _n_(47746, "print", lambda: print), 'Key:', _n_(47747, "key", lambda: key))
    _l_(47749)
    _c_(47754, _n_(47750, "print", lambda: print), 'Group:', _c_(47753, _n_(47751, "list", lambda: list), _n_(47752, "group", lambda: group)))
    _l_(47755)