# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_dups(nums):
    _l_(39002)

    freque = []
    _l_(38958)
    if not _n_(38959, "nums", lambda: nums):
        _l_(38962)

        aux = _n_(38960, "element", lambda: element)
        _l_(38961)
        return aux
    running_count = 1
    _l_(38963)
    for i in _c_(38968, _n_(38964, "range", lambda: range), _c_(38967, _n_(38965, "len", lambda: len), _n_(38966, "nums", lambda: nums)) - 1):
        _l_(38987)

        if _n_(38969, "nums", lambda: nums)[_n_(38970, "i", lambda: i)] == _n_(38971, "nums", lambda: nums)[_n_(38972, "i", lambda: i) + 1]:
            _l_(38986)

            running_count += 1
            _l_(38973)
        else:
            _c_(38977, _a_(38975, _n_(38974, "freque", lambda: freque), "append"), _n_(38976, "running_count", lambda: running_count))
            _l_(38978)
            _c_(38983, _a_(38980, _n_(38979, "element", lambda: element), "append"), _n_(38981, "nums", lambda: nums)[_n_(38982, "i", lambda: i)])
            _l_(38984)
            running_count = 1
            _l_(38985)
    _c_(38991, _a_(38989, _n_(38988, "freque", lambda: freque), "append"), _n_(38990, "running_count", lambda: running_count))
    _l_(38992)
    _c_(38997, _a_(38994, _n_(38993, "element", lambda: element), "append"), _n_(38995, "nums", lambda: nums)[_n_(38996, "i", lambda: i) + 1])
    _l_(38998)
    aux = (_n_(38999, "element", lambda: element), _n_(39000, "freque", lambda: freque))
    _l_(39001)
    return aux
nums = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
_l_(39003)
_c_(39005, _n_(39004, "print", lambda: print), 'Original lists:')
_l_(39006)
_c_(39009, _n_(39007, "print", lambda: print), _n_(39008, "nums", lambda: nums))
_l_(39010)
_c_(39012, _n_(39011, "print", lambda: print), '\nConsecutive duplicate elements and their frequency:')
_l_(39013)
_c_(39018, _n_(39014, "print", lambda: print), _c_(39017, _n_(39015, "count_dups", lambda: count_dups), _n_(39016, "nums", lambda: nums)))
_l_(39019)