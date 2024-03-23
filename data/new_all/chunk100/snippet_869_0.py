# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def nested_dictionary(l1, l2, l3):
    _l_(85635)

    result = [{_n_(85624, "x", lambda: x): {_n_(85625, "y", lambda: y): _n_(85626, "z", lambda: z)}} for (x, y, z) in _c_(85631, _n_(85627, "zip", lambda: zip), _n_(85628, "l1", lambda: l1), _n_(85629, "l2", lambda: l2), _n_(85630, "l3", lambda: l3))]
    _l_(85632)
    aux = _n_(85633, "result", lambda: result)
    _l_(85634)
    return aux
student_id = ['S001', 'S002', 'S003', 'S004']
_l_(85636)
student_name = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
_l_(85637)
_c_(85639, _n_(85638, "print", lambda: print), 'Original strings:')
_l_(85640)
_c_(85643, _n_(85641, "print", lambda: print), _n_(85642, "student_id", lambda: student_id))
_l_(85644)
_c_(85647, _n_(85645, "print", lambda: print), _n_(85646, "student_name", lambda: student_name))
_l_(85648)
_c_(85651, _n_(85649, "print", lambda: print), _n_(85650, "student_grade", lambda: student_grade))
_l_(85652)
_c_(85654, _n_(85653, "print", lambda: print), '\nNested dictionary:')
_l_(85655)
ch = 'a'
_l_(85656)
_c_(85663, _n_(85657, "print", lambda: print), _c_(85662, _n_(85658, "nested_dictionary", lambda: nested_dictionary), _n_(85659, "student_id", lambda: student_id), _n_(85660, "student_name", lambda: student_name), _n_(85661, "student_grade", lambda: student_grade)))
_l_(85664)