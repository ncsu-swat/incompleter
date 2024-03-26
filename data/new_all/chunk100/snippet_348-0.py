# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def permute(nums):
    _l_(111639)

    result_perms = [[]]
    _l_(111614)
    for n in _n_(111615, "nums", lambda: nums):
        _l_(111636)

        new_perms = []
        _l_(111616)
        for perm in _n_(111617, "result_perms", lambda: result_perms):
            _l_(111635)

            for i in _c_(111622, _n_(111618, "range", lambda: range), _c_(111621, _n_(111619, "len", lambda: len), _n_(111620, "perm", lambda: perm)) + 1):
                _l_(111634)

                _c_(111630, _a_(111624, _n_(111623, "new_perms", lambda: new_perms), "append"), _n_(111625, "perm", lambda: perm)[:_n_(111626, "i", lambda: i)] + [_n_(111627, "n", lambda: n)] + _n_(111628, "perm", lambda: perm)[_n_(111629, "i", lambda: i):])
                _l_(111631)
                result_perms = _n_(111632, "new_perms", lambda: new_perms)
                _l_(111633)
    aux = _n_(111637, "result_perms", lambda: result_perms)
    _l_(111638)
    return aux
_c_(111642, _n_(111640, "print", lambda: print), 'Original Cofllection: ', _n_(111641, "my_nums", lambda: my_nums))
_l_(111643)
_c_(111648, _n_(111644, "print", lambda: print), 'Collection of distinct numbers:\n', _c_(111647, _n_(111645, "permute", lambda: permute), _n_(111646, "my_nums", lambda: my_nums)))
_l_(111649)