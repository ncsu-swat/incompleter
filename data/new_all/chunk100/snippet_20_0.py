# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16252)

    common_elements = _c_(16234, _n_(16232, "set", lambda: set), _n_(16233, "l1", lambda: l1)) & _c_(16237, _n_(16235, "set", lambda: set), _n_(16236, "l2", lambda: l2))
    _l_(16238)
    l1 = [_n_(16239, "e", lambda: e) for e in _n_(16240, "l1", lambda: l1) if _n_(16241, "e", lambda: e) in _n_(16242, "common_elements", lambda: common_elements)]
    _l_(16243)
    l2 = [_n_(16244, "e", lambda: e) for e in _n_(16245, "l2", lambda: l2) if _n_(16246, "e", lambda: e) in _n_(16247, "common_elements", lambda: common_elements)]
    _l_(16248)
    aux = _n_(16249, "l1", lambda: l1) == _n_(16250, "l2", lambda: l2)
    _l_(16251)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(16253)
color3 = ['white', 'orange', 'pink', 'black']
_l_(16254)
_c_(16256, _n_(16255, "print", lambda: print), 'Original lists:')
_l_(16257)
_c_(16260, _n_(16258, "print", lambda: print), _n_(16259, "color1", lambda: color1))
_l_(16261)
_c_(16264, _n_(16262, "print", lambda: print), _n_(16263, "color2", lambda: color2))
_l_(16265)
_c_(16268, _n_(16266, "print", lambda: print), _n_(16267, "color3", lambda: color3))
_l_(16269)
_c_(16271, _n_(16270, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16272)
_c_(16278, _n_(16273, "print", lambda: print), _c_(16277, _n_(16274, "same_order", lambda: same_order), _n_(16275, "color1", lambda: color1), _n_(16276, "color2", lambda: color2)))
_l_(16279)
_c_(16281, _n_(16280, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16282)
_c_(16288, _n_(16283, "print", lambda: print), _c_(16287, _n_(16284, "same_order", lambda: same_order), _n_(16285, "color1", lambda: color1), _n_(16286, "color3", lambda: color3)))
_l_(16289)
_c_(16291, _n_(16290, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16292)
_c_(16298, _n_(16293, "print", lambda: print), _c_(16297, _n_(16294, "same_order", lambda: same_order), _n_(16295, "color2", lambda: color2), _n_(16296, "color3", lambda: color3)))
_l_(16299)