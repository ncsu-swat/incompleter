# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sectorarea():
    _l_(17445)

    pi = 22 / 7
    _l_(17425)
    angle = _c_(17429, _n_(17426, "float", lambda: float), _c_(17428, _n_(17427, "input", lambda: input), 'angle measure: '))
    _l_(17430)
    if _n_(17431, "angle", lambda: angle) >= 360:
        _l_(17436)

        _c_(17433, _n_(17432, "print", lambda: print), 'Angle is not possible')
        _l_(17434)
        aux = ""
        _l_(17435)
        return aux
    sur_area = _n_(17437, "pi", lambda: pi) * _n_(17438, "radius", lambda: radius) ** 2 * (_n_(17439, "angle", lambda: angle) / 360)
    _l_(17440)
    _c_(17443, _n_(17441, "print", lambda: print), 'Sector Area: ', _n_(17442, "sur_area", lambda: sur_area))
    _l_(17444)
_c_(17447, _n_(17446, "sectorarea", lambda: sectorarea))
_l_(17448)