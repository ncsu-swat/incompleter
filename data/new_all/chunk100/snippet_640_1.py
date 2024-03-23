# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selection_sort(nums):
    _l_(66150)

    for (i, n) in _c_(66138, _n_(66136, "enumerate", lambda: enumerate), _n_(66137, "nums", lambda: nums)):
        _l_(66147)

        (_n_(66139, "nums", lambda: nums)[_n_(66140, "i", lambda: i)], _n_(66141, "nums", lambda: nums)[_n_(66142, "mn", lambda: mn)]) = (_n_(66143, "nums", lambda: nums)[_n_(66144, "mn", lambda: mn)], _n_(66145, "n", lambda: n))
        _l_(66146)
    aux = _n_(66148, "nums", lambda: nums)
    _l_(66149)
    return aux
user_input = _c_(66154, _a_(66153, _c_(66152, _n_(66151, "input", lambda: input), 'Input numbers separated by a comma:\n'), "strip"))
_l_(66155)
nums = [_c_(66158, _n_(66156, "int", lambda: int), _n_(66157, "item", lambda: item)) for item in _c_(66161, _a_(66160, _n_(66159, "user_input", lambda: user_input), "split"), ',')]
_l_(66162)
_c_(66167, _n_(66163, "print", lambda: print), _c_(66166, _n_(66164, "selection_sort", lambda: selection_sort), _n_(66165, "nums", lambda: nums)))
_l_(66168)