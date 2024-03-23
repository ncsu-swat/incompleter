# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selection_sort(nums):
    _l_(66194)

    for (i, n) in _c_(66171, _n_(66169, "enumerate", lambda: enumerate), _n_(66170, "nums", lambda: nums)):
        _l_(66191)

        mn = _c_(66181, _n_(66172, "min", lambda: min), _c_(66178, _n_(66173, "range", lambda: range), _n_(66174, "i", lambda: i), _c_(66177, _n_(66175, "len", lambda: len), _n_(66176, "nums", lambda: nums))), key=_a_(66180, _n_(66179, "nums", lambda: nums), "__getitem__"))
        _l_(66182)
        (_n_(66183, "nums", lambda: nums)[_n_(66184, "i", lambda: i)], _n_(66185, "nums", lambda: nums)[_n_(66186, "mn", lambda: mn)]) = (_n_(66187, "nums", lambda: nums)[_n_(66188, "mn", lambda: mn)], _n_(66189, "n", lambda: n))
        _l_(66190)
    aux = _n_(66192, "nums", lambda: nums)
    _l_(66193)
    return aux
nums = [_c_(66197, _n_(66195, "int", lambda: int), _n_(66196, "item", lambda: item)) for item in _c_(66200, _a_(66199, _n_(66198, "user_input", lambda: user_input), "split"), ',')]
_l_(66201)
_c_(66206, _n_(66202, "print", lambda: print), _c_(66205, _n_(66203, "selection_sort", lambda: selection_sort), _n_(66204, "nums", lambda: nums)))
_l_(66207)