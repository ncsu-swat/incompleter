# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(118247)

except ImportError:
    pass

def find_sub_string(str):
    _l_(118307)

    str_len = _c_(118250, _n_(118248, "len", lambda: len), _n_(118249, "str", lambda: str))
    _l_(118251)
    dist_count_char = _c_(118257, _n_(118252, "len", lambda: len), _c_(118256, _n_(118253, "set", lambda: set), [_n_(118254, "x", lambda: x) for x in _n_(118255, "str", lambda: str)]))
    _l_(118258)
    ctr, start_pos, start_pos_index, min_len = (0, 0, -1, 9999999999)
    _l_(118259)
    curr_count = _c_(118261, _n_(118260, "defaultdict", lambda: defaultdict), lambda: 0)
    _l_(118262)
    for i in _c_(118265, _n_(118263, "range", lambda: range), _n_(118264, "str_len", lambda: str_len)):
        _l_(118301)

        _n_(118266, "curr_count", lambda: curr_count)[_n_(118267, "str", lambda: str)[_n_(118268, "i", lambda: i)]] += 1
        _l_(118269)
        if _n_(118270, "curr_count", lambda: curr_count)[_n_(118271, "str", lambda: str)[_n_(118272, "i", lambda: i)]] == 1:
            _l_(118274)

            ctr += 1
            _l_(118273)
        if _n_(118275, "ctr", lambda: ctr) == _n_(118276, "dist_count_char", lambda: dist_count_char):
            _l_(118300)

            while _n_(118277, "curr_count", lambda: curr_count)[_n_(118278, "str", lambda: str)[_n_(118279, "start_pos", lambda: start_pos)]] > 1:
                _l_(118289)

                if _n_(118280, "curr_count", lambda: curr_count)[_n_(118281, "str", lambda: str)[_n_(118282, "start_pos", lambda: start_pos)]] > 1:
                    _l_(118287)

                    _n_(118283, "curr_count", lambda: curr_count)[_n_(118284, "str", lambda: str)[_n_(118285, "start_pos", lambda: start_pos)]] -= 1
                    _l_(118286)
                start_pos += 1
                _l_(118288)
            len_window = _n_(118290, "i", lambda: i) - _n_(118291, "start_pos", lambda: start_pos) + 1
            _l_(118292)
            if _n_(118293, "min_len", lambda: min_len) > _n_(118294, "len_window", lambda: len_window):
                _l_(118299)

                min_len = _n_(118295, "len_window", lambda: len_window)
                _l_(118296)
                start_pos_index = _n_(118297, "start_pos", lambda: start_pos)
                _l_(118298)
    aux = _n_(118302, "str", lambda: str)[_n_(118303, "start_pos_index", lambda: start_pos_index):_n_(118304, "start_pos_index", lambda: start_pos_index) + _n_(118305, "min_len", lambda: min_len)]
    _l_(118306)
    return aux
_c_(118310, _n_(118308, "print", lambda: print), 'Original Strings:\n', _n_(118309, "str1", lambda: str1))
_l_(118311)
_c_(118313, _n_(118312, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(118314)
_c_(118319, _n_(118315, "print", lambda: print), _c_(118318, _n_(118316, "find_sub_string", lambda: find_sub_string), _n_(118317, "str1", lambda: str1)))
_l_(118320)