# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_strings_list(string_list):
    _l_(17220)

    result = _c_(17216, _n_(17207, "list", lambda: list), _c_(17215, _n_(17208, "map", lambda: map), lambda x: _c_(17213, _a_(17209, '', "join"), _c_(17212, _n_(17210, "reversed", lambda: reversed), _n_(17211, "x", lambda: x))), _n_(17214, "string_list", lambda: string_list)))
    _l_(17217)
    aux = _n_(17218, "result", lambda: result)
    _l_(17219)
    return aux
_c_(17222, _n_(17221, "print", lambda: print), '\nOriginal lists:')
_l_(17223)
_c_(17226, _n_(17224, "print", lambda: print), _n_(17225, "colors_list", lambda: colors_list))
_l_(17227)
_c_(17229, _n_(17228, "print", lambda: print), '\nReverse strings of the said given list:')
_l_(17230)
_c_(17235, _n_(17231, "print", lambda: print), _c_(17234, _n_(17232, "reverse_strings_list", lambda: reverse_strings_list), _n_(17233, "colors_list", lambda: colors_list)))
_l_(17236)