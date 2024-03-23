# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_dups(nums):
    _l_(39126)

    element = []
    _l_(39082)
    if not _n_(39083, "nums", lambda: nums):
        _l_(39086)

        aux = _n_(39084, "element", lambda: element)
        _l_(39085)
        return aux
    running_count = 1
    _l_(39087)
    for i in _c_(39092, _n_(39088, "range", lambda: range), _c_(39091, _n_(39089, "len", lambda: len), _n_(39090, "nums", lambda: nums)) - 1):
        _l_(39111)

        if _n_(39093, "nums", lambda: nums)[_n_(39094, "i", lambda: i)] == _n_(39095, "nums", lambda: nums)[_n_(39096, "i", lambda: i) + 1]:
            _l_(39110)

            running_count += 1
            _l_(39097)
        else:
            _c_(39101, _a_(39099, _n_(39098, "freque", lambda: freque), "append"), _n_(39100, "running_count", lambda: running_count))
            _l_(39102)
            _c_(39107, _a_(39104, _n_(39103, "element", lambda: element), "append"), _n_(39105, "nums", lambda: nums)[_n_(39106, "i", lambda: i)])
            _l_(39108)
            running_count = 1
            _l_(39109)
    _c_(39115, _a_(39113, _n_(39112, "freque", lambda: freque), "append"), _n_(39114, "running_count", lambda: running_count))
    _l_(39116)
    _c_(39121, _a_(39118, _n_(39117, "element", lambda: element), "append"), _n_(39119, "nums", lambda: nums)[_n_(39120, "i", lambda: i) + 1])
    _l_(39122)
    aux = (_n_(39123, "element", lambda: element), _n_(39124, "freque", lambda: freque))
    _l_(39125)
    return aux
nums = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
_l_(39127)
_c_(39129, _n_(39128, "print", lambda: print), 'Original lists:')
_l_(39130)
_c_(39133, _n_(39131, "print", lambda: print), _n_(39132, "nums", lambda: nums))
_l_(39134)
_c_(39136, _n_(39135, "print", lambda: print), '\nConsecutive duplicate elements and their frequency:')
_l_(39137)
_c_(39142, _n_(39138, "print", lambda: print), _c_(39141, _n_(39139, "count_dups", lambda: count_dups), _n_(39140, "nums", lambda: nums)))
_l_(39143)