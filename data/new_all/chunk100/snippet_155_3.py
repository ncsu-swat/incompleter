# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(10527)

    aux = _n_(10525, "x", lambda: x) % 2 == 0
    _l_(10526)
    return aux

def remove_items_con(data, N):
    _l_(10546)

    result = []
    _l_(10528)
    for x in _n_(10529, "data", lambda: data):
        _l_(10543)

        if _n_(10530, "ctr", lambda: ctr) > _n_(10531, "N", lambda: N) or not _c_(10534, _n_(10532, "condition_match", lambda: condition_match), _n_(10533, "x", lambda: x)):
            _l_(10542)

            _c_(10538, _a_(10536, _n_(10535, "result", lambda: result), "append"), _n_(10537, "x", lambda: x))
            _l_(10539)
        else:
            ctr = _n_(10540, "ctr", lambda: ctr) + 1
            _l_(10541)
    aux = _n_(10544, "result", lambda: result)
    _l_(10545)
    return aux
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
_l_(10547)
N = 4
_l_(10548)
_c_(10550, _n_(10549, "print", lambda: print), 'Original list:')
_l_(10551)
_c_(10554, _n_(10552, "print", lambda: print), _n_(10553, "nums", lambda: nums))
_l_(10555)
_c_(10557, _n_(10556, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(10558)
_c_(10564, _n_(10559, "print", lambda: print), _c_(10563, _n_(10560, "remove_items_con", lambda: remove_items_con), _n_(10561, "nums", lambda: nums), _n_(10562, "N", lambda: N)))
_l_(10565)