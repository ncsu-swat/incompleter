# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_dups(nums):
    _l_(114184)

    element = []
    _l_(114139)
    freque = []
    _l_(114140)
    if not _n_(114141, "nums", lambda: nums):
        _l_(114144)

        aux = _n_(114142, "element", lambda: element)
        _l_(114143)
        return aux
    running_count = 1
    _l_(114145)
    for i in _c_(114150, _n_(114146, "range", lambda: range), _c_(114149, _n_(114147, "len", lambda: len), _n_(114148, "nums", lambda: nums)) - 1):
        _l_(114169)

        if _n_(114151, "nums", lambda: nums)[_n_(114152, "i", lambda: i)] == _n_(114153, "nums", lambda: nums)[_n_(114154, "i", lambda: i) + 1]:
            _l_(114168)

            running_count += 1
            _l_(114155)
        else:
            _c_(114159, _a_(114157, _n_(114156, "freque", lambda: freque), "append"), _n_(114158, "running_count", lambda: running_count))
            _l_(114160)
            _c_(114165, _a_(114162, _n_(114161, "element", lambda: element), "append"), _n_(114163, "nums", lambda: nums)[_n_(114164, "i", lambda: i)])
            _l_(114166)
            running_count = 1
            _l_(114167)
    _c_(114173, _a_(114171, _n_(114170, "freque", lambda: freque), "append"), _n_(114172, "running_count", lambda: running_count))
    _l_(114174)
    _c_(114179, _a_(114176, _n_(114175, "element", lambda: element), "append"), _n_(114177, "nums", lambda: nums)[_n_(114178, "i", lambda: i) + 1])
    _l_(114180)
    aux = (_n_(114181, "element", lambda: element), _n_(114182, "freque", lambda: freque))
    _l_(114183)
    return aux
_c_(114186, _n_(114185, "print", lambda: print), 'Original lists:')
_l_(114187)
_c_(114190, _n_(114188, "print", lambda: print), _n_(114189, "nums", lambda: nums))
_l_(114191)
_c_(114193, _n_(114192, "print", lambda: print), '\nConsecutive duplicate elements and their frequency:')
_l_(114194)
_c_(114199, _n_(114195, "print", lambda: print), _c_(114198, _n_(114196, "count_dups", lambda: count_dups), _n_(114197, "nums", lambda: nums)))
_l_(114200)