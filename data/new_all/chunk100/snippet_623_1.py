# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def access_elements(nums, list_index):
    _l_(65370)

    result = [_n_(65364, "nums", lambda: nums)[_n_(65365, "i", lambda: i)] for i in _n_(65366, "list_index", lambda: list_index)]
    _l_(65367)
    aux = _n_(65368, "result", lambda: result)
    _l_(65369)
    return aux
_c_(65372, _n_(65371, "print", lambda: print), 'Original list:')
_l_(65373)
_c_(65376, _n_(65374, "print", lambda: print), _n_(65375, "nums", lambda: nums))
_l_(65377)
list_index = [0, 3, 5, 7, 10]
_l_(65378)
_c_(65380, _n_(65379, "print", lambda: print), 'Index list:')
_l_(65381)
_c_(65384, _n_(65382, "print", lambda: print), _n_(65383, "list_index", lambda: list_index))
_l_(65385)
_c_(65387, _n_(65386, "print", lambda: print), '\nItems with specified index of the said list:')
_l_(65388)
_c_(65394, _n_(65389, "print", lambda: print), _c_(65393, _n_(65390, "access_elements", lambda: access_elements), _n_(65391, "nums", lambda: nums), _n_(65392, "list_index", lambda: list_index)))
_l_(65395)