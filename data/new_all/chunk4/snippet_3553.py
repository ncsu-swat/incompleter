# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from CustomExceptions import InvalidAge
    _l_(580121)

except ImportError:
    pass

class Person:
    _l_(580177)

    def __init__(self, name, address, age):
        _l_(580166)

        _n_(580122, "self", lambda: self)._name = _n_(580123, "name", lambda: name)
        _l_(580124)
        _n_(580125, "self", lambda: self)._address = _n_(580126, "address", lambda: address)
        _l_(580127)
        _c_(580131, _a_(580129, _n_(580128, "self", lambda: self), "set_age"), _n_(580130, "age", lambda: age))
        _l_(580132)

        # getter and setter methods for the various properties
        def get_name(self):
            _l_(580136)

            aux = _a_(580134, _n_(580133, "self", lambda: self), "_name")
            _l_(580135)
            return aux

        def set_name(self, name):
            _l_(580140)

            _n_(580137, "self", lambda: self)._name = _n_(580138, "name", lambda: name)
            _l_(580139)

        def get_address(self):
            _l_(580144)

            aux = _a_(580142, _n_(580141, "self", lambda: self), "_address")
            _l_(580143)
            return aux

        def set_address(self, address):
            _l_(580148)

            _n_(580145, "self", lambda: self)._address = _n_(580146, "address", lambda: address)
            _l_(580147)

        def get_age(self):
            _l_(580152)

            aux = _a_(580150, _n_(580149, "self", lambda: self), "_age")
            _l_(580151)
            return aux

        def set_age(self, age):
            _l_(580165)

            MIN_AGE = 0
            _l_(580153)
            MAX_AGE = 120
            _l_(580154)

            if _n_(580155, "age", lambda: age) >= _n_(580156, "MIN_AGE", lambda: MIN_AGE) and _n_(580157, "age", lambda: age) <= _n_(580158, "MAX_AGE", lambda: MAX_AGE):
                _l_(580164)

                _n_(580159, "self", lambda: self)._age = _n_(580160, "age", lambda: age)
                _l_(580161)
            else:
                raise _n_(580162, "InvalidAge", lambda: InvalidAge)
                _l_(580163)

    # instance method
    def to_string(self):
        _l_(580176)

        aux = "Name: " + _a_(580168, _n_(580167, "self", lambda: self), "_name") + " Address: " + _a_(580170, _n_(580169, "self", lambda: self), "_address") + " Age: " + _c_(580174, _n_(580171, "str", lambda: str), _a_(580173, _n_(580172, "self", lambda: self), "_age"))
        _l_(580175)
        return aux