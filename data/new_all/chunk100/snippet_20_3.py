# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16452)

    common_elements = _c_(16434, _n_(16432, "set", lambda: set), _n_(16433, "l1", lambda: l1)) & _c_(16437, _n_(16435, "set", lambda: set), _n_(16436, "l2", lambda: l2))
    _l_(16438)
    l1 = [_n_(16439, "e", lambda: e) for e in _n_(16440, "l1", lambda: l1) if _n_(16441, "e", lambda: e) in _n_(16442, "common_elements", lambda: common_elements)]
    _l_(16443)
    l2 = [_n_(16444, "e", lambda: e) for e in _n_(16445, "l2", lambda: l2) if _n_(16446, "e", lambda: e) in _n_(16447, "common_elements", lambda: common_elements)]
    _l_(16448)
    aux = _n_(16449, "l1", lambda: l1) == _n_(16450, "l2", lambda: l2)
    _l_(16451)
    return aux
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(16453)
color3 = ['white', 'orange', 'pink', 'black']
_l_(16454)
_c_(16456, _n_(16455, "print", lambda: print), 'Original lists:')
_l_(16457)
_c_(16460, _n_(16458, "print", lambda: print), _n_(16459, "color1", lambda: color1))
_l_(16461)
_c_(16464, _n_(16462, "print", lambda: print), _n_(16463, "color2", lambda: color2))
_l_(16465)
_c_(16468, _n_(16466, "print", lambda: print), _n_(16467, "color3", lambda: color3))
_l_(16469)
_c_(16471, _n_(16470, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16472)
_c_(16478, _n_(16473, "print", lambda: print), _c_(16477, _n_(16474, "same_order", lambda: same_order), _n_(16475, "color1", lambda: color1), _n_(16476, "color2", lambda: color2)))
_l_(16479)
_c_(16481, _n_(16480, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16482)
_c_(16488, _n_(16483, "print", lambda: print), _c_(16487, _n_(16484, "same_order", lambda: same_order), _n_(16485, "color1", lambda: color1), _n_(16486, "color3", lambda: color3)))
_l_(16489)
_c_(16491, _n_(16490, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16492)
_c_(16498, _n_(16493, "print", lambda: print), _c_(16497, _n_(16494, "same_order", lambda: same_order), _n_(16495, "color2", lambda: color2), _n_(16496, "color3", lambda: color3)))
_l_(16499)