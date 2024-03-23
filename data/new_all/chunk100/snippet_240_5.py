# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19302)

    max_val = _c_(19279, _n_(19277, "max", lambda: max), _n_(19278, "nums", lambda: nums))
    _l_(19280)
    min_val = _c_(19283, _n_(19281, "min", lambda: min), _n_(19282, "nums", lambda: nums))
    _l_(19284)
    max_result = [_n_(19285, "i", lambda: i) for (i, j) in _c_(19288, _n_(19286, "enumerate", lambda: enumerate), _n_(19287, "nums", lambda: nums)) if _n_(19289, "j", lambda: j) == _n_(19290, "max_val", lambda: max_val)]
    _l_(19291)
    min_result = [_n_(19292, "i", lambda: i) for (i, j) in _c_(19295, _n_(19293, "enumerate", lambda: enumerate), _n_(19294, "nums", lambda: nums)) if _n_(19296, "j", lambda: j) == _n_(19297, "min_val", lambda: min_val)]
    _l_(19298)
    aux = (_n_(19299, "max_result", lambda: max_result), _n_(19300, "min_result", lambda: min_result))
    _l_(19301)
    return aux
_c_(19304, _n_(19303, "print", lambda: print), 'Original list:')
_l_(19305)
_c_(19308, _n_(19306, "print", lambda: print), _n_(19307, "nums", lambda: nums))
_l_(19309)
result = _c_(19312, _n_(19310, "position_max_min", lambda: position_max_min), _n_(19311, "nums", lambda: nums))
_l_(19313)
_c_(19315, _n_(19314, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19316)
_c_(19319, _n_(19317, "print", lambda: print), _n_(19318, "result", lambda: result)[0])
_l_(19320)
_c_(19322, _n_(19321, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19323)
_c_(19326, _n_(19324, "print", lambda: print), _n_(19325, "result", lambda: result)[1])
_l_(19327)