# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61291553/getting-type-errorobject-of-type-nonetype-has-no-len-and-it-also-not-print
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse(seq):
    _l_(350398)

    k=_c_(350380, _n_(350378, "len", lambda: len), _n_(350379, "seq", lambda: seq))
    _l_(350381)

    for i in _c_(350384, _n_(350382, "range", lambda: range), 0,_n_(350383, "k", lambda: k)):
        _l_(350393)

        _c_(350391, _a_(350386, _n_(350385, "seq", lambda: seq), "append"), _c_(350390, _a_(350388, _n_(350387, "seq", lambda: seq), "pop"), _n_(350389, "i", lambda: i)))
        _l_(350392)
    _c_(350396, _n_(350394, "print", lambda: print), _n_(350395, "seq", lambda: seq))
    _l_(350397)
_c_(350402, _n_(350399, "reverse", lambda: reverse), _c_(350401, _n_(350400, "reverse", lambda: reverse), [1,2,3,4,5]))
_l_(350403)