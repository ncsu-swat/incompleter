# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(19019)

    if _n_(18996, "n", lambda: n) <= 0:
        _l_(18999)

        yield []
        _l_(18997)
        aux = ""
        _l_(18998)
        return aux
    for i in _c_(19004, _n_(19000, "range", lambda: range), _c_(19003, _n_(19001, "len", lambda: len), _n_(19002, "n_list", lambda: n_list))):
        _l_(19018)

        c_num = _n_(19005, "n_list", lambda: n_list)[_n_(19006, "i", lambda: i):_n_(19007, "i", lambda: i) + 1]
        _l_(19008)
        for a_num in _c_(19013, _n_(19009, "combination", lambda: combination), _n_(19010, "n", lambda: n) - 1, _n_(19011, "n_list", lambda: n_list)[_n_(19012, "i", lambda: i) + 1:]):
            _l_(19017)

            yield (_n_(19014, "c_num", lambda: c_num) + _n_(19015, "a_num", lambda: a_num))
            _l_(19016)
_c_(19021, _n_(19020, "print", lambda: print), 'Original list:')
_l_(19022)
_c_(19025, _n_(19023, "print", lambda: print), _n_(19024, "n_list", lambda: n_list))
_l_(19026)
n = 2
_l_(19027)
result = _c_(19031, _n_(19028, "combination", lambda: combination), _n_(19029, "n", lambda: n), _n_(19030, "n_list", lambda: n_list))
_l_(19032)
_c_(19035, _n_(19033, "print", lambda: print), '\nCombinations of', _n_(19034, "n", lambda: n), 'distinct objects:')
_l_(19036)
for e in _n_(19037, "result", lambda: result):
    _l_(19042)

    _c_(19040, _n_(19038, "print", lambda: print), _n_(19039, "e", lambda: e))
    _l_(19041)