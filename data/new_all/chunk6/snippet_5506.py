# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69221111/my-code-keeps-coming-up-with-an-error-attributeerror-student-object-has-no-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Student import Student
    _l_(344168)

except ImportError:
    pass

student1 = _c_(344170, _n_(344169, "Student", lambda: Student), "Oscar", "Accounting", 3.1)
_l_(344171)
student2 = _c_(344173, _n_(344172, "Student", lambda: Student), "Phyllis", "Business", 3.8)
_l_(344174)

_c_(344179, _n_(344175, "print", lambda: print), _c_(344178, _a_(344177, _n_(344176, "student1", lambda: student1), "on_honor_roll")))
_l_(344180)

class Student:
    _l_(344197)

    def __init__(self, name,  major, gpa):
        _l_(344196)

        _n_(344181, "self", lambda: self).name = _n_(344182, "name", lambda: name)
        _l_(344183)
        _n_(344184, "self", lambda: self).major = _n_(344185, "major", lambda: major)
        _l_(344186)
        _n_(344187, "self", lambda: self).gpa = _n_(344188, "gpa", lambda: gpa)
        _l_(344189)

        def on_honor_roll(self):
            _l_(344195)

            if _a_(344191, _n_(344190, "self", lambda: self), "gpa") >= 3.5:
                _l_(344194)

                aux = True
                _l_(344192)
                return aux
            else:
                aux = False
                _l_(344193)
                return aux