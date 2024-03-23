# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(dictionary):
    _l_(71298)

    for key in _n_(71289, "dictionary", lambda: dictionary):
        _l_(71295)

        _c_(71293, _a_(71292, _n_(71290, "dictionary", lambda: dictionary)[_n_(71291, "key", lambda: key)], "clear"))
        _l_(71294)
    aux = _n_(71296, "dictionary", lambda: dictionary)
    _l_(71297)
    return aux
_c_(71300, _n_(71299, "print", lambda: print), '\nOriginal Dictionary:')
_l_(71301)
_c_(71304, _n_(71302, "print", lambda: print), _n_(71303, "dictionary", lambda: dictionary))
_l_(71305)
_c_(71307, _n_(71306, "print", lambda: print), '\nClear the list values in the said dictionary:')
_l_(71308)
_c_(71313, _n_(71309, "print", lambda: print), _c_(71312, _n_(71310, "test", lambda: test), _n_(71311, "dictionary", lambda: dictionary)))
_l_(71314)