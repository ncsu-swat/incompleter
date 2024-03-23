# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(50793)

except ImportError:
    pass

def find_sub_string(str):
    _l_(50851)

    str_len = _c_(50796, _n_(50794, "len", lambda: len), _n_(50795, "str", lambda: str))
    _l_(50797)
    dist_count_char = _c_(50803, _n_(50798, "len", lambda: len), _c_(50802, _n_(50799, "set", lambda: set), [_n_(50800, "x", lambda: x) for x in _n_(50801, "str", lambda: str)]))
    _l_(50804)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(50805)
    curr_count = _c_(50807, _n_(50806, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(50808)
    for i in _c_(50811, _n_(50809, "range", lambda: range), _n_(50810, "str_len", lambda: str_len)):
        _l_(50845)

        _n_(50812, "curr_count", lambda: curr_count)[_n_(50813, "str", lambda: str)[_n_(50814, "i", lambda: i)]] += 1
        _l_(50815)
        if _n_(50816, "curr_count", lambda: curr_count)[_n_(50817, "str", lambda: str)[_n_(50818, "i", lambda: i)]] == 1:
            _l_(50820)

            ctr += 1
            _l_(50819)
        if _n_(50821, "ctr", lambda: ctr) == _n_(50822, "dist_count_char", lambda: dist_count_char):
            _l_(50844)

            while _n_(50823, "curr_count", lambda: curr_count)[_n_(50824, "str", lambda: str)[_n_(50825, "start_pos", lambda: start_pos)]] > 1:
                _l_(50835)

                if _n_(50826, "curr_count", lambda: curr_count)[_n_(50827, "str", lambda: str)[_n_(50828, "start_pos", lambda: start_pos)]] > 1:
                    _l_(50833)

                    _n_(50829, "curr_count", lambda: curr_count)[_n_(50830, "str", lambda: str)[_n_(50831, "start_pos", lambda: start_pos)]] -= 1
                    _l_(50832)
                start_pos += 1
                _l_(50834)
            len_window = _n_(50836, "i", lambda: i) - _n_(50837, "start_pos", lambda: start_pos) + 1
            _l_(50838)
            if _n_(50839, "min_len", lambda: min_len) > _n_(50840, "len_window", lambda: len_window):
                _l_(50843)

                min_len = _n_(50841, "len_window", lambda: len_window)
                _l_(50842)
    aux = _n_(50846, "str", lambda: str)[_n_(50847, "start_pos_index", lambda: start_pos_index):_n_(50848, "start_pos_index", lambda: start_pos_index) + _n_(50849, "min_len", lambda: min_len)]
    _l_(50850)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(50852)
_c_(50855, _n_(50853, "print", lambda: print), 'Original Strings:\n', _n_(50854, "str1", lambda: str1))
_l_(50856)
_c_(50858, _n_(50857, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(50859)
_c_(50864, _n_(50860, "print", lambda: print), _c_(50863, _n_(50861, "find_sub_string", lambda: find_sub_string), _n_(50862, "str1", lambda: str1)))
_l_(50865)