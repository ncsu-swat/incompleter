# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def nested_dictionary(l1, l2, l3):
    _l_(85709)

    result = [{_n_(85698, "x", lambda: x): {_n_(85699, "y", lambda: y): _n_(85700, "z", lambda: z)}} for (x, y, z) in _c_(85705, _n_(85701, "zip", lambda: zip), _n_(85702, "l1", lambda: l1), _n_(85703, "l2", lambda: l2), _n_(85704, "l3", lambda: l3))]
    _l_(85706)
    aux = _n_(85707, "result", lambda: result)
    _l_(85708)
    return aux
student_name = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
_l_(85710)
student_grade = [85, 98, 89, 92]
_l_(85711)
_c_(85713, _n_(85712, "print", lambda: print), 'Original strings:')
_l_(85714)
_c_(85717, _n_(85715, "print", lambda: print), _n_(85716, "student_id", lambda: student_id))
_l_(85718)
_c_(85721, _n_(85719, "print", lambda: print), _n_(85720, "student_name", lambda: student_name))
_l_(85722)
_c_(85725, _n_(85723, "print", lambda: print), _n_(85724, "student_grade", lambda: student_grade))
_l_(85726)
_c_(85728, _n_(85727, "print", lambda: print), '\nNested dictionary:')
_l_(85729)
ch = 'a'
_l_(85730)
_c_(85737, _n_(85731, "print", lambda: print), _c_(85736, _n_(85732, "nested_dictionary", lambda: nested_dictionary), _n_(85733, "student_id", lambda: student_id), _n_(85734, "student_name", lambda: student_name), _n_(85735, "student_grade", lambda: student_grade)))
_l_(85738)