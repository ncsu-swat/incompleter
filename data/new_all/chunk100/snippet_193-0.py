# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(104255)

    aux = _c_(104245, _n_(104243, "list", lambda: list), _n_(104244, "val", lambda: val)) if _c_(104252, _n_(104246, "isinstance", lambda: isinstance), _n_(104247, "val", lambda: val), (_n_(104248, "tuple", lambda: tuple), _n_(104249, "list", lambda: list), _n_(104250, "set", lambda: set), _n_(104251, "dict", lambda: dict))) else [_n_(104253, "val", lambda: val)]
    _l_(104254)
    return aux
_c_(104260, _n_(104256, "print", lambda: print), _c_(104259, _n_(104257, "type", lambda: type), _n_(104258, "d1", lambda: d1)))
_l_(104261)
_c_(104266, _n_(104262, "print", lambda: print), _c_(104265, _n_(104263, "cast_list", lambda: cast_list), _n_(104264, "d1", lambda: d1)))
_l_(104267)
d2 = ('Red', 'Green')
_l_(104268)
_c_(104273, _n_(104269, "print", lambda: print), _c_(104272, _n_(104270, "type", lambda: type), _n_(104271, "d2", lambda: d2)))
_l_(104274)
_c_(104279, _n_(104275, "print", lambda: print), _c_(104278, _n_(104276, "cast_list", lambda: cast_list), _n_(104277, "d2", lambda: d2)))
_l_(104280)
d3 = {'Red', 'Green'}
_l_(104281)
_c_(104286, _n_(104282, "print", lambda: print), _c_(104285, _n_(104283, "type", lambda: type), _n_(104284, "d3", lambda: d3)))
_l_(104287)
_c_(104292, _n_(104288, "print", lambda: print), _c_(104291, _n_(104289, "cast_list", lambda: cast_list), _n_(104290, "d3", lambda: d3)))
_l_(104293)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(104294)
_c_(104299, _n_(104295, "print", lambda: print), _c_(104298, _n_(104296, "type", lambda: type), _n_(104297, "d4", lambda: d4)))
_l_(104300)
_c_(104305, _n_(104301, "print", lambda: print), _c_(104304, _n_(104302, "cast_list", lambda: cast_list), _n_(104303, "d4", lambda: d4)))
_l_(104306)