# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_sublists(input_list):
    _l_(106917)

    result = _c_(106913, _n_(106907, "sorted", lambda: sorted), _n_(106908, "input_list", lambda: input_list), key=lambda l: (_c_(106911, _n_(106909, "len", lambda: len), _n_(106910, "l", lambda: l)), _n_(106912, "l", lambda: l)))
    _l_(106914)
    aux = _n_(106915, "result", lambda: result)
    _l_(106916)
    return aux
_c_(106919, _n_(106918, "print", lambda: print), 'Original list:')
_l_(106920)
_c_(106923, _n_(106921, "print", lambda: print), _n_(106922, "list1", lambda: list1))
_l_(106924)
_c_(106926, _n_(106925, "print", lambda: print), '\nSort the list of lists by length and value:')
_l_(106927)
_c_(106932, _n_(106928, "print", lambda: print), _c_(106931, _n_(106929, "sort_sublists", lambda: sort_sublists), _n_(106930, "list1", lambda: list1)))
_l_(106933)