# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(88201)

    result = []
    _l_(88191)
    for i in _n_(88192, "lst", lambda: lst):
        _l_(88198)

        _c_(88196, _a_(88194, _n_(88193, "result", lambda: result), "append"), _n_(88195, "j", lambda: j))
        _l_(88197)
    aux = _n_(88199, "result", lambda: result)
    _l_(88200)
    return aux
text = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']
_l_(88202)
_c_(88204, _n_(88203, "print", lambda: print), '\nOriginal list:')
_l_(88205)
_c_(88208, _n_(88206, "print", lambda: print), _n_(88207, "text", lambda: text))
_l_(88209)
_c_(88211, _n_(88210, "print", lambda: print), 'Remove additional spaces from the said list:')
_l_(88212)
_c_(88217, _n_(88213, "print", lambda: print), _c_(88216, _n_(88214, "test", lambda: test), _n_(88215, "text", lambda: text)))
_l_(88218)