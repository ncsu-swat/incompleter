# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16577)

    common_elements = _c_(16564, _n_(16562, "set", lambda: set), _n_(16563, "l1", lambda: l1)) & _c_(16567, _n_(16565, "set", lambda: set), _n_(16566, "l2", lambda: l2))
    _l_(16568)
    l1 = [_n_(16569, "e", lambda: e) for e in _n_(16570, "l1", lambda: l1) if _n_(16571, "e", lambda: e) in _n_(16572, "common_elements", lambda: common_elements)]
    _l_(16573)
    aux = _n_(16574, "l1", lambda: l1) == _n_(16575, "l2", lambda: l2)
    _l_(16576)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(16578)
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(16579)
color3 = ['white', 'orange', 'pink', 'black']
_l_(16580)
_c_(16582, _n_(16581, "print", lambda: print), 'Original lists:')
_l_(16583)
_c_(16586, _n_(16584, "print", lambda: print), _n_(16585, "color1", lambda: color1))
_l_(16587)
_c_(16590, _n_(16588, "print", lambda: print), _n_(16589, "color2", lambda: color2))
_l_(16591)
_c_(16594, _n_(16592, "print", lambda: print), _n_(16593, "color3", lambda: color3))
_l_(16595)
_c_(16597, _n_(16596, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16598)
_c_(16604, _n_(16599, "print", lambda: print), _c_(16603, _n_(16600, "same_order", lambda: same_order), _n_(16601, "color1", lambda: color1), _n_(16602, "color2", lambda: color2)))
_l_(16605)
_c_(16607, _n_(16606, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16608)
_c_(16614, _n_(16609, "print", lambda: print), _c_(16613, _n_(16610, "same_order", lambda: same_order), _n_(16611, "color1", lambda: color1), _n_(16612, "color3", lambda: color3)))
_l_(16615)
_c_(16617, _n_(16616, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16618)
_c_(16624, _n_(16619, "print", lambda: print), _c_(16623, _n_(16620, "same_order", lambda: same_order), _n_(16621, "color2", lambda: color2), _n_(16622, "color3", lambda: color3)))
_l_(16625)