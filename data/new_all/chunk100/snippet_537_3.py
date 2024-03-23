# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def specified_element(nums, N):
    _l_(54332)

    result = [_n_(54326, "i", lambda: i)[_n_(54327, "N", lambda: N)] for i in _n_(54328, "nums", lambda: nums)]
    _l_(54329)
    aux = _n_(54330, "result", lambda: result)
    _l_(54331)
    return aux
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
_l_(54333)
_c_(54335, _n_(54334, "print", lambda: print), 'Original list of lists:')
_l_(54336)
_c_(54339, _n_(54337, "print", lambda: print), _n_(54338, "nums", lambda: nums))
_l_(54340)
_c_(54342, _n_(54341, "print", lambda: print), '\nExtract every first element from the said given two dimensional list:')
_l_(54343)
_c_(54349, _n_(54344, "print", lambda: print), _c_(54348, _n_(54345, "specified_element", lambda: specified_element), _n_(54346, "nums", lambda: nums), _n_(54347, "N", lambda: N)))
_l_(54350)
N = 2
_l_(54351)
_c_(54353, _n_(54352, "print", lambda: print), '\nExtract every third element from the said given two dimensional list:')
_l_(54354)
_c_(54360, _n_(54355, "print", lambda: print), _c_(54359, _n_(54356, "specified_element", lambda: specified_element), _n_(54357, "nums", lambda: nums), _n_(54358, "N", lambda: N)))
_l_(54361)