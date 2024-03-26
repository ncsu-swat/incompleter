# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(class_students):
    _l_(111663)

    return_max = _c_(111653, _n_(111650, "max", lambda: max), _n_(111651, "class_students", lambda: class_students), key=lambda item: _n_(111652, "item", lambda: item)[1])[1]
    _l_(111654)
    return_min = _c_(111658, _n_(111655, "min", lambda: min), _n_(111656, "class_students", lambda: class_students), key=lambda item: _n_(111657, "item", lambda: item)[1])[1]
    _l_(111659)
    aux = (_n_(111660, "return_max", lambda: return_max), _n_(111661, "return_min", lambda: return_min))
    _l_(111662)
    return aux
_c_(111665, _n_(111664, "print", lambda: print), 'Original list with tuples:')
_l_(111666)
_c_(111669, _n_(111667, "print", lambda: print), _n_(111668, "class_students", lambda: class_students))
_l_(111670)
_c_(111672, _n_(111671, "print", lambda: print), '\nMaximum and minimum values of the said list of tuples:')
_l_(111673)
_c_(111678, _n_(111674, "print", lambda: print), _c_(111677, _n_(111675, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(111676, "class_students", lambda: class_students)))
_l_(111679)