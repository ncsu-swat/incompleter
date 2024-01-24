# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45000350/getting-attributeerror-during-instantiation-of-subclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Keyword(_n_(444152, "Cipher", lambda: Cipher)):
    _l_(444188)

    converted_string = []
    _l_(444153)

    def __init__(self, secret_string, *args, **kwargs):
        _l_(444167)

        if _c_(444157, _n_(444154, "len", lambda: len), _a_(444156, _n_(444155, "self", lambda: self), "secret_string")) < 1:
            _l_(444161)

            raise _c_(444159, _n_(444158, "ValueError", lambda: ValueError), "Secret string cannot be empty")
            _l_(444160)
        _c_(444165, _a_(444163, _n_(444162, "super", lambda: super)(), "__init__"), _n_(444164, "secret_string", lambda: secret_string))
        _l_(444166)

    @_n_(444168, "property", lambda: property)
    def convert_to_keyword_string(self):
        _l_(444187)

        for num in _a_(444170, _n_(444169, "self", lambda: self), "secret_numbers"):
            _l_(444183)

            for k, v in _a_(444172, _n_(444171, "self", lambda: self), "orig_dict"):
                _l_(444182)

                if _n_(444173, "num", lambda: num) == _n_(444174, "v", lambda: v):
                    _l_(444181)

                    _c_(444179, _a_(444177, _a_(444176, _n_(444175, "self", lambda: self), "converted_string"), "append"), _n_(444178, "k", lambda: k))
                    _l_(444180)
        aux = _a_(444185, _n_(444184, "self", lambda: self), "converted_string")
        _l_(444186)
        return aux