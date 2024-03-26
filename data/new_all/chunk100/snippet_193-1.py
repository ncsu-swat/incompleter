# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(104319)

    aux = _c_(104309, _n_(104307, "list", lambda: list), _n_(104308, "val", lambda: val)) if _c_(104316, _n_(104310, "isinstance", lambda: isinstance), _n_(104311, "val", lambda: val), (_n_(104312, "tuple", lambda: tuple), _n_(104313, "list", lambda: list), _n_(104314, "set", lambda: set), _n_(104315, "dict", lambda: dict))) else [_n_(104317, "val", lambda: val)]
    _l_(104318)
    return aux
d1 = [1]
_l_(104320)
_c_(104325, _n_(104321, "print", lambda: print), _c_(104324, _n_(104322, "type", lambda: type), _n_(104323, "d1", lambda: d1)))
_l_(104326)
_c_(104331, _n_(104327, "print", lambda: print), _c_(104330, _n_(104328, "cast_list", lambda: cast_list), _n_(104329, "d1", lambda: d1)))
_l_(104332)
d2 = ('Red', 'Green')
_l_(104333)
_c_(104338, _n_(104334, "print", lambda: print), _c_(104337, _n_(104335, "type", lambda: type), _n_(104336, "d2", lambda: d2)))
_l_(104339)
_c_(104344, _n_(104340, "print", lambda: print), _c_(104343, _n_(104341, "cast_list", lambda: cast_list), _n_(104342, "d2", lambda: d2)))
_l_(104345)
d3 = {'Red', 'Green'}
_l_(104346)
_c_(104351, _n_(104347, "print", lambda: print), _c_(104350, _n_(104348, "type", lambda: type), _n_(104349, "d3", lambda: d3)))
_l_(104352)
_c_(104357, _n_(104353, "print", lambda: print), _c_(104356, _n_(104354, "cast_list", lambda: cast_list), _n_(104355, "d3", lambda: d3)))
_l_(104358)
_c_(104363, _n_(104359, "print", lambda: print), _c_(104362, _n_(104360, "type", lambda: type), _n_(104361, "d4", lambda: d4)))
_l_(104364)
_c_(104369, _n_(104365, "print", lambda: print), _c_(104368, _n_(104366, "cast_list", lambda: cast_list), _n_(104367, "d4", lambda: d4)))
_l_(104370)