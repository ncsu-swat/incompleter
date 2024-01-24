# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# data hiding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Fruit:
    _l_(367781)

    __price = 0
    _l_(367772)

    def show(self):
        _l_(367780)

        _n_(367773, "self", lambda: self).__price += 1
        _l_(367774)
        _c_(367778, _n_(367775, "print", lambda: print), _a_(367777, _n_(367776, "self", lambda: self), "__price"))
        _l_(367779)

objFruit = _c_(367783, _n_(367782, "Fruit", lambda: Fruit))
_l_(367784)
_c_(367787, _a_(367786, _n_(367785, "objFruit", lambda: objFruit), "show"))
_l_(367788)
_c_(367791, _a_(367790, _n_(367789, "objFruit", lambda: objFruit), "show"))
_l_(367792)
_c_(367795, _a_(367794, _n_(367793, "objFruit", lambda: objFruit), "show"))
_l_(367796)
_c_(367801, _n_(367797, "print", lambda: print), _a_(367800, _a_(367799, _n_(367798, "objFruit", lambda: objFruit), "_Fruit"), "__price")) # error
_l_(367802) # error