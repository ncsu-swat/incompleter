# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44138754/python-3-error-typeerror-unsupported-operand-types-for-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Billy = {
  'Homework':[76, 88, 90, 95, 54],
  'Quiz':[89, 97, 54],
  'Test':[78, 89]
}
_l_(620753)

Martha = {
  'Homework':[74, 66, 90, 100, 98],
  'Quiz':[67, 80, 99],
  'Test':[88, 98]
}
_l_(620754)

Robert = {
  'Homework':[89, 76, 65, 99, 87],
  'Quiz':[88, 98, 73],
  'Test':[81, 92]
}
_l_(620755)

#Sum
def grades_sum(homework):
    _l_(620763)

    total = 0
    _l_(620756)
    for grade in _n_(620757, "homework", lambda: homework):
        _l_(620760)

        total += _n_(620758, "grade", lambda: grade)
        _l_(620759)
    aux = _n_(620761, "total", lambda: total)
    _l_(620762)
    return aux

_c_(620768, _n_(620764, "print", lambda: print), _c_(620767, _n_(620765, "grades_sum", lambda: grades_sum), _n_(620766, "Billy", lambda: Billy)))
_l_(620769)

#Average
def grades_average(grades):
    _l_(620783)

    sum_of_grades = _c_(620772, _n_(620770, "grades_sum", lambda: grades_sum), _n_(620771, "grades", lambda: grades))
    _l_(620773)
    average = _n_(620774, "sum_of_grades", lambda: sum_of_grades) / _c_(620779, _n_(620775, "float", lambda: float), _c_(620778, _n_(620776, "len", lambda: len), _n_(620777, "grades", lambda: grades)))
    _l_(620780)
    aux = _n_(620781, "average", lambda: average)
    _l_(620782)
    return aux