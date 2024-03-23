# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def same_order(l1, l2):
    _l_(16513)

    l1 = [_n_(16500, "e", lambda: e) for e in _n_(16501, "l1", lambda: l1) if _n_(16502, "e", lambda: e) in _n_(16503, "common_elements", lambda: common_elements)]
    _l_(16504)
    l2 = [_n_(16505, "e", lambda: e) for e in _n_(16506, "l2", lambda: l2) if _n_(16507, "e", lambda: e) in _n_(16508, "common_elements", lambda: common_elements)]
    _l_(16509)
    aux = _n_(16510, "l1", lambda: l1) == _n_(16511, "l2", lambda: l2)
    _l_(16512)
    return aux
color1 = ['red', 'green', 'black', 'orange']
_l_(16514)
color2 = ['red', 'pink', 'green', 'white', 'black']
_l_(16515)
color3 = ['white', 'orange', 'pink', 'black']
_l_(16516)
_c_(16518, _n_(16517, "print", lambda: print), 'Original lists:')
_l_(16519)
_c_(16522, _n_(16520, "print", lambda: print), _n_(16521, "color1", lambda: color1))
_l_(16523)
_c_(16526, _n_(16524, "print", lambda: print), _n_(16525, "color2", lambda: color2))
_l_(16527)
_c_(16530, _n_(16528, "print", lambda: print), _n_(16529, "color3", lambda: color3))
_l_(16531)
_c_(16533, _n_(16532, "print", lambda: print), '\nTest common elements between color1 and color2 are in same order?')
_l_(16534)
_c_(16540, _n_(16535, "print", lambda: print), _c_(16539, _n_(16536, "same_order", lambda: same_order), _n_(16537, "color1", lambda: color1), _n_(16538, "color2", lambda: color2)))
_l_(16541)
_c_(16543, _n_(16542, "print", lambda: print), '\nTest common elements between color1 and color3 are in same order?')
_l_(16544)
_c_(16550, _n_(16545, "print", lambda: print), _c_(16549, _n_(16546, "same_order", lambda: same_order), _n_(16547, "color1", lambda: color1), _n_(16548, "color3", lambda: color3)))
_l_(16551)
_c_(16553, _n_(16552, "print", lambda: print), '\nTest common elements between color2 and color3 are in same order?')
_l_(16554)
_c_(16560, _n_(16555, "print", lambda: print), _c_(16559, _n_(16556, "same_order", lambda: same_order), _n_(16557, "color2", lambda: color2), _n_(16558, "color3", lambda: color3)))
_l_(16561)