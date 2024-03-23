# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(51015)

except ImportError:
    pass

def find_sub_string(str):
    _l_(51068)

    str_len = _c_(51018, _n_(51016, "len", lambda: len), _n_(51017, "str", lambda: str))
    _l_(51019)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(51020)
    curr_count = _c_(51022, _n_(51021, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(51023)
    for i in _c_(51026, _n_(51024, "range", lambda: range), _n_(51025, "str_len", lambda: str_len)):
        _l_(51062)

        _n_(51027, "curr_count", lambda: curr_count)[_n_(51028, "str", lambda: str)[_n_(51029, "i", lambda: i)]] += 1
        _l_(51030)
        if _n_(51031, "curr_count", lambda: curr_count)[_n_(51032, "str", lambda: str)[_n_(51033, "i", lambda: i)]] == 1:
            _l_(51035)

            ctr += 1
            _l_(51034)
        if _n_(51036, "ctr", lambda: ctr) == _n_(51037, "dist_count_char", lambda: dist_count_char):
            _l_(51061)

            while _n_(51038, "curr_count", lambda: curr_count)[_n_(51039, "str", lambda: str)[_n_(51040, "start_pos", lambda: start_pos)]] > 1:
                _l_(51050)

                if _n_(51041, "curr_count", lambda: curr_count)[_n_(51042, "str", lambda: str)[_n_(51043, "start_pos", lambda: start_pos)]] > 1:
                    _l_(51048)

                    _n_(51044, "curr_count", lambda: curr_count)[_n_(51045, "str", lambda: str)[_n_(51046, "start_pos", lambda: start_pos)]] -= 1
                    _l_(51047)
                start_pos += 1
                _l_(51049)
            len_window = _n_(51051, "i", lambda: i) - _n_(51052, "start_pos", lambda: start_pos) + 1
            _l_(51053)
            if _n_(51054, "min_len", lambda: min_len) > _n_(51055, "len_window", lambda: len_window):
                _l_(51060)

                min_len = _n_(51056, "len_window", lambda: len_window)
                _l_(51057)
                start_pos_index = _n_(51058, "start_pos", lambda: start_pos)
                _l_(51059)
    aux = _n_(51063, "str", lambda: str)[_n_(51064, "start_pos_index", lambda: start_pos_index):_n_(51065, "start_pos_index", lambda: start_pos_index) + _n_(51066, "min_len", lambda: min_len)]
    _l_(51067)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(51069)
_c_(51072, _n_(51070, "print", lambda: print), 'Original Strings:\n', _n_(51071, "str1", lambda: str1))
_l_(51073)
_c_(51075, _n_(51074, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(51076)
_c_(51081, _n_(51077, "print", lambda: print), _c_(51080, _n_(51078, "find_sub_string", lambda: find_sub_string), _n_(51079, "str1", lambda: str1)))
_l_(51082)