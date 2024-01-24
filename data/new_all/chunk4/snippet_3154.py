# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68953459/attributeerror-str-object-has-no-attribute-describe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Computer:
    _l_(607118)


    def _inti_(self, storage, color , system):
        _l_(607107)

        no_of_Computer = 0
        _l_(607095)
        _n_(607096, "self", lambda: self).storage = _n_(607097, "storage", lambda: storage)
        _l_(607098)
        _n_(607099, "self", lambda: self).color = _n_(607100, "color", lambda: color)
        _l_(607101)
        _n_(607102, "self", lambda: self).system = _n_(607103, "system", lambda: system)
        _l_(607104)
        _n_(607105, "Computer", lambda: Computer).no_of_Computer +=1
        _l_(607106)

    def describe (self):
        _l_(607117)


        _c_(607115, _n_(607108, "print", lambda: print), f'my storage is {_a_(607110, _n_(607109, "self", lambda: self), "storage")} and my color is{_a_(607112, _n_(607111, "self", lambda: self), "color")} and my system is {_a_(607114, _n_(607113, "self", lambda: self), "system")}')
        _l_(607116)

Computer_1 = ("1TB ,  silver , windows ")
_l_(607119)

Computer_2 = (" 4TB , black , linux")
_l_(607120)

Computer_3 = (" 9TB , white ,mac ")
_l_(607121)

_c_(607124, _a_(607123, _n_(607122, 'Computer_1', lambda: Computer_1), 'describe'))
_l_(607125)