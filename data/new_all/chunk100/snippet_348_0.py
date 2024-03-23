# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute(nums):
    _l_(34762)

    result_perms = [[]]
    _l_(34739)
    for n in _n_(34740, "nums", lambda: nums):
        _l_(34759)

        new_perms = []
        _l_(34741)
        for perm in _n_(34742, "result_perms", lambda: result_perms):
            _l_(34758)

            for i in _c_(34747, _n_(34743, "range", lambda: range), _c_(34746, _n_(34744, "len", lambda: len), _n_(34745, "perm", lambda: perm)) + 1):
                _l_(34757)

                _c_(34755, _a_(34749, _n_(34748, "new_perms", lambda: new_perms), "append"), _n_(34750, "perm", lambda: perm)[:_n_(34751, "i", lambda: i)] + [_n_(34752, "n", lambda: n)] + _n_(34753, "perm", lambda: perm)[_n_(34754, "i", lambda: i):])
                _l_(34756)
    aux = _n_(34760, "result_perms", lambda: result_perms)
    _l_(34761)
    return aux
my_nums = [1, 2, 3]
_l_(34763)
_c_(34766, _n_(34764, "print", lambda: print), 'Original Cofllection: ', _n_(34765, "my_nums", lambda: my_nums))
_l_(34767)
_c_(34772, _n_(34768, "print", lambda: print), 'Collection of distinct numbers:\n', _c_(34771, _n_(34769, "permute", lambda: permute), _n_(34770, "my_nums", lambda: my_nums)))
_l_(34773)