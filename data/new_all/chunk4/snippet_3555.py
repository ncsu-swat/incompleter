# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from CustomExceptions import InvalidPlayerNumException
    _l_(628887)

except ImportError:
    pass

class Player:
    _l_(628930)

    # custom constructor. Constructors are named __init__()
    def __init__(self, name, number):
        _l_(628896)

        # set the attributes
        # note the single underscore _ before the variable name makes them protected
        _n_(628888, "self", lambda: self)._name = _n_(628889, "name", lambda: name)
        _l_(628890)
        _c_(628894, _a_(628892, _n_(628891, "self", lambda: self), "set_number"), _n_(628893, "number", lambda: number)) # note we call the setter method here
        _l_(628895) # note we call the setter method here


    # getter and setter methods for the various properties
    def get_name(self):
        _l_(628900)

        aux = _a_(628898, _n_(628897, "self", lambda: self), "_name")
        _l_(628899)
        return aux

    def set_name(self, name):
        _l_(628904)

        _n_(628901, "self", lambda: self)._name = _n_(628902, "name", lambda: name)
        _l_(628903)

    def get_number(self):
        _l_(628908)

        aux = _a_(628906, _n_(628905, "self", lambda: self), "_number")
        _l_(628907)
        return aux

    def set_number(self, number):
        _l_(628921)

        MIN_NUMBER = 1
        _l_(628909)
        MAX_NUMBER = 999
        _l_(628910)

        # Add validation to make sure number is in the expected range
        if _n_(628911, "number", lambda: number) >= _n_(628912, "MIN_NUMBER", lambda: MIN_NUMBER) and _n_(628913, "number", lambda: number) <= _n_(628914, "MAX_NUMBER", lambda: MAX_NUMBER):
            _l_(628920)

            _n_(628915, "self", lambda: self)._number = _n_(628916, "number", lambda: number)
            _l_(628917)
        else:
            # instead of setting player number to MIN_NUMBER, raise an exception
            #self._number = MIN_NUMBER # original code
            raise _n_(628918, "InvalidPlayerNumException", lambda: InvalidPlayerNumException)
            _l_(628919)


    # instance method
    def to_string(self):
        _l_(628929)

        aux = "Name: " + _a_(628923, _n_(628922, "self", lambda: self), "_name") + " Number: " + _c_(628927, _n_(628924, "str", lambda: str), _a_(628926, _n_(628925, "self", lambda: self), "_number"))
        _l_(628928)
        return aux