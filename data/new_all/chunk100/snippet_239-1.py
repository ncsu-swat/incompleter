# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(106482)

    if _n_(106459, "n", lambda: n) <= 0:
        _l_(106462)

        yield []
        _l_(106460)
        aux = ""
        _l_(106461)
        return aux
    for i in _c_(106467, _n_(106463, "range", lambda: range), _c_(106466, _n_(106464, "len", lambda: len), _n_(106465, "n_list", lambda: n_list))):
        _l_(106481)

        c_num = _n_(106468, "n_list", lambda: n_list)[_n_(106469, "i", lambda: i):_n_(106470, "i", lambda: i) + 1]
        _l_(106471)
        for a_num in _c_(106476, _n_(106472, "combination", lambda: combination), _n_(106473, "n", lambda: n) - 1, _n_(106474, "n_list", lambda: n_list)[_n_(106475, "i", lambda: i) + 1:]):
            _l_(106480)

            yield (_n_(106477, "c_num", lambda: c_num) + _n_(106478, "a_num", lambda: a_num))
            _l_(106479)
_c_(106484, _n_(106483, "print", lambda: print), 'Original list:')
_l_(106485)
_c_(106488, _n_(106486, "print", lambda: print), _n_(106487, "n_list", lambda: n_list))
_l_(106489)
n = 2
_l_(106490)
result = _c_(106494, _n_(106491, "combination", lambda: combination), _n_(106492, "n", lambda: n), _n_(106493, "n_list", lambda: n_list))
_l_(106495)
_c_(106498, _n_(106496, "print", lambda: print), '\nCombinations of', _n_(106497, "n", lambda: n), 'distinct objects:')
_l_(106499)
for e in _n_(106500, "result", lambda: result):
    _l_(106505)

    _c_(106503, _n_(106501, "print", lambda: print), _n_(106502, "e", lambda: e))
    _l_(106504)