# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(str1):
    _l_(114132)

    messg = [lambda str1: _c_(114100, _n_(114095, "any", lambda: any), (_c_(114098, _a_(114097, _n_(114096, "x", lambda: x), "isupper")) for x in _n_(114099, "str1", lambda: str1))) or 'String must have 1 upper case character.', lambda str1: _c_(114106, _n_(114101, "any", lambda: any), (_c_(114104, _a_(114103, _n_(114102, "x", lambda: x), "islower")) for x in _n_(114105, "str1", lambda: str1))) or 'String must have 1 lower case character.', lambda str1: _c_(114112, _n_(114107, "any", lambda: any), (_c_(114110, _a_(114109, _n_(114108, "x", lambda: x), "isdigit")) for x in _n_(114111, "str1", lambda: str1))) or 'String must have 1 number.', lambda str1: _c_(114115, _n_(114113, "len", lambda: len), _n_(114114, "str1", lambda: str1)) >= 7 or 'String length should be atleast 8.']
    _l_(114116)
    result = [_n_(114117, "x", lambda: x) for x in [_c_(114120, _n_(114118, "i", lambda: i), _n_(114119, "str1", lambda: str1)) for i in _n_(114121, "messg", lambda: messg)] if _n_(114122, "x", lambda: x) != True]
    _l_(114123)
    if not _n_(114124, "result", lambda: result):
        _l_(114129)

        _c_(114127, _a_(114126, _n_(114125, "result", lambda: result), "append"), 'Valid string.')
        _l_(114128)
    aux = _n_(114130, "result", lambda: result)
    _l_(114131)
    return aux
_c_(114137, _n_(114133, "print", lambda: print), _c_(114136, _n_(114134, "check_string", lambda: check_string), _n_(114135, "s", lambda: s)))
_l_(114138)