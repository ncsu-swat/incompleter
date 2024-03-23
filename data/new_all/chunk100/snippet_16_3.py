# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_last_n(nums, N):
    _l_(11975)

    result = _n_(11967, "nums", lambda: nums)[:_c_(11970, _n_(11968, "len", lambda: len), _n_(11969, "nums", lambda: nums)) - _n_(11971, "N", lambda: N)]
    _l_(11972)
    aux = _n_(11973, "result", lambda: result)
    _l_(11974)
    return aux
_c_(11977, _n_(11976, "print", lambda: print), 'Original lists:')
_l_(11978)
_c_(11981, _n_(11979, "print", lambda: print), _n_(11980, "nums", lambda: nums))
_l_(11982)
N = 3
_l_(11983)
_c_(11986, _n_(11984, "print", lambda: print), '\nRemove the last', _n_(11985, "N", lambda: N), 'elements from the said list:')
_l_(11987)
_c_(11993, _n_(11988, "print", lambda: print), _c_(11992, _n_(11989, "remove_last_n", lambda: remove_last_n), _n_(11990, "nums", lambda: nums), _n_(11991, "N", lambda: N)))
_l_(11994)
N = 5
_l_(11995)
_c_(11998, _n_(11996, "print", lambda: print), '\nRemove the last', _n_(11997, "N", lambda: N), 'elements from the said list:')
_l_(11999)
_c_(12005, _n_(12000, "print", lambda: print), _c_(12004, _n_(12001, "remove_last_n", lambda: remove_last_n), _n_(12002, "nums", lambda: nums), _n_(12003, "N", lambda: N)))
_l_(12006)
N = 1
_l_(12007)
_c_(12010, _n_(12008, "print", lambda: print), '\nRemove the last', _n_(12009, "N", lambda: N), 'element from the said list:')
_l_(12011)
_c_(12017, _n_(12012, "print", lambda: print), _c_(12016, _n_(12013, "remove_last_n", lambda: remove_last_n), _n_(12014, "nums", lambda: nums), _n_(12015, "N", lambda: N)))
_l_(12018)