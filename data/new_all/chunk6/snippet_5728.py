# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# metaclass methods

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Meta(_n_(365313, "type", lambda: type)):
    _l_(365316)

    def show(cls):
        _l_(365315)

        aux = 'I am a Meta class method'
        _l_(365314)
        return aux

class Mistake(_n_(365317, "object", lambda: object)):
    _l_(365320)

    __metaclass__ = _n_(365318, "Meta", lambda: Meta)
    _l_(365319)