# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def arclength():
    _l_(80927)

    diameter = _c_(80906, _n_(80903, "float", lambda: float), _c_(80905, _n_(80904, "input", lambda: input), 'Diameter of circle: '))
    _l_(80907)
    angle = _c_(80911, _n_(80908, "float", lambda: float), _c_(80910, _n_(80909, "input", lambda: input), 'angle measure: '))
    _l_(80912)
    if _n_(80913, "angle", lambda: angle) >= 360:
        _l_(80918)

        _c_(80915, _n_(80914, "print", lambda: print), 'Angle is not possible')
        _l_(80916)
        aux = ""
        _l_(80917)
        return aux
    arc_length = _n_(80919, "pi", lambda: pi) * _n_(80920, "diameter", lambda: diameter) * (_n_(80921, "angle", lambda: angle) / 360)
    _l_(80922)
    _c_(80925, _n_(80923, "print", lambda: print), 'Arc Length is: ', _n_(80924, "arc_length", lambda: arc_length))
    _l_(80926)
_c_(80929, _n_(80928, "arclength", lambda: arclength))
_l_(80930)