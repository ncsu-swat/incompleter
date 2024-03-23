# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16315)

    common_elements = _c_(16302, _n_(16300, "set", lambda: set), _n_(16301, "l1", lambda: l1)) & _c_(16305, _n_(16303, "set", lambda: set), _n_(16304, "l2", lambda: l2))
    _l_(16306)
    l2 = [_n_(16307, "e", lambda: e) for e in _n_(16308, "l2", lambda: l2) if _n_(16309, "e", lambda: e) in _n_(16310, "common_elements", lambda: common_elements)]
    _l_(16311)
    aux = _n_(16312, "l1", lambda: l1) == _n_(16313, "l2", lambda: l2)
    _l_(16314)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(16316)
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(16317)
color3 = ['white', 'orange', 'pink', 'black']
_l_(16318)
_c_(16320, _n_(16319, "print", lambda: print), 'Original lists:')
_l_(16321)
_c_(16324, _n_(16322, "print", lambda: print), _n_(16323, "color1", lambda: color1))
_l_(16325)
_c_(16328, _n_(16326, "print", lambda: print), _n_(16327, "color2", lambda: color2))
_l_(16329)
_c_(16332, _n_(16330, "print", lambda: print), _n_(16331, "color3", lambda: color3))
_l_(16333)
_c_(16335, _n_(16334, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16336)
_c_(16342, _n_(16337, "print", lambda: print), _c_(16341, _n_(16338, "same_order", lambda: same_order), _n_(16339, "color1", lambda: color1), _n_(16340, "color2", lambda: color2)))
_l_(16343)
_c_(16345, _n_(16344, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16346)
_c_(16352, _n_(16347, "print", lambda: print), _c_(16351, _n_(16348, "same_order", lambda: same_order), _n_(16349, "color1", lambda: color1), _n_(16350, "color3", lambda: color3)))
_l_(16353)
_c_(16355, _n_(16354, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16356)
_c_(16362, _n_(16357, "print", lambda: print), _c_(16361, _n_(16358, "same_order", lambda: same_order), _n_(16359, "color2", lambda: color2), _n_(16360, "color3", lambda: color3)))
_l_(16363)