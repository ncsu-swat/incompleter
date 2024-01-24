# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45269822/getting-error-in-python-3-x-typeerror-int-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car():
    _l_(637430)

    def __init__(self, make, model, year):
        _l_(637407)

        _n_(637396, "self", lambda: self).make = _n_(637397, "make", lambda: make)
        _l_(637398)
        _n_(637399, "self", lambda: self).model = _n_(637400, "model", lambda: model)
        _l_(637401)
        _n_(637402, "self", lambda: self).year = _n_(637403, "year", lambda: year)
        _l_(637404)
        _n_(637405, "self", lambda: self).odometer_reading = 0
        _l_(637406)

    def get_descriptive_name(self):
        _l_(637421)

        car_name = _c_(637411, _n_(637408, "str", lambda: str), _a_(637410, _n_(637409, "self", lambda: self), "year")) + ' ' + _a_(637413, _n_(637412, "self", lambda: self), "make") + ' ' + _a_(637415, _n_(637414, "self", lambda: self), "model") + 'model.'
        _l_(637416)
        aux = _c_(637419, _a_(637418, _n_(637417, "car_name", lambda: car_name), "title"))
        _l_(637420)
        return aux
    def read_odometer(self):
        _l_(637429)

        _c_(637427, _n_(637422, "print", lambda: print), "This car has " + _c_(637426, _n_(637423, "str", lambda: str), _a_(637425, _n_(637424, "self", lambda: self), "odometer_reading")) + " miles on it.")
        _l_(637428)

my_dream_car = _c_(637432, _n_(637431, "Car", lambda: Car), 'lamborghini', 'one-off', 2017 )
_l_(637433)
_c_(637438, _n_(637434, "print", lambda: print), "\nMy dream car is " + _c_(637437, _a_(637436, _n_(637435, "my_dream_car", lambda: my_dream_car), "get_descriptive_name")))
_l_(637439)
_n_(637440, "my_dream_car", lambda: my_dream_car).odometer_reading = 23
_l_(637441)
_c_(637444, _a_(637443, _n_(637442, "my_dream_car", lambda: my_dream_car), "odometer_reading"))
_l_(637445)