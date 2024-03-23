# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_largest_number(lst):
    _l_(61039)

    if _c_(61014, _n_(61011, "all", lambda: all), (_n_(61012, "val", lambda: val) == 0 for val in _n_(61013, "lst", lambda: lst))):
        _l_(61016)

        aux = '0'
        _l_(61015)
        return aux
    result = _c_(61035, _a_(61017, '', "join"), _c_(61034, _n_(61018, "sorted", lambda: sorted), (_c_(61021, _n_(61019, "str", lambda: str), _n_(61020, "val", lambda: val)) for val in _n_(61022, "lst", lambda: lst)), reverse=False, key=lambda i: _n_(61023, "i", lambda: i) * (_c_(61030, _n_(61024, "len", lambda: len), _c_(61029, _n_(61025, "str", lambda: str), _c_(61028, _n_(61026, "min", lambda: min), _n_(61027, "lst", lambda: lst)))) * 2 // _c_(61033, _n_(61031, "len", lambda: len), _n_(61032, "i", lambda: i)))))
    _l_(61036)
    aux = _n_(61037, "result", lambda: result)
    _l_(61038)
    return aux
_c_(61041, _n_(61040, "print", lambda: print), 'Original list:')
_l_(61042)
_c_(61045, _n_(61043, "print", lambda: print), _n_(61044, "nums", lambda: nums))
_l_(61046)
_c_(61048, _n_(61047, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61049)
_c_(61054, _n_(61050, "print", lambda: print), _c_(61053, _n_(61051, "create_largest_number", lambda: create_largest_number), _n_(61052, "nums", lambda: nums)))
_l_(61055)
nums = [10, 40, 20, 30, 50, 60]
_l_(61056)
_c_(61058, _n_(61057, "print", lambda: print), '\nOriginal list:')
_l_(61059)
_c_(61062, _n_(61060, "print", lambda: print), _n_(61061, "nums", lambda: nums))
_l_(61063)
_c_(61065, _n_(61064, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61066)
_c_(61071, _n_(61067, "print", lambda: print), _c_(61070, _n_(61068, "create_largest_number", lambda: create_largest_number), _n_(61069, "nums", lambda: nums)))
_l_(61072)
nums = [8, 4, 2, 9, 5, 6, 1, 0]
_l_(61073)
_c_(61075, _n_(61074, "print", lambda: print), '\nOriginal list:')
_l_(61076)
_c_(61079, _n_(61077, "print", lambda: print), _n_(61078, "nums", lambda: nums))
_l_(61080)
_c_(61082, _n_(61081, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61083)
_c_(61088, _n_(61084, "print", lambda: print), _c_(61087, _n_(61085, "create_largest_number", lambda: create_largest_number), _n_(61086, "nums", lambda: nums)))
_l_(61089)