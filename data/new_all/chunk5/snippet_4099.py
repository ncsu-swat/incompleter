# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62914304/attributeerror-car-object-has-no-attribute-describe-battery
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car:
    _l_(668266)

    def __init__(self, make, model, year):
        _l_(668245)

        """Initialize attributes of car"""
        _n_(668236, "self", lambda: self).make = _n_(668237, "make", lambda: make)
        _l_(668238)
        _n_(668239, "self", lambda: self).model = _n_(668240, "model", lambda: model)
        _l_(668241)
        _n_(668242, "self", lambda: self).year = _n_(668243, "year", lambda: year)
        _l_(668244)
    
    def get_descriptive_name(self):
        _l_(668265)

        """Displaying car descriptive name"""
        _c_(668251, _n_(668246, "print", lambda: print), f"Car model : {_c_(668250, _a_(668249, _a_(668248, _n_(668247, 'self', lambda: self), 'model'), 'title'))}")
        _l_(668252)
        _c_(668256, _n_(668253, "print", lambda: print), f"Manufacture Date: {_a_(668255, _n_(668254, 'self', lambda: self), 'year')}")
        _l_(668257)
        _c_(668263, _n_(668258, "print", lambda: print), f"Car name : {_c_(668262, _a_(668261, _a_(668260, _n_(668259, 'self', lambda: self), 'make'), 'title'))}")
        _l_(668264)
class ElectricCar(_n_(668267, "Car", lambda: Car)):
    _l_(668284)

    def __init__(self, make, model, year):
        _l_(668277)

        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        _c_(668273, _a_(668269, _n_(668268, "super", lambda: super)(), "__init__"), _n_(668270, "make", lambda: make), _n_(668271, "model", lambda: model), _n_(668272, "year", lambda: year))
        _l_(668274)
        _n_(668275, "self", lambda: self).battery_size = 65
        _l_(668276)
    def describe_battery(self):
        _l_(668283)

        """Printing statement describing battert size """
        _c_(668281, _n_(668278, "print", lambda: print), f"Your car battery {_a_(668280, _n_(668279, 'self', lambda: self), 'battery_size')} kWh battery.")
        _l_(668282)

name = _c_(668286, _n_(668285, "Car", lambda: Car), 'tesla', 'tesla X78', 2021)
_l_(668287)
_c_(668292, _n_(668288, "print", lambda: print), _c_(668291, _a_(668290, _n_(668289, "name", lambda: name), "get_descriptive_name")))
_l_(668293)

_c_(668296, _a_(668295, _n_(668294, "name", lambda: name), "describe_battery"))
_l_(668297)