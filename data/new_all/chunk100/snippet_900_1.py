# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(88233)

    result = []
    _l_(88219)
    for i in _n_(88220, "lst", lambda: lst):
        _l_(88230)

        j = _c_(88223, _a_(88222, _n_(88221, "i", lambda: i), "replace"), ' ', '')
        _l_(88224)
        _c_(88228, _a_(88226, _n_(88225, "result", lambda: result), "append"), _n_(88227, "j", lambda: j))
        _l_(88229)
    aux = _n_(88231, "result", lambda: result)
    _l_(88232)
    return aux
_c_(88235, _n_(88234, "print", lambda: print), '\nOriginal list:')
_l_(88236)
_c_(88239, _n_(88237, "print", lambda: print), _n_(88238, "text", lambda: text))
_l_(88240)
_c_(88242, _n_(88241, "print", lambda: print), 'Remove additional spaces from the said list:')
_l_(88243)
_c_(88248, _n_(88244, "print", lambda: print), _c_(88247, _n_(88245, "test", lambda: test), _n_(88246, "text", lambda: text)))
_l_(88249)