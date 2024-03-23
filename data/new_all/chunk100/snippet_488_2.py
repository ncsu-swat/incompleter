# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(50867)

except ImportError:
    pass

def find_sub_string(str):
    _l_(50927)

    str_len = _c_(50870, _n_(50868, "len", lambda: len), _n_(50869, "str", lambda: str))
    _l_(50871)
    dist_count_char = _c_(50877, _n_(50872, "len", lambda: len), _c_(50876, _n_(50873, "set", lambda: set), [_n_(50874, "x", lambda: x) for x in _n_(50875, "str", lambda: str)]))
    _l_(50878)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(50879)
    curr_count = _c_(50881, _n_(50880, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(50882)
    for i in _c_(50885, _n_(50883, "range", lambda: range), _n_(50884, "str_len", lambda: str_len)):
        _l_(50921)

        _n_(50886, "curr_count", lambda: curr_count)[_n_(50887, "str", lambda: str)[_n_(50888, "i", lambda: i)]] += 1
        _l_(50889)
        if _n_(50890, "curr_count", lambda: curr_count)[_n_(50891, "str", lambda: str)[_n_(50892, "i", lambda: i)]] == 1:
            _l_(50894)

            ctr += 1
            _l_(50893)
        if _n_(50895, "ctr", lambda: ctr) == _n_(50896, "dist_count_char", lambda: dist_count_char):
            _l_(50920)

            while _n_(50897, "curr_count", lambda: curr_count)[_n_(50898, "str", lambda: str)[_n_(50899, "start_pos", lambda: start_pos)]] > 1:
                _l_(50909)

                if _n_(50900, "curr_count", lambda: curr_count)[_n_(50901, "str", lambda: str)[_n_(50902, "start_pos", lambda: start_pos)]] > 1:
                    _l_(50907)

                    _n_(50903, "curr_count", lambda: curr_count)[_n_(50904, "str", lambda: str)[_n_(50905, "start_pos", lambda: start_pos)]] -= 1
                    _l_(50906)
                start_pos += 1
                _l_(50908)
            len_window = _n_(50910, "i", lambda: i) - _n_(50911, "start_pos", lambda: start_pos) + 1
            _l_(50912)
            if _n_(50913, "min_len", lambda: min_len) > _n_(50914, "len_window", lambda: len_window):
                _l_(50919)

                min_len = _n_(50915, "len_window", lambda: len_window)
                _l_(50916)
                start_pos_index = _n_(50917, "start_pos", lambda: start_pos)
                _l_(50918)
    aux = _n_(50922, "str", lambda: str)[_n_(50923, "start_pos_index", lambda: start_pos_index):_n_(50924, "start_pos_index", lambda: start_pos_index) + _n_(50925, "min_len", lambda: min_len)]
    _l_(50926)
    return aux
_c_(50930, _n_(50928, "print", lambda: print), 'Original Strings:\n', _n_(50929, "str1", lambda: str1))
_l_(50931)
_c_(50933, _n_(50932, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(50934)
_c_(50939, _n_(50935, "print", lambda: print), _c_(50938, _n_(50936, "find_sub_string", lambda: find_sub_string), _n_(50937, "str1", lambda: str1)))
_l_(50940)