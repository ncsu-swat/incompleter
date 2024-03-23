# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(16982)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(16985)

    aux = _n_(16983, "result", lambda: result)
    _l_(16984)
    return aux
list1 = [100, 200, 300, 400, 500, 600, 700]
_l_(16986)
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(16987)
list3 = [1, 2, 3, 4, 5, 6, 7]
_l_(16988)
_c_(16990, _n_(16989, "print", lambda: print), 'Original list:')
_l_(16991)
_c_(16994, _n_(16992, "print", lambda: print), 'list1:', _n_(16993, "list1", lambda: list1))
_l_(16995)
_c_(16998, _n_(16996, "print", lambda: print), 'list2:', _n_(16997, "list2", lambda: list2))
_l_(16999)
_c_(17002, _n_(17000, "print", lambda: print), 'list3:', _n_(17001, "list3", lambda: list3))
_l_(17003)
_c_(17005, _n_(17004, "print", lambda: print), '\nInterleave multiple lists:')
_l_(17006)
_c_(17013, _n_(17007, "print", lambda: print), _c_(17012, _n_(17008, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(17009, "list1", lambda: list1), _n_(17010, "list2", lambda: list2), _n_(17011, "list3", lambda: list3)))
_l_(17014)