# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def nested_dictionary(l1, l2, l3):
    _l_(85791)

    result = [{_n_(85780, "x", lambda: x): {_n_(85781, "y", lambda: y): _n_(85782, "z", lambda: z)}} for (x, y, z) in _c_(85787, _n_(85783, "zip", lambda: zip), _n_(85784, "l1", lambda: l1), _n_(85785, "l2", lambda: l2), _n_(85786, "l3", lambda: l3))]
    _l_(85788)
    aux = _n_(85789, "result", lambda: result)
    _l_(85790)
    return aux
student_id = ['S001', 'S002', 'S003', 'S004']
_l_(85792)
student_grade = [85, 98, 89, 92]
_l_(85793)
_c_(85795, _n_(85794, "print", lambda: print), 'Original strings:')
_l_(85796)
_c_(85799, _n_(85797, "print", lambda: print), _n_(85798, "student_id", lambda: student_id))
_l_(85800)
_c_(85803, _n_(85801, "print", lambda: print), _n_(85802, "student_name", lambda: student_name))
_l_(85804)
_c_(85807, _n_(85805, "print", lambda: print), _n_(85806, "student_grade", lambda: student_grade))
_l_(85808)
_c_(85810, _n_(85809, "print", lambda: print), '\nNested dictionary:')
_l_(85811)
ch = 'a'
_l_(85812)
_c_(85819, _n_(85813, "print", lambda: print), _c_(85818, _n_(85814, "nested_dictionary", lambda: nested_dictionary), _n_(85815, "student_id", lambda: student_id), _n_(85816, "student_name", lambda: student_name), _n_(85817, "student_grade", lambda: student_grade)))
_l_(85820)