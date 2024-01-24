# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46505037/typeerror-cant-instantiate-abstract-class-with-abstract-methods
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import ABC
    _l_(386142)

except ImportError:
    pass
try:
    from abc import abstractmethod
    _l_(386144)

except ImportError:
    pass

class Mamifiero(_n_(386145, "ABC", lambda: ABC)):
    _l_(386154)

    """docstring for Mamifiero"""
    def __init__(self):
        _l_(386148)

        _n_(386146, "self", lambda: self).alimentacion = 'carnivoro'
        _l_(386147)
    
    @_n_(386149, "abstractmethod", lambda: abstractmethod)
    def __respirar(self):
        _l_(386153)

        _c_(386151, _n_(386150, "print", lambda: print), 'inhalar... exhalar')
        _l_(386152)
class Perro(_n_(386155, "Mamifiero", lambda: Mamifiero)):
    _l_(386160)

    """docstring for Perro"""
    def __init__(self, ojos=2,):
        _l_(386159)

        _n_(386156, "self", lambda: self).ojos = _n_(386157, "ojos", lambda: ojos)
        _l_(386158)