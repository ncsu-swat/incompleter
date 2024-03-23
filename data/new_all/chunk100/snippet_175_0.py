# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(12414)

    max_length = _c_(12402, _n_(12397, "max", lambda: max), (_c_(12400, _n_(12398, "len", lambda: len), _n_(12399, "x", lambda: x)) for x in _n_(12401, "input_list", lambda: input_list)))
    _l_(12403)
    max_list = _c_(12409, _n_(12404, "max", lambda: max), _n_(12405, "input_list", lambda: input_list), key=lambda i: _c_(12408, _n_(12406, "len", lambda: len), _n_(12407, "i", lambda: i)))
    _l_(12410)
    aux = (_n_(12411, "max_length", lambda: max_length), _n_(12412, "max_list", lambda: max_list))
    _l_(12413)
    return aux

def min_length_list(input_list):
    _l_(12425)

    min_length = _c_(12420, _n_(12415, "min", lambda: min), (_c_(12418, _n_(12416, "len", lambda: len), _n_(12417, "x", lambda: x)) for x in _n_(12419, "input_list", lambda: input_list)))
    _l_(12421)
    aux = (_n_(12422, "min_length", lambda: min_length), _n_(12423, "min_list", lambda: min_list))
    _l_(12424)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(12426)
_c_(12428, _n_(12427, "print", lambda: print), 'Original list:')
_l_(12429)
_c_(12432, _n_(12430, "print", lambda: print), _n_(12431, "list1", lambda: list1))
_l_(12433)
_c_(12435, _n_(12434, "print", lambda: print), '\nList with maximum length of lists:')
_l_(12436)
_c_(12441, _n_(12437, "print", lambda: print), _c_(12440, _n_(12438, "max_length_list", lambda: max_length_list), _n_(12439, "list1", lambda: list1)))
_l_(12442)
_c_(12444, _n_(12443, "print", lambda: print), '\nList with minimum length of lists:')
_l_(12445)
_c_(12450, _n_(12446, "print", lambda: print), _c_(12449, _n_(12447, "min_length_list", lambda: min_length_list), _n_(12448, "list1", lambda: list1)))
_l_(12451)