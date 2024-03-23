# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11196)

    result = _n_(11183, "lst", lambda: lst)
    _l_(11184)
    _n_(11185, "result", lambda: result)[_n_(11186, "merge_from", lambda: merge_from):_n_(11187, "merge_to", lambda: merge_to)] = [_c_(11192, _a_(11188, '', "join"), _n_(11189, "result", lambda: result)[_n_(11190, "merge_from", lambda: merge_from):_n_(11191, "merge_to", lambda: merge_to)])]
    _l_(11193)
    aux = _n_(11194, "result", lambda: result)
    _l_(11195)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11197)
_c_(11199, _n_(11198, "print", lambda: print), 'Original lists:')
_l_(11200)
_c_(11203, _n_(11201, "print", lambda: print), _n_(11202, "chars", lambda: chars))
_l_(11204)
merge_from = 2
_l_(11205)
merge_to = 4
_l_(11206)
_c_(11210, _n_(11207, "print", lambda: print), '\nMerge items from', _n_(11208, "merge_from", lambda: merge_from), 'to', _n_(11209, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11211)
_c_(11218, _n_(11212, "print", lambda: print), _c_(11217, _n_(11213, "merge_some_chars", lambda: merge_some_chars), _n_(11214, "chars", lambda: chars), _n_(11215, "merge_from", lambda: merge_from), _n_(11216, "merge_to", lambda: merge_to)))
_l_(11219)
merge_from = 3
_l_(11220)
merge_to = 7
_l_(11221)
_c_(11225, _n_(11222, "print", lambda: print), '\nMerge items from', _n_(11223, "merge_from", lambda: merge_from), 'to', _n_(11224, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11226)
_c_(11233, _n_(11227, "print", lambda: print), _c_(11232, _n_(11228, "merge_some_chars", lambda: merge_some_chars), _n_(11229, "chars", lambda: chars), _n_(11230, "merge_from", lambda: merge_from), _n_(11231, "merge_to", lambda: merge_to)))
_l_(11234)