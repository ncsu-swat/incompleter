# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(51158)

except ImportError:
    pass

def find_sub_string(str):
    _l_(51215)

    str_len = _c_(51161, _n_(51159, "len", lambda: len), _n_(51160, "str", lambda: str))
    _l_(51162)
    dist_count_char = _c_(51168, _n_(51163, "len", lambda: len), _c_(51167, _n_(51164, "set", lambda: set), [_n_(51165, "x", lambda: x) for x in _n_(51166, "str", lambda: str)]))
    _l_(51169)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(51170)
    for i in _c_(51173, _n_(51171, "range", lambda: range), _n_(51172, "str_len", lambda: str_len)):
        _l_(51209)

        _n_(51174, "curr_count", lambda: curr_count)[_n_(51175, "str", lambda: str)[_n_(51176, "i", lambda: i)]] += 1
        _l_(51177)
        if _n_(51178, "curr_count", lambda: curr_count)[_n_(51179, "str", lambda: str)[_n_(51180, "i", lambda: i)]] == 1:
            _l_(51182)

            ctr += 1
            _l_(51181)
        if _n_(51183, "ctr", lambda: ctr) == _n_(51184, "dist_count_char", lambda: dist_count_char):
            _l_(51208)

            while _n_(51185, "curr_count", lambda: curr_count)[_n_(51186, "str", lambda: str)[_n_(51187, "start_pos", lambda: start_pos)]] > 1:
                _l_(51197)

                if _n_(51188, "curr_count", lambda: curr_count)[_n_(51189, "str", lambda: str)[_n_(51190, "start_pos", lambda: start_pos)]] > 1:
                    _l_(51195)

                    _n_(51191, "curr_count", lambda: curr_count)[_n_(51192, "str", lambda: str)[_n_(51193, "start_pos", lambda: start_pos)]] -= 1
                    _l_(51194)
                start_pos += 1
                _l_(51196)
            len_window = _n_(51198, "i", lambda: i) - _n_(51199, "start_pos", lambda: start_pos) + 1
            _l_(51200)
            if _n_(51201, "min_len", lambda: min_len) > _n_(51202, "len_window", lambda: len_window):
                _l_(51207)

                min_len = _n_(51203, "len_window", lambda: len_window)
                _l_(51204)
                start_pos_index = _n_(51205, "start_pos", lambda: start_pos)
                _l_(51206)
    aux = _n_(51210, "str", lambda: str)[_n_(51211, "start_pos_index", lambda: start_pos_index):_n_(51212, "start_pos_index", lambda: start_pos_index) + _n_(51213, "min_len", lambda: min_len)]
    _l_(51214)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(51216)
_c_(51219, _n_(51217, "print", lambda: print), 'Original Strings:\n', _n_(51218, "str1", lambda: str1))
_l_(51220)
_c_(51222, _n_(51221, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(51223)
_c_(51228, _n_(51224, "print", lambda: print), _c_(51227, _n_(51225, "find_sub_string", lambda: find_sub_string), _n_(51226, "str1", lambda: str1)))
_l_(51229)