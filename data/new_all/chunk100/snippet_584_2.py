# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_largest_number(lst):
    _l_(61178)

    if _c_(61153, _n_(61150, "all", lambda: all), (_n_(61151, "val", lambda: val) == 0 for val in _n_(61152, "lst", lambda: lst))):
        _l_(61155)

        aux = '0'
        _l_(61154)
        return aux
    result = _c_(61174, _a_(61156, '', "join"), _c_(61173, _n_(61157, "sorted", lambda: sorted), (_c_(61160, _n_(61158, "str", lambda: str), _n_(61159, "val", lambda: val)) for val in _n_(61161, "lst", lambda: lst)), reverse=False, key=lambda i: _n_(61162, "i", lambda: i) * (_c_(61169, _n_(61163, "len", lambda: len), _c_(61168, _n_(61164, "str", lambda: str), _c_(61167, _n_(61165, "min", lambda: min), _n_(61166, "lst", lambda: lst)))) * 2 // _c_(61172, _n_(61170, "len", lambda: len), _n_(61171, "i", lambda: i)))))
    _l_(61175)
    aux = _n_(61176, "result", lambda: result)
    _l_(61177)
    return aux
nums = [3, 40, 41, 43, 74, 9]
_l_(61179)
_c_(61181, _n_(61180, "print", lambda: print), 'Original list:')
_l_(61182)
_c_(61185, _n_(61183, "print", lambda: print), _n_(61184, "nums", lambda: nums))
_l_(61186)
_c_(61188, _n_(61187, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61189)
_c_(61194, _n_(61190, "print", lambda: print), _c_(61193, _n_(61191, "create_largest_number", lambda: create_largest_number), _n_(61192, "nums", lambda: nums)))
_l_(61195)
nums = [10, 40, 20, 30, 50, 60]
_l_(61196)
_c_(61198, _n_(61197, "print", lambda: print), '\nOriginal list:')
_l_(61199)
_c_(61202, _n_(61200, "print", lambda: print), _n_(61201, "nums", lambda: nums))
_l_(61203)
_c_(61205, _n_(61204, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61206)
_c_(61211, _n_(61207, "print", lambda: print), _c_(61210, _n_(61208, "create_largest_number", lambda: create_largest_number), _n_(61209, "nums", lambda: nums)))
_l_(61212)
_c_(61214, _n_(61213, "print", lambda: print), '\nOriginal list:')
_l_(61215)
_c_(61218, _n_(61216, "print", lambda: print), _n_(61217, "nums", lambda: nums))
_l_(61219)
_c_(61221, _n_(61220, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61222)
_c_(61227, _n_(61223, "print", lambda: print), _c_(61226, _n_(61224, "create_largest_number", lambda: create_largest_number), _n_(61225, "nums", lambda: nums)))
_l_(61228)