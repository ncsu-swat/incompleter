# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/699866/python-int-to-binary-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def dectobin(number):
    _l_(1540879)

    bin = ''
    _l_(1540865)
    while (_n_(1540866, "number", lambda: number) >= 1):
        _l_(1540876)

        number, rem = _c_(1540869, _n_(1540867, "divmod", lambda: divmod), _n_(1540868, "number", lambda: number), 2)
        _l_(1540870)
        bin = _n_(1540871, "bin", lambda: bin) + _c_(1540874, _n_(1540872, "str", lambda: str), _n_(1540873, "rem", lambda: rem))
        _l_(1540875)
    aux = _n_(1540877, "bin", lambda: bin)
    _l_(1540878)
    return aux

