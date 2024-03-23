# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(51084)

except ImportError:
    pass

def find_sub_string(str):
    _l_(51142)

    str_len = _c_(51087, _n_(51085, "len", lambda: len), _n_(51086, "str", lambda: str))
    _l_(51088)
    dist_count_char = _c_(51094, _n_(51089, "len", lambda: len), _c_(51093, _n_(51090, "set", lambda: set), [_n_(51091, "x", lambda: x) for x in _n_(51092, "str", lambda: str)]))
    _l_(51095)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(51096)
    curr_count = _c_(51098, _n_(51097, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(51099)
    for i in _c_(51102, _n_(51100, "range", lambda: range), _n_(51101, "str_len", lambda: str_len)):
        _l_(51136)

        _n_(51103, "curr_count", lambda: curr_count)[_n_(51104, "str", lambda: str)[_n_(51105, "i", lambda: i)]] += 1
        _l_(51106)
        if _n_(51107, "curr_count", lambda: curr_count)[_n_(51108, "str", lambda: str)[_n_(51109, "i", lambda: i)]] == 1:
            _l_(51111)

            ctr += 1
            _l_(51110)
        if _n_(51112, "ctr", lambda: ctr) == _n_(51113, "dist_count_char", lambda: dist_count_char):
            _l_(51135)

            while _n_(51114, "curr_count", lambda: curr_count)[_n_(51115, "str", lambda: str)[_n_(51116, "start_pos", lambda: start_pos)]] > 1:
                _l_(51126)

                if _n_(51117, "curr_count", lambda: curr_count)[_n_(51118, "str", lambda: str)[_n_(51119, "start_pos", lambda: start_pos)]] > 1:
                    _l_(51124)

                    _n_(51120, "curr_count", lambda: curr_count)[_n_(51121, "str", lambda: str)[_n_(51122, "start_pos", lambda: start_pos)]] -= 1
                    _l_(51123)
                start_pos += 1
                _l_(51125)
            len_window = _n_(51127, "i", lambda: i) - _n_(51128, "start_pos", lambda: start_pos) + 1
            _l_(51129)
            if _n_(51130, "min_len", lambda: min_len) > _n_(51131, "len_window", lambda: len_window):
                _l_(51134)

                start_pos_index = _n_(51132, "start_pos", lambda: start_pos)
                _l_(51133)
    aux = _n_(51137, "str", lambda: str)[_n_(51138, "start_pos_index", lambda: start_pos_index):_n_(51139, "start_pos_index", lambda: start_pos_index) + _n_(51140, "min_len", lambda: min_len)]
    _l_(51141)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(51143)
_c_(51146, _n_(51144, "print", lambda: print), 'Original Strings:\n', _n_(51145, "str1", lambda: str1))
_l_(51147)
_c_(51149, _n_(51148, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(51150)
_c_(51155, _n_(51151, "print", lambda: print), _c_(51154, _n_(51152, "find_sub_string", lambda: find_sub_string), _n_(51153, "str1", lambda: str1)))
_l_(51156)