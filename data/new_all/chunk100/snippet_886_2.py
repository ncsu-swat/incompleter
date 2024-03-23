# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as clt
    _l_(86957)

except ImportError:
    pass

def check_break_list(nums, n):
    _l_(86983)

    for x in _c_(86962, _n_(86958, "sorted", lambda: sorted), _c_(86961, _a_(86960, _n_(86959, "coll_data", lambda: coll_data), "keys"))):
        _l_(86981)

        for index in _c_(86965, _n_(86963, "range", lambda: range), 1, _n_(86964, "n", lambda: n)):
            _l_(86980)

            _n_(86966, "coll_data", lambda: coll_data)[_n_(86967, "x", lambda: x) + _n_(86968, "index", lambda: index)] = _n_(86969, "coll_data", lambda: coll_data)[_n_(86970, "x", lambda: x) + _n_(86971, "index", lambda: index)] - _n_(86972, "coll_data", lambda: coll_data)[_n_(86973, "x", lambda: x)]
            _l_(86974)
            if _n_(86975, "coll_data", lambda: coll_data)[_n_(86976, "x", lambda: x) + _n_(86977, "index", lambda: index)] < 0:
                _l_(86979)

                aux = False
                _l_(86978)
                return aux
    aux = True
    _l_(86982)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(86984)
n = 4
_l_(86985)
_c_(86988, _n_(86986, "print", lambda: print), 'Original list:', _n_(86987, "nums", lambda: nums))
_l_(86989)
_c_(86992, _n_(86990, "print", lambda: print), 'Number to devide the said list:', _n_(86991, "n", lambda: n))
_l_(86993)
_c_(86999, _n_(86994, "print", lambda: print), _c_(86998, _n_(86995, "check_break_list", lambda: check_break_list), _n_(86996, "nums", lambda: nums), _n_(86997, "n", lambda: n)))
_l_(87000)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(87001)
n = 3
_l_(87002)
_c_(87005, _n_(87003, "print", lambda: print), '\nOriginal list:', _n_(87004, "nums", lambda: nums))
_l_(87006)
_c_(87009, _n_(87007, "print", lambda: print), 'Number to devide the said list:', _n_(87008, "n", lambda: n))
_l_(87010)
_c_(87016, _n_(87011, "print", lambda: print), _c_(87015, _n_(87012, "check_break_list", lambda: check_break_list), _n_(87013, "nums", lambda: nums), _n_(87014, "n", lambda: n)))
_l_(87017)