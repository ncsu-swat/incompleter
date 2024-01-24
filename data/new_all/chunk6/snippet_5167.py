# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68953459/attributeerror-str-object-has-no-attribute-describe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Computer:
    _l_(366302)


    def _inti_(self, storage, color , system):
        _l_(366291)

        no_of_Computer = 0
        _l_(366279)
        _n_(366280, "self", lambda: self).storage = _n_(366281, "storage", lambda: storage)
        _l_(366282)
        _n_(366283, "self", lambda: self).color = _n_(366284, "color", lambda: color)
        _l_(366285)
        _n_(366286, "self", lambda: self).system = _n_(366287, "system", lambda: system)
        _l_(366288)
        _n_(366289, "Computer", lambda: Computer).no_of_Computer +=1
        _l_(366290)

    def describe (self):
        _l_(366301)


        _c_(366299, _n_(366292, "print", lambda: print), f'my storage is {_a_(366294, _n_(366293, "self", lambda: self), "storage")} and my color is{_a_(366296, _n_(366295, "self", lambda: self), "color")} and my system is {_a_(366298, _n_(366297, "self", lambda: self), "system")}')
        _l_(366300)

Computer_1 = ("1TB ,  silver , windows ")
_l_(366303)

Computer_2 = (" 4TB , black , linux")
_l_(366304)

Computer_3 = (" 9TB , white ,mac ")
_l_(366305)

_c_(366308, _a_(366307, _n_(366306, 'Computer_1', lambda: Computer_1), 'describe'))
_l_(366309)