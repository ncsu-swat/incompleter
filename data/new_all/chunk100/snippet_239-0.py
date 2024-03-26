# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(106439)

    if _n_(106416, "n", lambda: n) <= 0:
        _l_(106419)

        yield []
        _l_(106417)
        aux = ""
        _l_(106418)
        return aux
    for i in _c_(106424, _n_(106420, "range", lambda: range), _c_(106423, _n_(106421, "len", lambda: len), _n_(106422, "n_list", lambda: n_list))):
        _l_(106438)

        c_num = _n_(106425, "n_list", lambda: n_list)[_n_(106426, "i", lambda: i):_n_(106427, "i", lambda: i) + 1]
        _l_(106428)
        for a_num in _c_(106433, _n_(106429, "combination", lambda: combination), _n_(106430, "n", lambda: n) - 1, _n_(106431, "n_list", lambda: n_list)[_n_(106432, "i", lambda: i) + 1:]):
            _l_(106437)

            yield (_n_(106434, "c_num", lambda: c_num) + _n_(106435, "a_num", lambda: a_num))
            _l_(106436)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_l_(106440)
_c_(106442, _n_(106441, "print", lambda: print), 'Original list:')
_l_(106443)
_c_(106446, _n_(106444, "print", lambda: print), _n_(106445, "n_list", lambda: n_list))
_l_(106447)
n = 2
_l_(106448)
_c_(106451, _n_(106449, "print", lambda: print), '\nCombinations of', _n_(106450, "n", lambda: n), 'distinct objects:')
_l_(106452)
for e in _n_(106453, "result", lambda: result):
    _l_(106458)

    _c_(106456, _n_(106454, "print", lambda: print), _n_(106455, "e", lambda: e))
    _l_(106457)