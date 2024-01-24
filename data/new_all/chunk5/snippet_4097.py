# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62914304/attributeerror-car-object-has-no-attribute-describe-battery
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Car:
    _l_(656603)

    def __init__(self, make, model, year):
        _l_(656582)

        """Initialize attributes of car"""
        _n_(656573, "self", lambda: self).make = _n_(656574, "make", lambda: make)
        _l_(656575)
        _n_(656576, "self", lambda: self).model = _n_(656577, "model", lambda: model)
        _l_(656578)
        _n_(656579, "self", lambda: self).year = _n_(656580, "year", lambda: year)
        _l_(656581)
    
    def get_descriptive_name(self):
        _l_(656602)

        """Displaying car descriptive name"""
        _c_(656588, _n_(656583, "print", lambda: print), f"Car model : {_c_(656587, _a_(656586, _a_(656585, _n_(656584, 'self', lambda: self), 'model'), 'title'))}")
        _l_(656589)
        _c_(656593, _n_(656590, "print", lambda: print), f"Manufacture Date: {_a_(656592, _n_(656591, 'self', lambda: self), 'year')}")
        _l_(656594)
        _c_(656600, _n_(656595, "print", lambda: print), f"Car name : {_c_(656599, _a_(656598, _a_(656597, _n_(656596, 'self', lambda: self), 'make'), 'title'))}")
        _l_(656601)
class ElectricCar(_n_(656604, "Car", lambda: Car)):
    _l_(656621)

    def __init__(self, make, model, year):
        _l_(656614)

        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        _c_(656610, _a_(656606, _n_(656605, "super", lambda: super)(), "__init__"), _n_(656607, "make", lambda: make), _n_(656608, "model", lambda: model), _n_(656609, "year", lambda: year))
        _l_(656611)
        _n_(656612, "self", lambda: self).battery_size = 65
        _l_(656613)
    def describe_battery(self):
        _l_(656620)

        """Printing statement describing battert size """
        _c_(656618, _n_(656615, "print", lambda: print), f"Your car battery {_a_(656617, _n_(656616, 'self', lambda: self), 'battery_size')} kWh battery.")
        _l_(656619)

name = _c_(656623, _n_(656622, "Car", lambda: Car), 'tesla', 'tesla X78', 2021)
_l_(656624)
_c_(656629, _n_(656625, "print", lambda: print), _c_(656628, _a_(656627, _n_(656626, "name", lambda: name), "get_descriptive_name")))
_l_(656630)

_c_(656633, _a_(656632, _n_(656631, "name", lambda: name), "describe_battery"))
_l_(656634)