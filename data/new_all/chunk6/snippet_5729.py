# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# data hiding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Fruit:
    _l_(358429)

    __price = 0
    _l_(358420)

    def show(self):
        _l_(358428)

        _n_(358421, "self", lambda: self).__price += 1
        _l_(358422)
        _c_(358426, _n_(358423, "print", lambda: print), _a_(358425, _n_(358424, "self", lambda: self), "__price"))
        _l_(358427)

objFruit = _c_(358431, _n_(358430, "Fruit", lambda: Fruit))
_l_(358432)
_c_(358435, _a_(358434, _n_(358433, "objFruit", lambda: objFruit), "show"))
_l_(358436)
_c_(358439, _a_(358438, _n_(358437, "objFruit", lambda: objFruit), "show"))
_l_(358440)
_c_(358443, _a_(358442, _n_(358441, "objFruit", lambda: objFruit), "show"))
_l_(358444)
_c_(358449, _n_(358445, "print", lambda: print), _a_(358448, _a_(358447, _n_(358446, "objFruit", lambda: objFruit), "_Fruit"), "__price")) # error
_l_(358450) # error