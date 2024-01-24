# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31162350/attributeerror-unsupported-operand-types-for-nonetype-and-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Attendancename(_a_(531201, _n_(531200, "models", lambda: models), "Model")):
    _l_(531230)

    teacher_name = _c_(531203, _a_(531202, models, "ForeignKey"), Teachername)
    _l_(531204)
    date = _c_(531206, _a_(531205, models, "DateField"), 'Date')
    _l_(531207)
    intime = _c_(531209, _a_(531208, models, "DateTimeField"), 'IN-TIME')
    _l_(531210)
    outtime = _c_(531212, _a_(531211, models, "DateTimeField"), 'OUT-TIME')
    _l_(531213)

    def hours_calculate(self):
        _l_(531225)

        tdelta = _a_(531215, _n_(531214, "self", lambda: self), "outtime") - _a_(531217, _n_(531216, "self", lambda: self), "intime")
        _l_(531218)
        tdelta = _c_(531221, _n_(531219, "float", lambda: float), _n_(531220, "tdelta", lambda: tdelta))/3600
        _l_(531222)
        aux = _n_(531223, "tdelta", lambda: tdelta)
        _l_(531224)
        return aux
    def __str__(self):
        _l_(531229)

        aux = "%s" %_a_(531227, _n_(531226, "self", lambda: self), "teacher_name")
        _l_(531228)
        return aux