# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_dups(nums):
    _l_(38941)

    element = []
    _l_(38896)
    freque = []
    _l_(38897)
    if not _n_(38898, "nums", lambda: nums):
        _l_(38901)

        aux = _n_(38899, "element", lambda: element)
        _l_(38900)
        return aux
    running_count = 1
    _l_(38902)
    for i in _c_(38907, _n_(38903, "range", lambda: range), _c_(38906, _n_(38904, "len", lambda: len), _n_(38905, "nums", lambda: nums)) - 1):
        _l_(38926)

        if _n_(38908, "nums", lambda: nums)[_n_(38909, "i", lambda: i)] == _n_(38910, "nums", lambda: nums)[_n_(38911, "i", lambda: i) + 1]:
            _l_(38925)

            running_count += 1
            _l_(38912)
        else:
            _c_(38916, _a_(38914, _n_(38913, "freque", lambda: freque), "append"), _n_(38915, "running_count", lambda: running_count))
            _l_(38917)
            _c_(38922, _a_(38919, _n_(38918, "element", lambda: element), "append"), _n_(38920, "nums", lambda: nums)[_n_(38921, "i", lambda: i)])
            _l_(38923)
            running_count = 1
            _l_(38924)
    _c_(38930, _a_(38928, _n_(38927, "freque", lambda: freque), "append"), _n_(38929, "running_count", lambda: running_count))
    _l_(38931)
    _c_(38936, _a_(38933, _n_(38932, "element", lambda: element), "append"), _n_(38934, "nums", lambda: nums)[_n_(38935, "i", lambda: i) + 1])
    _l_(38937)
    aux = (_n_(38938, "element", lambda: element), _n_(38939, "freque", lambda: freque))
    _l_(38940)
    return aux
_c_(38943, _n_(38942, "print", lambda: print), 'Original lists:')
_l_(38944)
_c_(38947, _n_(38945, "print", lambda: print), _n_(38946, "nums", lambda: nums))
_l_(38948)
_c_(38950, _n_(38949, "print", lambda: print), '\nConsecutive duplicate elements and their frequency:')
_l_(38951)
_c_(38956, _n_(38952, "print", lambda: print), _c_(38955, _n_(38953, "count_dups", lambda: count_dups), _n_(38954, "nums", lambda: nums)))
_l_(38957)