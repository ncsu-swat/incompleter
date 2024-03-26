# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(104823)

    common_elements = _c_(104805, _n_(104803, "set", lambda: set), _n_(104804, "l1", lambda: l1)) & _c_(104808, _n_(104806, "set", lambda: set), _n_(104807, "l2", lambda: l2))
    _l_(104809)
    l1 = [_n_(104810, "e", lambda: e) for e in _n_(104811, "l1", lambda: l1) if _n_(104812, "e", lambda: e) in _n_(104813, "common_elements", lambda: common_elements)]
    _l_(104814)
    l2 = [_n_(104815, "e", lambda: e) for e in _n_(104816, "l2", lambda: l2) if _n_(104817, "e", lambda: e) in _n_(104818, "common_elements", lambda: common_elements)]
    _l_(104819)
    aux = _n_(104820, "l1", lambda: l1) == _n_(104821, "l2", lambda: l2)
    _l_(104822)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(104824)
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(104825)
_c_(104827, _n_(104826, "print", lambda: print), 'Original lists:')
_l_(104828)
_c_(104831, _n_(104829, "print", lambda: print), _n_(104830, "color1", lambda: color1))
_l_(104832)
_c_(104835, _n_(104833, "print", lambda: print), _n_(104834, "color2", lambda: color2))
_l_(104836)
_c_(104839, _n_(104837, "print", lambda: print), _n_(104838, "color3", lambda: color3))
_l_(104840)
_c_(104842, _n_(104841, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(104843)
_c_(104849, _n_(104844, "print", lambda: print), _c_(104848, _n_(104845, "same_order", lambda: same_order), _n_(104846, "color1", lambda: color1), _n_(104847, "color2", lambda: color2)))
_l_(104850)
_c_(104852, _n_(104851, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(104853)
_c_(104859, _n_(104854, "print", lambda: print), _c_(104858, _n_(104855, "same_order", lambda: same_order), _n_(104856, "color1", lambda: color1), _n_(104857, "color3", lambda: color3)))
_l_(104860)
_c_(104862, _n_(104861, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(104863)
_c_(104869, _n_(104864, "print", lambda: print), _c_(104868, _n_(104865, "same_order", lambda: same_order), _n_(104866, "color2", lambda: color2), _n_(104867, "color3", lambda: color3)))
_l_(104870)