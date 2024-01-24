# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43403992/typeerror-not-supported-between-instances-of-list-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
_l_(401858)
alice = {
    "name": "Alice",
    "homework": [100.0, 97.0, 98.0, 100.0],
    "quizzes": [98.0, 99.0, 99.0],
    "tests": [100.0, 100.0]
}
_l_(401859)
tyler = {
    "name": "Tyler",
    "homework": [0.0, 35.0, 45.0, 22.0],
    "quizzes": [0.0, 60.0, 58.0],
    "tests": [65.0, 58.0]
}
_l_(401860)
students = [_n_(401861, "lloyd", lambda: lloyd),_n_(401862, "alice", lambda: alice),_n_(401863, "tyler", lambda: tyler)]
_l_(401864)
def average(numbers):
    _l_(401878)

    total= _c_(401867, _n_(401865, "sum", lambda: sum), _n_(401866, "numbers", lambda: numbers))
    _l_(401868)
    total = _c_(401871, _n_(401869, "float", lambda: float), _n_(401870, "total", lambda: total))
    _l_(401872)
    aux = _n_(401873, "total", lambda: total) / _c_(401876, _n_(401874, "len", lambda: len), _n_(401875, "numbers", lambda: numbers)) 
    _l_(401877) 
    return aux 

def get_average(student):
    _l_(401895)

    homework= _c_(401881, _n_(401879, "average", lambda: average), _n_(401880, "student", lambda: student)["homework"])
    _l_(401882)
    quizzes= _c_(401885, _n_(401883, "average", lambda: average), _n_(401884, "student", lambda: student)["quizzes"])
    _l_(401886)
    tests= _c_(401889, _n_(401887, "average", lambda: average), _n_(401888, "student", lambda: student)["tests"])
    _l_(401890)
    aux = 0.1 * _n_(401891, "homework", lambda: homework) + 0.3 * _n_(401892, "quizzes", lambda: quizzes) + 0.6 * _n_(401893, "tests", lambda: tests)
    _l_(401894)
    return aux

def get_letter_grade(score):
    _l_(401909)

    if _n_(401896, "score", lambda: score) >= 90:
        _l_(401908)

        aux = "A"
        _l_(401897)
        return aux
    elif _n_(401898, "score", lambda: score) >= 80:
        _l_(401907)

        aux = "B"
        _l_(401899)
        return aux
    elif _n_(401900, "score", lambda: score) >= 70:
        _l_(401906)

        aux = "C"
        _l_(401901)
        return aux
    elif _n_(401902, "score", lambda: score) >= 60:
        _l_(401905)

        aux = "D"
        _l_(401903)
        return aux
    else:
        aux = "F"
        _l_(401904)
        return aux

def get_student_average(gruppo):
    _l_(401934)

    for student in _n_(401910, "gruppo", lambda: gruppo):
        _l_(401933)

        results= []
        _l_(401911)
        _c_(401917, _a_(401913, _n_(401912, "results", lambda: results), "append"), _c_(401916, _n_(401914, "get_average", lambda: get_average), _n_(401915, "student", lambda: student)))
        _l_(401918)
        _c_(401921, _n_(401919, "print", lambda: print), _n_(401920, "student", lambda: student)["name"])
        _l_(401922)
        _c_(401925, _n_(401923, "print", lambda: print), _n_(401924, "results", lambda: results))
        _l_(401926)
        _c_(401931, _n_(401927, "print", lambda: print), _c_(401930, _n_(401928, "get_letter_grade", lambda: get_letter_grade), _n_(401929, "results", lambda: results)))
        _l_(401932)

_c_(401937, _n_(401935, "get_student_average", lambda: get_student_average), _n_(401936, "students", lambda: students))
_l_(401938)