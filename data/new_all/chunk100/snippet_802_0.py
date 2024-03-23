# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def arclength():
    _l_(80899)

    pi = 22 / 7
    _l_(80879)
    angle = _c_(80883, _n_(80880, "float", lambda: float), _c_(80882, _n_(80881, "input", lambda: input), 'angle measure: '))
    _l_(80884)
    if _n_(80885, "angle", lambda: angle) >= 360:
        _l_(80890)

        _c_(80887, _n_(80886, "print", lambda: print), 'Angle is not possible')
        _l_(80888)
        aux = ""
        _l_(80889)
        return aux
    arc_length = _n_(80891, "pi", lambda: pi) * _n_(80892, "diameter", lambda: diameter) * (_n_(80893, "angle", lambda: angle) / 360)
    _l_(80894)
    _c_(80897, _n_(80895, "print", lambda: print), 'Arc Length is: ', _n_(80896, "arc_length", lambda: arc_length))
    _l_(80898)
_c_(80901, _n_(80900, "arclength", lambda: arclength))
_l_(80902)