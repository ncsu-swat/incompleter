# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51636107/why-does-the-below-code-throw-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car:
    _l_(575813)

    def __init__(self, mileage, make, model):
        _l_(575804)

        _n_(575795, "self", lambda: self).mileage = _n_(575796, "mileage", lambda: mileage)
        _l_(575797)
        _n_(575798, "self", lambda: self).make = _n_(575799, "make", lambda: make)
        _l_(575800)
        _n_(575801, "self", lambda: self).model = _n_(575802, "model", lambda: model)
        _l_(575803)

    def printCar(self):
        _l_(575812)

        aux = "The Model is:" + _a_(575806, _n_(575805, "self", lambda: self), "model") + " the make is: " + _a_(575808, _n_(575807, "self", lambda: self), "make") + " and the mileage is: " + _a_(575810, _n_(575809, "self", lambda: self), "mileage")
        _l_(575811)
        return aux


car = _c_(575815, _n_(575814, "Car", lambda: Car), 100, 'Suzuki', 'Brezza')
_l_(575816)

_c_(575821, _n_(575817, "print", lambda: print), _c_(575820, _a_(575819, _n_(575818, "car", lambda: car), "printCar")))
_l_(575822)