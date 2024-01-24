# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52434994/python-getting-attributeerror-electriccar-object-has-no-attribute-battery
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car:
    _l_(529298)

    def __init__(self, year, make, model):
        _l_(529257)

        _n_(529246, "self", lambda: self).year = _n_(529247, "year", lambda: year)
        _l_(529248)
        _n_(529249, "self", lambda: self).make = _n_(529250, "make", lambda: make)
        _l_(529251)
        _n_(529252, "self", lambda: self).model = _n_(529253, "model", lambda: model)
        _l_(529254)
        _n_(529255, "self", lambda: self).odometer_reading = 0
        _l_(529256)
    def get_descriptive_name(self):
        _l_(529275)

        long_name = _c_(529261, _n_(529258, "str", lambda: str), _a_(529260, _n_(529259, "self", lambda: self), "year")) + ' ' + _c_(529265, _n_(529262, "str", lambda: str), _a_(529264, _n_(529263, "self", lambda: self), "make")) + ' ' +_c_(529269, _n_(529266, "str", lambda: str), _a_(529268, _n_(529267, "self", lambda: self), "model"))
        _l_(529270)
        aux = _c_(529273, _a_(529272, _n_(529271, "long_name", lambda: long_name), "title"))
        _l_(529274)
        return aux
    def read_odometer(self):
        _l_(529283)

        _c_(529281, _n_(529276, "print", lambda: print), 'This car has ' + _c_(529280, _n_(529277, "str", lambda: str), _a_(529279, _n_(529278, "self", lambda: self), "odometer_reading")) + ' miles on it')
        _l_(529282)
    def update_odometer(self, mileage):
        _l_(529297)

        _n_(529284, "self", lambda: self).odometer_reading = _n_(529285, "mileage", lambda: mileage)
        _l_(529286)
        if _n_(529287, "mileage", lambda: mileage) >= _a_(529289, _n_(529288, "self", lambda: self), "odometer_reading"):
            _l_(529296)

            _n_(529290, "self", lambda: self).odometer_reading = _n_(529291, "mileage", lambda: mileage)
            _l_(529292)
        else:
            _c_(529294, _n_(529293, "print", lambda: print), 'you cant roll it back')
            _l_(529295)


class Battery():
    _l_(529312)

    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        _l_(529302)

        _n_(529299, "self", lambda: self).battery_size = _n_(529300, "battery_size", lambda: battery_size)
        _l_(529301)
    def describe_battery(self):
        _l_(529311)

        " ""Print a statement describing the battery size."""
        _l_(529303)
        _c_(529309, _n_(529304, "print", lambda: print), "This car has a " + _c_(529308, _n_(529305, "str", lambda: str), _a_(529307, _n_(529306, "self", lambda: self), "battery_size")) + "-kWh battery.")
        _l_(529310)

#The call to the battery attribute in the ElectricCar class is where the         
#error emanates
class ElectricCar(_n_(529313, "Car", lambda: Car)):
    _l_(529326)

    def __inti__(self, make, model, year):
        _l_(529325)

        _c_(529319, _a_(529315, _n_(529314, "super", lambda: super)(), "__init__"), _n_(529316, "make", lambda: make), _n_(529317, "model", lambda: model), _n_(529318, "year", lambda: year))
        _l_(529320)
        _n_(529321, "self", lambda: self).battery = _c_(529323, _n_(529322, "Battery", lambda: Battery))
        _l_(529324)


my_telsa = _c_(529328, _n_(529327, "ElectricCar", lambda: ElectricCar), 'Volvo', 'models s', 2006)
_l_(529329)
_c_(529334, _n_(529330, "print", lambda: print), _c_(529333, _a_(529332, _n_(529331, "my_telsa", lambda: my_telsa), "get_descriptive_name")))
_l_(529335)
_c_(529339, _a_(529338, _a_(529337, _n_(529336, "my_telsa", lambda: my_telsa), "battery"), "describe_battery"))
_l_(529340)