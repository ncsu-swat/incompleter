# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def create_largest_number(lst):
    _l_(61257)

    if _c_(61232, _n_(61229, "all", lambda: all), (_n_(61230, "val", lambda: val) == 0 for val in _n_(61231, "lst", lambda: lst))):
        _l_(61234)

        aux = '0'
        _l_(61233)
        return aux
    result = _c_(61253, _a_(61235, '', "join"), _c_(61252, _n_(61236, "sorted", lambda: sorted), (_c_(61239, _n_(61237, "str", lambda: str), _n_(61238, "val", lambda: val)) for val in _n_(61240, "lst", lambda: lst)), reverse=False, key=lambda i: _n_(61241, "i", lambda: i) * (_c_(61248, _n_(61242, "len", lambda: len), _c_(61247, _n_(61243, "str", lambda: str), _c_(61246, _n_(61244, "min", lambda: min), _n_(61245, "lst", lambda: lst)))) * 2 // _c_(61251, _n_(61249, "len", lambda: len), _n_(61250, "i", lambda: i)))))
    _l_(61254)
    aux = _n_(61255, "result", lambda: result)
    _l_(61256)
    return aux
nums = [3, 40, 41, 43, 74, 9]
_l_(61258)
_c_(61260, _n_(61259, "print", lambda: print), 'Original list:')
_l_(61261)
_c_(61264, _n_(61262, "print", lambda: print), _n_(61263, "nums", lambda: nums))
_l_(61265)
_c_(61267, _n_(61266, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61268)
_c_(61273, _n_(61269, "print", lambda: print), _c_(61272, _n_(61270, "create_largest_number", lambda: create_largest_number), _n_(61271, "nums", lambda: nums)))
_l_(61274)
_c_(61276, _n_(61275, "print", lambda: print), '\nOriginal list:')
_l_(61277)
_c_(61280, _n_(61278, "print", lambda: print), _n_(61279, "nums", lambda: nums))
_l_(61281)
_c_(61283, _n_(61282, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61284)
_c_(61289, _n_(61285, "print", lambda: print), _c_(61288, _n_(61286, "create_largest_number", lambda: create_largest_number), _n_(61287, "nums", lambda: nums)))
_l_(61290)
nums = [8, 4, 2, 9, 5, 6, 1, 0]
_l_(61291)
_c_(61293, _n_(61292, "print", lambda: print), '\nOriginal list:')
_l_(61294)
_c_(61297, _n_(61295, "print", lambda: print), _n_(61296, "nums", lambda: nums))
_l_(61298)
_c_(61300, _n_(61299, "print", lambda: print), 'Smallest possible number using the elements of the said list of positive integers:')
_l_(61301)
_c_(61306, _n_(61302, "print", lambda: print), _c_(61305, _n_(61303, "create_largest_number", lambda: create_largest_number), _n_(61304, "nums", lambda: nums)))
_l_(61307)