# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def access_elements(nums, list_index):
    _l_(65338)

    result = [_n_(65332, "nums", lambda: nums)[_n_(65333, "i", lambda: i)] for i in _n_(65334, "list_index", lambda: list_index)]
    _l_(65335)
    aux = _n_(65336, "result", lambda: result)
    _l_(65337)
    return aux
nums = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
_l_(65339)
_c_(65341, _n_(65340, "print", lambda: print), 'Original list:')
_l_(65342)
_c_(65345, _n_(65343, "print", lambda: print), _n_(65344, "nums", lambda: nums))
_l_(65346)
_c_(65348, _n_(65347, "print", lambda: print), 'Index list:')
_l_(65349)
_c_(65352, _n_(65350, "print", lambda: print), _n_(65351, "list_index", lambda: list_index))
_l_(65353)
_c_(65355, _n_(65354, "print", lambda: print), '\nItems with specified index of the said list:')
_l_(65356)
_c_(65362, _n_(65357, "print", lambda: print), _c_(65361, _n_(65358, "access_elements", lambda: access_elements), _n_(65359, "nums", lambda: nums), _n_(65360, "list_index", lambda: list_index)))
_l_(65363)