# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61396892/python-cant-use-base-abstract-calass-property-from-subclass-gettig-attributeerr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import abstractmethod, ABC
    _l_(538307)

except ImportError:
    pass
class Base(_n_(538308, "ABC", lambda: ABC)):
    _l_(538321)


    @_n_(538309, "property", lambda: property)
    def is_ver0(self):
        _l_(538311)

        aux = None
        _l_(538310)
        return aux

    @_n_(538312, "abstractmethod", lambda: abstractmethod)
    def execute_sql(self):
        _l_(538316)

        _c_(538314, _n_(538313, "print", lambda: print), "Base execute_sql")
        _l_(538315)

    def print_and_exit(self):
        _l_(538320)

        _c_(538318, _n_(538317, "print", lambda: print), "Base")
        _l_(538319)