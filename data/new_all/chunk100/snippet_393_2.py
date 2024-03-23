# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_dups(nums):
    _l_(39064)

    element = []
    _l_(39020)
    freque = []
    _l_(39021)
    if not _n_(39022, "nums", lambda: nums):
        _l_(39025)

        aux = _n_(39023, "element", lambda: element)
        _l_(39024)
        return aux
    for i in _c_(39030, _n_(39026, "range", lambda: range), _c_(39029, _n_(39027, "len", lambda: len), _n_(39028, "nums", lambda: nums)) - 1):
        _l_(39049)

        if _n_(39031, "nums", lambda: nums)[_n_(39032, "i", lambda: i)] == _n_(39033, "nums", lambda: nums)[_n_(39034, "i", lambda: i) + 1]:
            _l_(39048)

            running_count += 1
            _l_(39035)
        else:
            _c_(39039, _a_(39037, _n_(39036, "freque", lambda: freque), "append"), _n_(39038, "running_count", lambda: running_count))
            _l_(39040)
            _c_(39045, _a_(39042, _n_(39041, "element", lambda: element), "append"), _n_(39043, "nums", lambda: nums)[_n_(39044, "i", lambda: i)])
            _l_(39046)
            running_count = 1
            _l_(39047)
    _c_(39053, _a_(39051, _n_(39050, "freque", lambda: freque), "append"), _n_(39052, "running_count", lambda: running_count))
    _l_(39054)
    _c_(39059, _a_(39056, _n_(39055, "element", lambda: element), "append"), _n_(39057, "nums", lambda: nums)[_n_(39058, "i", lambda: i) + 1])
    _l_(39060)
    aux = (_n_(39061, "element", lambda: element), _n_(39062, "freque", lambda: freque))
    _l_(39063)
    return aux
nums = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
_l_(39065)
_c_(39067, _n_(39066, "print", lambda: print), 'Original lists:')
_l_(39068)
_c_(39071, _n_(39069, "print", lambda: print), _n_(39070, "nums", lambda: nums))
_l_(39072)
_c_(39074, _n_(39073, "print", lambda: print), '\nConsecutive duplicate elements and their frequency:')
_l_(39075)
_c_(39080, _n_(39076, "print", lambda: print), _c_(39079, _n_(39077, "count_dups", lambda: count_dups), _n_(39078, "nums", lambda: nums)))
_l_(39081)