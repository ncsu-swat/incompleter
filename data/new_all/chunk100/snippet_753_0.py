# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class IOString:
    _l_(76718)


    def __init__(self):
        _l_(76704)

        _n_(76702, "self", lambda: self).str1 = ''
        _l_(76703)

    def get_String(self):
        _l_(76709)

        _n_(76705, "self", lambda: self).str1 = _c_(76707, _n_(76706, "input", lambda: input))
        _l_(76708)

    def print_String(self):
        _l_(76717)

        _c_(76715, _n_(76710, "print", lambda: print), _c_(76714, _a_(76713, _a_(76712, _n_(76711, "self", lambda: self), "str1"), "upper")))
        _l_(76716)
_c_(76721, _a_(76720, _n_(76719, "str1", lambda: str1), "get_String"))
_l_(76722)
_c_(76725, _a_(76724, _n_(76723, "str1", lambda: str1), "print_String"))
_l_(76726)