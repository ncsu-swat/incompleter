# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(104755)

    common_elements = _c_(104737, _n_(104735, "set", lambda: set), _n_(104736, "l1", lambda: l1)) & _c_(104740, _n_(104738, "set", lambda: set), _n_(104739, "l2", lambda: l2))
    _l_(104741)
    l1 = [_n_(104742, "e", lambda: e) for e in _n_(104743, "l1", lambda: l1) if _n_(104744, "e", lambda: e) in _n_(104745, "common_elements", lambda: common_elements)]
    _l_(104746)
    l2 = [_n_(104747, "e", lambda: e) for e in _n_(104748, "l2", lambda: l2) if _n_(104749, "e", lambda: e) in _n_(104750, "common_elements", lambda: common_elements)]
    _l_(104751)
    aux = _n_(104752, "l1", lambda: l1) == _n_(104753, "l2", lambda: l2)
    _l_(104754)
    return aux
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(104756)
color3 = ['white', 'orange', 'pink', 'black']
_l_(104757)
_c_(104759, _n_(104758, "print", lambda: print), 'Original lists:')
_l_(104760)
_c_(104763, _n_(104761, "print", lambda: print), _n_(104762, "color1", lambda: color1))
_l_(104764)
_c_(104767, _n_(104765, "print", lambda: print), _n_(104766, "color2", lambda: color2))
_l_(104768)
_c_(104771, _n_(104769, "print", lambda: print), _n_(104770, "color3", lambda: color3))
_l_(104772)
_c_(104774, _n_(104773, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(104775)
_c_(104781, _n_(104776, "print", lambda: print), _c_(104780, _n_(104777, "same_order", lambda: same_order), _n_(104778, "color1", lambda: color1), _n_(104779, "color2", lambda: color2)))
_l_(104782)
_c_(104784, _n_(104783, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(104785)
_c_(104791, _n_(104786, "print", lambda: print), _c_(104790, _n_(104787, "same_order", lambda: same_order), _n_(104788, "color1", lambda: color1), _n_(104789, "color3", lambda: color3)))
_l_(104792)
_c_(104794, _n_(104793, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(104795)
_c_(104801, _n_(104796, "print", lambda: print), _c_(104800, _n_(104797, "same_order", lambda: same_order), _n_(104798, "color2", lambda: color2), _n_(104799, "color3", lambda: color3)))
_l_(104802)