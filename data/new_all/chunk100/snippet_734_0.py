# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def discriminant():
    _l_(74059)

    y_value = _c_(74030, _n_(74027, "float", lambda: float), _c_(74029, _n_(74028, "input", lambda: input), 'The y value: '))
    _l_(74031)
    z_value = _c_(74035, _n_(74032, "float", lambda: float), _c_(74034, _n_(74033, "input", lambda: input), 'The z value: '))
    _l_(74036)
    discriminant = _n_(74037, "y_value", lambda: y_value) ** 2 - 4 * _n_(74038, "x_value", lambda: x_value) * _n_(74039, "z_value", lambda: z_value)
    _l_(74040)
    if _n_(74041, "discriminant", lambda: discriminant) > 0:
        _l_(74058)

        _c_(74044, _n_(74042, "print", lambda: print), 'Two Solutions. Discriminant value is:', _n_(74043, "discriminant", lambda: discriminant))
        _l_(74045)
    elif _n_(74046, "discriminant", lambda: discriminant) == 0:
        _l_(74057)

        _c_(74049, _n_(74047, "print", lambda: print), 'One Solution. Discriminant value is:', _n_(74048, "discriminant", lambda: discriminant))
        _l_(74050)
    elif _n_(74051, "discriminant", lambda: discriminant) < 0:
        _l_(74056)

        _c_(74054, _n_(74052, "print", lambda: print), 'No Real Solutions. Discriminant value is:', _n_(74053, "discriminant", lambda: discriminant))
        _l_(74055)
_c_(74061, _n_(74060, "discriminant", lambda: discriminant))
_l_(74062)