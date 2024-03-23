# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_sublists(input_list):
    _l_(19509)

    result = _c_(19505, _n_(19499, "sorted", lambda: sorted), _n_(19500, "input_list", lambda: input_list), key=lambda l: (_c_(19503, _n_(19501, "len", lambda: len), _n_(19502, "l", lambda: l)), _n_(19504, "l", lambda: l)))
    _l_(19506)
    aux = _n_(19507, "result", lambda: result)
    _l_(19508)
    return aux
_c_(19511, _n_(19510, "print", lambda: print), 'Original list:')
_l_(19512)
_c_(19515, _n_(19513, "print", lambda: print), _n_(19514, "list1", lambda: list1))
_l_(19516)
_c_(19518, _n_(19517, "print", lambda: print), '\nSort the list of lists by length and value:')
_l_(19519)
_c_(19524, _n_(19520, "print", lambda: print), _c_(19523, _n_(19521, "sort_sublists", lambda: sort_sublists), _n_(19522, "list1", lambda: list1)))
_l_(19525)