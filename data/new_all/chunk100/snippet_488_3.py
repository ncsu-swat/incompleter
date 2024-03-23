# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(50942)

except ImportError:
    pass

def find_sub_string(str):
    _l_(50999)

    str_len = _c_(50945, _n_(50943, "len", lambda: len), _n_(50944, "str", lambda: str))
    _l_(50946)
    dist_count_char = _c_(50952, _n_(50947, "len", lambda: len), _c_(50951, _n_(50948, "set", lambda: set), [_n_(50949, "x", lambda: x) for x in _n_(50950, "str", lambda: str)]))
    _l_(50953)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(50954)
    curr_count = _c_(50956, _n_(50955, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(50957)
    for i in _c_(50960, _n_(50958, "range", lambda: range), _n_(50959, "str_len", lambda: str_len)):
        _l_(50993)

        _n_(50961, "curr_count", lambda: curr_count)[_n_(50962, "str", lambda: str)[_n_(50963, "i", lambda: i)]] += 1
        _l_(50964)
        if _n_(50965, "curr_count", lambda: curr_count)[_n_(50966, "str", lambda: str)[_n_(50967, "i", lambda: i)]] == 1:
            _l_(50969)

            ctr += 1
            _l_(50968)
        if _n_(50970, "ctr", lambda: ctr) == _n_(50971, "dist_count_char", lambda: dist_count_char):
            _l_(50992)

            while _n_(50972, "curr_count", lambda: curr_count)[_n_(50973, "str", lambda: str)[_n_(50974, "start_pos", lambda: start_pos)]] > 1:
                _l_(50984)

                if _n_(50975, "curr_count", lambda: curr_count)[_n_(50976, "str", lambda: str)[_n_(50977, "start_pos", lambda: start_pos)]] > 1:
                    _l_(50982)

                    _n_(50978, "curr_count", lambda: curr_count)[_n_(50979, "str", lambda: str)[_n_(50980, "start_pos", lambda: start_pos)]] -= 1
                    _l_(50981)
                start_pos += 1
                _l_(50983)
            if _n_(50985, "min_len", lambda: min_len) > _n_(50986, "len_window", lambda: len_window):
                _l_(50991)

                min_len = _n_(50987, "len_window", lambda: len_window)
                _l_(50988)
                start_pos_index = _n_(50989, "start_pos", lambda: start_pos)
                _l_(50990)
    aux = _n_(50994, "str", lambda: str)[_n_(50995, "start_pos_index", lambda: start_pos_index):_n_(50996, "start_pos_index", lambda: start_pos_index) + _n_(50997, "min_len", lambda: min_len)]
    _l_(50998)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(51000)
_c_(51003, _n_(51001, "print", lambda: print), 'Original Strings:\n', _n_(51002, "str1", lambda: str1))
_l_(51004)
_c_(51006, _n_(51005, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(51007)
_c_(51012, _n_(51008, "print", lambda: print), _c_(51011, _n_(51009, "find_sub_string", lambda: find_sub_string), _n_(51010, "str1", lambda: str1)))
_l_(51013)