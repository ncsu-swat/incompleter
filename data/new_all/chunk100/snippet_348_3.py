# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute(nums):
    _l_(34870)

    result_perms = [[]]
    _l_(34846)
    for n in _n_(34847, "nums", lambda: nums):
        _l_(34867)

        for perm in _n_(34848, "result_perms", lambda: result_perms):
            _l_(34866)

            for i in _c_(34853, _n_(34849, "range", lambda: range), _c_(34852, _n_(34850, "len", lambda: len), _n_(34851, "perm", lambda: perm)) + 1):
                _l_(34865)

                _c_(34861, _a_(34855, _n_(34854, "new_perms", lambda: new_perms), "append"), _n_(34856, "perm", lambda: perm)[:_n_(34857, "i", lambda: i)] + [_n_(34858, "n", lambda: n)] + _n_(34859, "perm", lambda: perm)[_n_(34860, "i", lambda: i):])
                _l_(34862)
                result_perms = _n_(34863, "new_perms", lambda: new_perms)
                _l_(34864)
    aux = _n_(34868, "result_perms", lambda: result_perms)
    _l_(34869)
    return aux
my_nums = [1, 2, 3]
_l_(34871)
_c_(34874, _n_(34872, "print", lambda: print), 'Original Cofllection: ', _n_(34873, "my_nums", lambda: my_nums))
_l_(34875)
_c_(34880, _n_(34876, "print", lambda: print), 'Collection of distinct numbers:\n', _c_(34879, _n_(34877, "permute", lambda: permute), _n_(34878, "my_nums", lambda: my_nums)))
_l_(34881)