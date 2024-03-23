# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(str1):
    _l_(38864)

    messg = [lambda str1: _c_(38832, _n_(38827, "any", lambda: any), (_c_(38830, _a_(38829, _n_(38828, "x", lambda: x), "isupper")) for x in _n_(38831, "str1", lambda: str1))) or 'String must have 1 upper case character.', lambda str1: _c_(38838, _n_(38833, "any", lambda: any), (_c_(38836, _a_(38835, _n_(38834, "x", lambda: x), "islower")) for x in _n_(38837, "str1", lambda: str1))) or 'String must have 1 lower case character.', lambda str1: _c_(38844, _n_(38839, "any", lambda: any), (_c_(38842, _a_(38841, _n_(38840, "x", lambda: x), "isdigit")) for x in _n_(38843, "str1", lambda: str1))) or 'String must have 1 number.', lambda str1: _c_(38847, _n_(38845, "len", lambda: len), _n_(38846, "str1", lambda: str1)) >= 7 or 'String length should be atleast 8.']
    _l_(38848)
    result = [_n_(38849, "x", lambda: x) for x in [_c_(38852, _n_(38850, "i", lambda: i), _n_(38851, "str1", lambda: str1)) for i in _n_(38853, "messg", lambda: messg)] if _n_(38854, "x", lambda: x) != True]
    _l_(38855)
    if not _n_(38856, "result", lambda: result):
        _l_(38861)

        _c_(38859, _a_(38858, _n_(38857, "result", lambda: result), "append"), 'Valid string.')
        _l_(38860)
    aux = _n_(38862, "result", lambda: result)
    _l_(38863)
    return aux
_c_(38869, _n_(38865, "print", lambda: print), _c_(38868, _n_(38866, "check_string", lambda: check_string), _n_(38867, "s", lambda: s)))
_l_(38870)