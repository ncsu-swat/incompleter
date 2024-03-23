# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(74458)

except ImportError:
    pass

def max_min_list_tuples(class_students):
    _l_(74468)

    return_min = _c_(74463, _n_(74459, "min", lambda: min), _n_(74460, "class_students", lambda: class_students), key=_c_(74462, _n_(74461, "itemgetter", lambda: itemgetter), 1))[1]
    _l_(74464)
    aux = (_n_(74465, "return_max", lambda: return_max), _n_(74466, "return_min", lambda: return_min))
    _l_(74467)
    return aux
class_students = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
_l_(74469)
_c_(74471, _n_(74470, "print", lambda: print), 'Original list with tuples:')
_l_(74472)
_c_(74475, _n_(74473, "print", lambda: print), _n_(74474, "class_students", lambda: class_students))
_l_(74476)
_c_(74478, _n_(74477, "print", lambda: print), '\nMaximum and minimum values of the said list of tuples:')
_l_(74479)
_c_(74484, _n_(74480, "print", lambda: print), _c_(74483, _n_(74481, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(74482, "class_students", lambda: class_students)))
_l_(74485)