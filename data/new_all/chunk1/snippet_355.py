# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62523278/typeerror-field-classroom-expected-a-number-but-got-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
students = [
    ["James", "Smith", 4, 10],
    # more students here
]
_l_(380873)

for s in _n_(380874, "students", lambda: students):
    _l_(380894)

    student = _c_(380876, _n_(380875, "Student", lambda: Student))
    _l_(380877)
    _n_(380878, "student", lambda: student).first_name = _n_(380879, "s", lambda: s)[0],
    _l_(380880)
    _n_(380881, "student", lambda: student).last_name = _n_(380882, "s", lambda: s)[1],
    _l_(380883)
    _n_(380884, "student", lambda: student).classroom = _n_(380885, "s", lambda: s)[2],
    _l_(380886)
    _n_(380887, "student", lambda: student).grade1 = _n_(380888, "s", lambda: s)[3],
    _l_(380889)
    _c_(380892, _a_(380891, _n_(380890, "student", lambda: student), "save"))
    _l_(380893)