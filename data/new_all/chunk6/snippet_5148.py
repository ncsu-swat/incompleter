# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69014725/why-is-self-age-showing-attribute-error-whilst-the-use-of-only-age-in-condition
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class student_list:
    _l_(367190)

    class_membership=True
    _l_(367164)
    def __init__(self,name,age,miles):
        _l_(367177)

        if _a_(367166, _n_(367165, "self", lambda: self), "age")>=18:
            _l_(367176)

            _n_(367167, "self", lambda: self).name=_n_(367168, "name", lambda: name)
            _l_(367169)
            _n_(367170, "self", lambda: self).age=_n_(367171, "age", lambda: age)
            _l_(367172)
            _n_(367173, "self", lambda: self).miles=_n_(367174, "miles", lambda: miles)
            _l_(367175)

    def run(self):
        _l_(367183)

        _c_(367181, _n_(367178, "print", lambda: print), f'I ran {_a_(367180, _n_(367179, "self", lambda: self), "miles")}')
        _l_(367182)

    def name_1(self):
        _l_(367189)

        _c_(367187, _n_(367184, 'print', lambda: print), f'Hi my name is {_a_(367186, _n_(367185, "self", lambda: self), "name")}')
        _l_(367188)

player_1=_c_(367192, _n_(367191, 'student_list', lambda: student_list), 'Tom Ellis',20,20)
_l_(367193)
_c_(367197, _n_(367194, 'print', lambda: print), _a_(367196, _n_(367195, 'player_1', lambda: player_1), 'name'))
_l_(367198)
_c_(367202, _n_(367199, 'print', lambda: print), _a_(367201, _n_(367200, 'player_1', lambda: player_1), 'age'))
_l_(367203)