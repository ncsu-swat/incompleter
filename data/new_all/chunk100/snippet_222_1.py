# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sectorarea():
    _l_(17473)

    radius = _c_(17452, _n_(17449, "float", lambda: float), _c_(17451, _n_(17450, "input", lambda: input), 'Radius of Circle: '))
    _l_(17453)
    angle = _c_(17457, _n_(17454, "float", lambda: float), _c_(17456, _n_(17455, "input", lambda: input), 'angle measure: '))
    _l_(17458)
    if _n_(17459, "angle", lambda: angle) >= 360:
        _l_(17464)

        _c_(17461, _n_(17460, "print", lambda: print), 'Angle is not possible')
        _l_(17462)
        aux = ""
        _l_(17463)
        return aux
    sur_area = _n_(17465, "pi", lambda: pi) * _n_(17466, "radius", lambda: radius) ** 2 * (_n_(17467, "angle", lambda: angle) / 360)
    _l_(17468)
    _c_(17471, _n_(17469, "print", lambda: print), 'Sector Area: ', _n_(17470, "sur_area", lambda: sur_area))
    _l_(17472)
_c_(17475, _n_(17474, "sectorarea", lambda: sectorarea))
_l_(17476)