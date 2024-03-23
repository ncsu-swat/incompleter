# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(74521)

except ImportError:
    pass

def max_min_list_tuples(class_students):
    _l_(74531)

    return_max = _c_(74526, _n_(74522, "max", lambda: max), _n_(74523, "class_students", lambda: class_students), key=_c_(74525, _n_(74524, "itemgetter", lambda: itemgetter), 1))[1]
    _l_(74527)
    aux = (_n_(74528, "return_max", lambda: return_max), _n_(74529, "return_min", lambda: return_min))
    _l_(74530)
    return aux
class_students = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
_l_(74532)
_c_(74534, _n_(74533, "print", lambda: print), 'Original list with tuples:')
_l_(74535)
_c_(74538, _n_(74536, "print", lambda: print), _n_(74537, "class_students", lambda: class_students))
_l_(74539)
_c_(74541, _n_(74540, "print", lambda: print), '\nMaximum and minimum values of the said list of tuples:')
_l_(74542)
_c_(74547, _n_(74543, "print", lambda: print), _c_(74546, _n_(74544, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(74545, "class_students", lambda: class_students)))
_l_(74548)