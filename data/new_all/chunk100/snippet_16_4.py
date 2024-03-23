# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_last_n(nums, N):
    _l_(12027)

    result = _n_(12019, "nums", lambda: nums)[:_c_(12022, _n_(12020, "len", lambda: len), _n_(12021, "nums", lambda: nums)) - _n_(12023, "N", lambda: N)]
    _l_(12024)
    aux = _n_(12025, "result", lambda: result)
    _l_(12026)
    return aux
nums = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
_l_(12028)
_c_(12030, _n_(12029, "print", lambda: print), 'Original lists:')
_l_(12031)
_c_(12034, _n_(12032, "print", lambda: print), _n_(12033, "nums", lambda: nums))
_l_(12035)
N = 3
_l_(12036)
_c_(12039, _n_(12037, "print", lambda: print), '\nRemove the last', _n_(12038, "N", lambda: N), 'elements from the said list:')
_l_(12040)
_c_(12046, _n_(12041, "print", lambda: print), _c_(12045, _n_(12042, "remove_last_n", lambda: remove_last_n), _n_(12043, "nums", lambda: nums), _n_(12044, "N", lambda: N)))
_l_(12047)
N = 5
_l_(12048)
_c_(12051, _n_(12049, "print", lambda: print), '\nRemove the last', _n_(12050, "N", lambda: N), 'elements from the said list:')
_l_(12052)
_c_(12058, _n_(12053, "print", lambda: print), _c_(12057, _n_(12054, "remove_last_n", lambda: remove_last_n), _n_(12055, "nums", lambda: nums), _n_(12056, "N", lambda: N)))
_l_(12059)
_c_(12062, _n_(12060, "print", lambda: print), '\nRemove the last', _n_(12061, "N", lambda: N), 'element from the said list:')
_l_(12063)
_c_(12069, _n_(12064, "print", lambda: print), _c_(12068, _n_(12065, "remove_last_n", lambda: remove_last_n), _n_(12066, "nums", lambda: nums), _n_(12067, "N", lambda: N)))
_l_(12070)