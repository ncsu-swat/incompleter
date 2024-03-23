# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16384)

    common_elements = _c_(16366, _n_(16364, "set", lambda: set), _n_(16365, "l1", lambda: l1)) & _c_(16369, _n_(16367, "set", lambda: set), _n_(16368, "l2", lambda: l2))
    _l_(16370)
    l1 = [_n_(16371, "e", lambda: e) for e in _n_(16372, "l1", lambda: l1) if _n_(16373, "e", lambda: e) in _n_(16374, "common_elements", lambda: common_elements)]
    _l_(16375)
    l2 = [_n_(16376, "e", lambda: e) for e in _n_(16377, "l2", lambda: l2) if _n_(16378, "e", lambda: e) in _n_(16379, "common_elements", lambda: common_elements)]
    _l_(16380)
    aux = _n_(16381, "l1", lambda: l1) == _n_(16382, "l2", lambda: l2)
    _l_(16383)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(16385)
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(16386)
_c_(16388, _n_(16387, "print", lambda: print), 'Original lists:')
_l_(16389)
_c_(16392, _n_(16390, "print", lambda: print), _n_(16391, "color1", lambda: color1))
_l_(16393)
_c_(16396, _n_(16394, "print", lambda: print), _n_(16395, "color2", lambda: color2))
_l_(16397)
_c_(16400, _n_(16398, "print", lambda: print), _n_(16399, "color3", lambda: color3))
_l_(16401)
_c_(16403, _n_(16402, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16404)
_c_(16410, _n_(16405, "print", lambda: print), _c_(16409, _n_(16406, "same_order", lambda: same_order), _n_(16407, "color1", lambda: color1), _n_(16408, "color2", lambda: color2)))
_l_(16411)
_c_(16413, _n_(16412, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16414)
_c_(16420, _n_(16415, "print", lambda: print), _c_(16419, _n_(16416, "same_order", lambda: same_order), _n_(16417, "color1", lambda: color1), _n_(16418, "color3", lambda: color3)))
_l_(16421)
_c_(16423, _n_(16422, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16424)
_c_(16430, _n_(16425, "print", lambda: print), _c_(16429, _n_(16426, "same_order", lambda: same_order), _n_(16427, "color2", lambda: color2), _n_(16428, "color3", lambda: color3)))
_l_(16431)