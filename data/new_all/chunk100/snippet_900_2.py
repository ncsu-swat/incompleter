# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(88263)

    for i in _n_(88250, "lst", lambda: lst):
        _l_(88260)

        j = _c_(88253, _a_(88252, _n_(88251, "i", lambda: i), "replace"), ' ', '')
        _l_(88254)
        _c_(88258, _a_(88256, _n_(88255, "result", lambda: result), "append"), _n_(88257, "j", lambda: j))
        _l_(88259)
    aux = _n_(88261, "result", lambda: result)
    _l_(88262)
    return aux
text = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']
_l_(88264)
_c_(88266, _n_(88265, "print", lambda: print), '\nOriginal list:')
_l_(88267)
_c_(88270, _n_(88268, "print", lambda: print), _n_(88269, "text", lambda: text))
_l_(88271)
_c_(88273, _n_(88272, "print", lambda: print), 'Remove additional spaces from the said list:')
_l_(88274)
_c_(88279, _n_(88275, "print", lambda: print), _c_(88278, _n_(88276, "test", lambda: test), _n_(88277, "text", lambda: text)))
_l_(88280)