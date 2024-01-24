# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61524254/what-is-wrong-here-why-is-it-showing-type-error-when-it-shouldnt-be
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class student :
    _l_(355083)

    def __init__(self,name,age,grade):
        _l_(355078)

        _n_(355069, "self", lambda: self).name = _n_(355070, "name", lambda: name)
        _l_(355071)
        _n_(355072, "self", lambda: self).age = _n_(355073, "age", lambda: age)
        _l_(355074)
        _n_(355075, "self", lambda: self).grade = _n_(355076, "grade", lambda: grade)   # 0 - 100
        _l_(355077)   # 0 - 100

    def get_grade(self):
        _l_(355082)

        aux = _a_(355080, _n_(355079, "self", lambda: self), "grade")
        _l_(355081)
        return aux

class Course :
    _l_(355124)

    def __init__(self, name, max_students):
        _l_(355092)

        _n_(355084, "self", lambda: self).name = _n_(355085, "name", lambda: name)
        _l_(355086)
        _n_(355087, "self", lambda: self).max_students = _n_(355088, "max_students", lambda: max_students)
        _l_(355089)
        _n_(355090, "self", lambda: self).students = []
        _l_(355091)

    def add_student(self, student):
        _l_(355108)

        if _c_(355096, _n_(355093, "len", lambda: len), _a_(355095, _n_(355094, "self", lambda: self), "students")) < _a_(355098, _n_(355097, "self", lambda: self), "max_students") :
            _l_(355106)

            _c_(355103, _a_(355101, _a_(355100, _n_(355099, "self", lambda: self), "students"), "append"), _n_(355102, "student", lambda: student))
            _l_(355104)
            aux = True
            _l_(355105)
            return aux
        aux = False
        _l_(355107)
        return aux
    def get_average_grade(self):
        _l_(355123)

        value = 0
        _l_(355109)
        for i in _a_(355111, _n_(355110, "self", lambda: self), "students") :
            _l_(355116)

            value += _c_(355114, _a_(355113, _n_(355112, "student", lambda: student), "get_grade")) # this part had the error
            _l_(355115) # this part had the error
        aux = _n_(355117, "value", lambda: value) / _c_(355121, _n_(355118, "len", lambda: len), _a_(355120, _n_(355119, "self", lambda: self), "students"))
        _l_(355122)

        return aux

s1 = _c_(355126, _n_(355125, "student", lambda: student), 'Bob', 12, 50)
_l_(355127)
s2 = _c_(355129, _n_(355128, "student", lambda: student), 'Joe', 12, 60)
_l_(355130)
s3 = _c_(355132, _n_(355131, "student", lambda: student), 'Sadie', 12, 100)
_l_(355133)

Course1 = _c_(355135, _n_(355134, "Course", lambda: Course), 'Chemistry', 5)
_l_(355136)
_c_(355140, _a_(355138, _n_(355137, "Course1", lambda: Course1), "add_student"), _n_(355139, "s1", lambda: s1))
_l_(355141)
_c_(355145, _a_(355143, _n_(355142, "Course1", lambda: Course1), "add_student"), _n_(355144, "s2", lambda: s2))
_l_(355146)
_c_(355150, _a_(355148, _n_(355147, "Course1", lambda: Course1), "add_student"), _n_(355149, "s3", lambda: s3))
_l_(355151)
_c_(355156, _n_(355152, "print", lambda: print), _a_(355155, _a_(355154, _n_(355153, "Course1", lambda: Course1), "students")[0], "name"))
_l_(355157)
_c_(355162, _n_(355158, "print", lambda: print), _c_(355161, _a_(355160, _n_(355159, "Course1", lambda: Course1), "get_average_grade")))
_l_(355163)