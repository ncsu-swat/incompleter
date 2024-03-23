# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def nested_dictionary(l1, l2, l3):
    _l_(85750)

    result = [{_n_(85739, "x", lambda: x): {_n_(85740, "y", lambda: y): _n_(85741, "z", lambda: z)}} for (x, y, z) in _c_(85746, _n_(85742, "zip", lambda: zip), _n_(85743, "l1", lambda: l1), _n_(85744, "l2", lambda: l2), _n_(85745, "l3", lambda: l3))]
    _l_(85747)
    aux = _n_(85748, "result", lambda: result)
    _l_(85749)
    return aux
student_id = ['S001', 'S002', 'S003', 'S004']
_l_(85751)
student_name = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
_l_(85752)
student_grade = [85, 98, 89, 92]
_l_(85753)
_c_(85755, _n_(85754, "print", lambda: print), 'Original strings:')
_l_(85756)
_c_(85759, _n_(85757, "print", lambda: print), _n_(85758, "student_id", lambda: student_id))
_l_(85760)
_c_(85763, _n_(85761, "print", lambda: print), _n_(85762, "student_name", lambda: student_name))
_l_(85764)
_c_(85767, _n_(85765, "print", lambda: print), _n_(85766, "student_grade", lambda: student_grade))
_l_(85768)
_c_(85770, _n_(85769, "print", lambda: print), '\nNested dictionary:')
_l_(85771)
_c_(85778, _n_(85772, "print", lambda: print), _c_(85777, _n_(85773, "nested_dictionary", lambda: nested_dictionary), _n_(85774, "student_id", lambda: student_id), _n_(85775, "student_name", lambda: student_name), _n_(85776, "student_grade", lambda: student_grade)))
_l_(85779)