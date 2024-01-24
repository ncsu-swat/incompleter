# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62463683/instances-as-attributes-trying-to-make-a-class-an-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Battery():
    _l_(698294)

    """Model batter for a electric car"""
    def __init__(self,battery_size = 70):
        _l_(698285)

        _n_(698282, "self", lambda: self).battery_size = _n_(698283, "battery_size", lambda: battery_size)
        _l_(698284)
    def describe_battery(self):
        _l_(698293)

        """print statement about battery size"""
        _c_(698291, _n_(698286, "print", lambda: print), "This car has a " + _c_(698290, _n_(698287, "str", lambda: str), _a_(698289, _n_(698288, "self", lambda: self), "battery_size")) + "-kWh battery.")
        _l_(698292)
class ElectricCar(_n_(698295, "Car", lambda: Car)):
    _l_(698308)

    """Represent a electric car"""
    def __init___(self,make,model,year):
        _l_(698307)

        """
        Initialize attributes of the parent class,
        then initialize attributes specific to electric car
        """
        _c_(698301, _a_(698297, _n_(698296, "super", lambda: super)(), "__init__"), _n_(698298, "make", lambda: make),_n_(698299, "model", lambda: model),_n_(698300, "year", lambda: year))
        _l_(698302)
        _n_(698303, "self", lambda: self).battery = _c_(698305, _n_(698304, "Battery", lambda: Battery))
        _l_(698306)

new_tesla = _c_(698310, _n_(698309, "ElectricCar", lambda: ElectricCar), 'Big tesla',"model Z",'2020')
_l_(698311)
_c_(698315, _a_(698314, _a_(698313, _n_(698312, "new_tesla", lambda: new_tesla), "battery"), "describe_battery"))
_l_(698316)