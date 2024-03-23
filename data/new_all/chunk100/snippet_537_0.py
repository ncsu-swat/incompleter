# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def specified_element(nums, N):
    _l_(54227)

    result = [_n_(54221, "i", lambda: i)[_n_(54222, "N", lambda: N)] for i in _n_(54223, "nums", lambda: nums)]
    _l_(54224)
    aux = _n_(54225, "result", lambda: result)
    _l_(54226)
    return aux
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
_l_(54228)
_c_(54230, _n_(54229, "print", lambda: print), 'Original list of lists:')
_l_(54231)
_c_(54234, _n_(54232, "print", lambda: print), _n_(54233, "nums", lambda: nums))
_l_(54235)
N = 0
_l_(54236)
_c_(54238, _n_(54237, "print", lambda: print), '\nExtract every first element from the said given two dimensional list:')
_l_(54239)
_c_(54245, _n_(54240, "print", lambda: print), _c_(54244, _n_(54241, "specified_element", lambda: specified_element), _n_(54242, "nums", lambda: nums), _n_(54243, "N", lambda: N)))
_l_(54246)
_c_(54248, _n_(54247, "print", lambda: print), '\nExtract every third element from the said given two dimensional list:')
_l_(54249)
_c_(54255, _n_(54250, "print", lambda: print), _c_(54254, _n_(54251, "specified_element", lambda: specified_element), _n_(54252, "nums", lambda: nums), _n_(54253, "N", lambda: N)))
_l_(54256)