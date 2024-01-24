# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# metaclass methods

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Meta(_n_(374759, "type", lambda: type)):
    _l_(374762)

    def show(cls):
        _l_(374761)

        aux = 'I am a Meta class method'
        _l_(374760)
        return aux

class Mistake(_n_(374763, "object", lambda: object)):
    _l_(374766)

    __metaclass__ = _n_(374764, "Meta", lambda: Meta)
    _l_(374765)