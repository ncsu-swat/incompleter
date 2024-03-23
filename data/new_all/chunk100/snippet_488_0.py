# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(50721)

except ImportError:
    pass

def find_sub_string(str):
    _l_(50777)

    dist_count_char = _c_(50727, _n_(50722, "len", lambda: len), _c_(50726, _n_(50723, "set", lambda: set), [_n_(50724, "x", lambda: x) for x in _n_(50725, "str", lambda: str)]))
    _l_(50728)
    (ctr, start_pos, start_pos_index, min_len) = (0, 0, -1, 9999999999)
    _l_(50729)
    curr_count = _c_(50731, _n_(50730, "defaultdict", lambda: defaultdict), lambda : 0)
    _l_(50732)
    for i in _c_(50735, _n_(50733, "range", lambda: range), _n_(50734, "str_len", lambda: str_len)):
        _l_(50771)

        _n_(50736, "curr_count", lambda: curr_count)[_n_(50737, "str", lambda: str)[_n_(50738, "i", lambda: i)]] += 1
        _l_(50739)
        if _n_(50740, "curr_count", lambda: curr_count)[_n_(50741, "str", lambda: str)[_n_(50742, "i", lambda: i)]] == 1:
            _l_(50744)

            ctr += 1
            _l_(50743)
        if _n_(50745, "ctr", lambda: ctr) == _n_(50746, "dist_count_char", lambda: dist_count_char):
            _l_(50770)

            while _n_(50747, "curr_count", lambda: curr_count)[_n_(50748, "str", lambda: str)[_n_(50749, "start_pos", lambda: start_pos)]] > 1:
                _l_(50759)

                if _n_(50750, "curr_count", lambda: curr_count)[_n_(50751, "str", lambda: str)[_n_(50752, "start_pos", lambda: start_pos)]] > 1:
                    _l_(50757)

                    _n_(50753, "curr_count", lambda: curr_count)[_n_(50754, "str", lambda: str)[_n_(50755, "start_pos", lambda: start_pos)]] -= 1
                    _l_(50756)
                start_pos += 1
                _l_(50758)
            len_window = _n_(50760, "i", lambda: i) - _n_(50761, "start_pos", lambda: start_pos) + 1
            _l_(50762)
            if _n_(50763, "min_len", lambda: min_len) > _n_(50764, "len_window", lambda: len_window):
                _l_(50769)

                min_len = _n_(50765, "len_window", lambda: len_window)
                _l_(50766)
                start_pos_index = _n_(50767, "start_pos", lambda: start_pos)
                _l_(50768)
    aux = _n_(50772, "str", lambda: str)[_n_(50773, "start_pos_index", lambda: start_pos_index):_n_(50774, "start_pos_index", lambda: start_pos_index) + _n_(50775, "min_len", lambda: min_len)]
    _l_(50776)
    return aux
str1 = 'asdaewsqgtwwsa'
_l_(50778)
_c_(50781, _n_(50779, "print", lambda: print), 'Original Strings:\n', _n_(50780, "str1", lambda: str1))
_l_(50782)
_c_(50784, _n_(50783, "print", lambda: print), '\nSmallest window that contains all characters of the said string:')
_l_(50785)
_c_(50790, _n_(50786, "print", lambda: print), _c_(50789, _n_(50787, "find_sub_string", lambda: find_sub_string), _n_(50788, "str1", lambda: str1)))
_l_(50791)