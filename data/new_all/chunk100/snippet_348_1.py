# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute(nums):
    _l_(34798)

    for n in _n_(34774, "nums", lambda: nums):
        _l_(34795)

        new_perms = []
        _l_(34775)
        for perm in _n_(34776, "result_perms", lambda: result_perms):
            _l_(34794)

            for i in _c_(34781, _n_(34777, "range", lambda: range), _c_(34780, _n_(34778, "len", lambda: len), _n_(34779, "perm", lambda: perm)) + 1):
                _l_(34793)

                _c_(34789, _a_(34783, _n_(34782, "new_perms", lambda: new_perms), "append"), _n_(34784, "perm", lambda: perm)[:_n_(34785, "i", lambda: i)] + [_n_(34786, "n", lambda: n)] + _n_(34787, "perm", lambda: perm)[_n_(34788, "i", lambda: i):])
                _l_(34790)
                result_perms = _n_(34791, "new_perms", lambda: new_perms)
                _l_(34792)
    aux = _n_(34796, "result_perms", lambda: result_perms)
    _l_(34797)
    return aux
my_nums = [1, 2, 3]
_l_(34799)
_c_(34802, _n_(34800, "print", lambda: print), 'Original Cofllection: ', _n_(34801, "my_nums", lambda: my_nums))
_l_(34803)
_c_(34808, _n_(34804, "print", lambda: print), 'Collection of distinct numbers:\n', _c_(34807, _n_(34805, "permute", lambda: permute), _n_(34806, "my_nums", lambda: my_nums)))
_l_(34809)