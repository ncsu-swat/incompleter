# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(104687)

    common_elements = _c_(104669, _n_(104667, "set", lambda: set), _n_(104668, "l1", lambda: l1)) & _c_(104672, _n_(104670, "set", lambda: set), _n_(104671, "l2", lambda: l2))
    _l_(104673)
    l1 = [_n_(104674, "e", lambda: e) for e in _n_(104675, "l1", lambda: l1) if _n_(104676, "e", lambda: e) in _n_(104677, "common_elements", lambda: common_elements)]
    _l_(104678)
    l2 = [_n_(104679, "e", lambda: e) for e in _n_(104680, "l2", lambda: l2) if _n_(104681, "e", lambda: e) in _n_(104682, "common_elements", lambda: common_elements)]
    _l_(104683)
    aux = _n_(104684, "l1", lambda: l1) == _n_(104685, "l2", lambda: l2)
    _l_(104686)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(104688)
color3 = ['white', 'orange', 'pink', 'black']
_l_(104689)
_c_(104691, _n_(104690, "print", lambda: print), 'Original lists:')
_l_(104692)
_c_(104695, _n_(104693, "print", lambda: print), _n_(104694, "color1", lambda: color1))
_l_(104696)
_c_(104699, _n_(104697, "print", lambda: print), _n_(104698, "color2", lambda: color2))
_l_(104700)
_c_(104703, _n_(104701, "print", lambda: print), _n_(104702, "color3", lambda: color3))
_l_(104704)
_c_(104706, _n_(104705, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(104707)
_c_(104713, _n_(104708, "print", lambda: print), _c_(104712, _n_(104709, "same_order", lambda: same_order), _n_(104710, "color1", lambda: color1), _n_(104711, "color2", lambda: color2)))
_l_(104714)
_c_(104716, _n_(104715, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(104717)
_c_(104723, _n_(104718, "print", lambda: print), _c_(104722, _n_(104719, "same_order", lambda: same_order), _n_(104720, "color1", lambda: color1), _n_(104721, "color3", lambda: color3)))
_l_(104724)
_c_(104726, _n_(104725, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(104727)
_c_(104733, _n_(104728, "print", lambda: print), _c_(104732, _n_(104729, "same_order", lambda: same_order), _n_(104730, "color2", lambda: color2), _n_(104731, "color3", lambda: color3)))
_l_(104734)