# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selection_sort(nums):
    _l_(66124)

    for (i, n) in _c_(66101, _n_(66099, "enumerate", lambda: enumerate), _n_(66100, "nums", lambda: nums)):
        _l_(66121)

        mn = _c_(66111, _n_(66102, "min", lambda: min), _c_(66108, _n_(66103, "range", lambda: range), _n_(66104, "i", lambda: i), _c_(66107, _n_(66105, "len", lambda: len), _n_(66106, "nums", lambda: nums))), key=_a_(66110, _n_(66109, "nums", lambda: nums), "__getitem__"))
        _l_(66112)
        (_n_(66113, "nums", lambda: nums)[_n_(66114, "i", lambda: i)], _n_(66115, "nums", lambda: nums)[_n_(66116, "mn", lambda: mn)]) = (_n_(66117, "nums", lambda: nums)[_n_(66118, "mn", lambda: mn)], _n_(66119, "n", lambda: n))
        _l_(66120)
    aux = _n_(66122, "nums", lambda: nums)
    _l_(66123)
    return aux
user_input = _c_(66128, _a_(66127, _c_(66126, _n_(66125, "input", lambda: input), 'Input numbers separated by a comma:\n'), "strip"))
_l_(66129)
_c_(66134, _n_(66130, "print", lambda: print), _c_(66133, _n_(66131, "selection_sort", lambda: selection_sort), _n_(66132, "nums", lambda: nums)))
_l_(66135)