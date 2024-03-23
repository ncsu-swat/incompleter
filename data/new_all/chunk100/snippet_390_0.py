# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(str1):
    _l_(38817)

    messg = [lambda str1: _c_(38792, _n_(38787, "any", lambda: any), (_c_(38790, _a_(38789, _n_(38788, "x", lambda: x), "isupper")) for x in _n_(38791, "str1", lambda: str1))) or 'String must have 1 upper case character.', lambda str1: _c_(38798, _n_(38793, "any", lambda: any), (_c_(38796, _a_(38795, _n_(38794, "x", lambda: x), "islower")) for x in _n_(38797, "str1", lambda: str1))) or 'String must have 1 lower case character.', lambda str1: _c_(38804, _n_(38799, "any", lambda: any), (_c_(38802, _a_(38801, _n_(38800, "x", lambda: x), "isdigit")) for x in _n_(38803, "str1", lambda: str1))) or 'String must have 1 number.', lambda str1: _c_(38807, _n_(38805, "len", lambda: len), _n_(38806, "str1", lambda: str1)) >= 7 or 'String length should be atleast 8.']
    _l_(38808)
    if not _n_(38809, "result", lambda: result):
        _l_(38814)

        _c_(38812, _a_(38811, _n_(38810, "result", lambda: result), "append"), 'Valid string.')
        _l_(38813)
    aux = _n_(38815, "result", lambda: result)
    _l_(38816)
    return aux
s = _c_(38819, _n_(38818, "input", lambda: input), 'Input the string: ')
_l_(38820)
_c_(38825, _n_(38821, "print", lambda: print), _c_(38824, _n_(38822, "check_string", lambda: check_string), _n_(38823, "s", lambda: s)))
_l_(38826)