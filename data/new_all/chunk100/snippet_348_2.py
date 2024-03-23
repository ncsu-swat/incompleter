# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute(nums):
    _l_(34835)

    result_perms = [[]]
    _l_(34810)
    for n in _n_(34811, "nums", lambda: nums):
        _l_(34832)

        new_perms = []
        _l_(34812)
        for perm in _n_(34813, "result_perms", lambda: result_perms):
            _l_(34831)

            for i in _c_(34818, _n_(34814, "range", lambda: range), _c_(34817, _n_(34815, "len", lambda: len), _n_(34816, "perm", lambda: perm)) + 1):
                _l_(34830)

                _c_(34826, _a_(34820, _n_(34819, "new_perms", lambda: new_perms), "append"), _n_(34821, "perm", lambda: perm)[:_n_(34822, "i", lambda: i)] + [_n_(34823, "n", lambda: n)] + _n_(34824, "perm", lambda: perm)[_n_(34825, "i", lambda: i):])
                _l_(34827)
                result_perms = _n_(34828, "new_perms", lambda: new_perms)
                _l_(34829)
    aux = _n_(34833, "result_perms", lambda: result_perms)
    _l_(34834)
    return aux
_c_(34838, _n_(34836, "print", lambda: print), 'Original Cofllection: ', _n_(34837, "my_nums", lambda: my_nums))
_l_(34839)
_c_(34844, _n_(34840, "print", lambda: print), 'Collection of distinct numbers:\n', _c_(34843, _n_(34841, "permute", lambda: permute), _n_(34842, "my_nums", lambda: my_nums)))
_l_(34845)