# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69014725/why-is-self-age-showing-attribute-error-whilst-the-use-of-only-age-in-condition
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class student_list:
    _l_(354110)

    class_membership=True
    _l_(354084)
    def __init__(self,name,age,miles):
        _l_(354097)

        if _a_(354086, _n_(354085, "self", lambda: self), "age")>=18:
            _l_(354096)

            _n_(354087, "self", lambda: self).name=_n_(354088, "name", lambda: name)
            _l_(354089)
            _n_(354090, "self", lambda: self).age=_n_(354091, "age", lambda: age)
            _l_(354092)
            _n_(354093, "self", lambda: self).miles=_n_(354094, "miles", lambda: miles)
            _l_(354095)

    def run(self):
        _l_(354103)

        _c_(354101, _n_(354098, "print", lambda: print), f'I ran {_a_(354100, _n_(354099, "self", lambda: self), "miles")}')
        _l_(354102)

    def name_1(self):
        _l_(354109)

        _c_(354107, _n_(354104, 'print', lambda: print), f'Hi my name is {_a_(354106, _n_(354105, "self", lambda: self), "name")}')
        _l_(354108)

player_1=_c_(354112, _n_(354111, 'student_list', lambda: student_list), 'Tom Ellis',20,20)
_l_(354113)
_c_(354117, _n_(354114, 'print', lambda: print), _a_(354116, _n_(354115, 'player_1', lambda: player_1), 'name'))
_l_(354118)
_c_(354122, _n_(354119, 'print', lambda: print), _a_(354121, _n_(354120, 'player_1', lambda: player_1), 'age'))
_l_(354123)