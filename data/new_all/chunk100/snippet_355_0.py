# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def string_test(s):
    _l_(35240)

    for c in _n_(35213, "s", lambda: s):
        _l_(35227)

        if _c_(35216, _a_(35215, _n_(35214, "c", lambda: c), "isupper")):
            _l_(35226)

            _n_(35217, "d", lambda: d)['UPPER_CASE'] += 1
            _l_(35218)
        elif _c_(35221, _a_(35220, _n_(35219, "c", lambda: c), "islower")):
            _l_(35225)

            _n_(35222, "d", lambda: d)['LOWER_CASE'] += 1
            _l_(35223)
        else:
            pass
            _l_(35224)
    _c_(35230, _n_(35228, "print", lambda: print), 'Original String : ', _n_(35229, "s", lambda: s))
    _l_(35231)
    _c_(35234, _n_(35232, "print", lambda: print), 'No. of Upper case characters : ', _n_(35233, "d", lambda: d)['UPPER_CASE'])
    _l_(35235)
    _c_(35238, _n_(35236, "print", lambda: print), 'No. of Lower case Characters : ', _n_(35237, "d", lambda: d)['LOWER_CASE'])
    _l_(35239)
_c_(35242, _n_(35241, "string_test", lambda: string_test), 'The quick Brown Fox')
_l_(35243)