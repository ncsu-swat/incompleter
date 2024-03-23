# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def to_uppercase(str1):
    _l_(63104)

    for letter in _n_(63088, "str1", lambda: str1)[:4]:
        _l_(63095)

        if _c_(63091, _a_(63090, _n_(63089, "letter", lambda: letter), "upper")) == _n_(63092, "letter", lambda: letter):
            _l_(63094)

            num_upper += 1
            _l_(63093)
    if _n_(63096, "num_upper", lambda: num_upper) >= 2:
        _l_(63101)

        aux = _c_(63099, _a_(63098, _n_(63097, "str1", lambda: str1), "upper"))
        _l_(63100)
        return aux
    aux = _n_(63102, "str1", lambda: str1)
    _l_(63103)
    return aux
_c_(63108, _n_(63105, "print", lambda: print), _c_(63107, _n_(63106, "to_uppercase", lambda: to_uppercase), 'Python'))
_l_(63109)
_c_(63113, _n_(63110, "print", lambda: print), _c_(63112, _n_(63111, "to_uppercase", lambda: to_uppercase), 'PyThon'))
_l_(63114)