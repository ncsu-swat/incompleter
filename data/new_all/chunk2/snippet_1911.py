# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37229359/money-and-typeerror-init-takes-from-1-to-2-positional-arguments-but-3-wer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from money import Money
    _l_(469287)

except ImportError:
    pass
class USD(_n_(469288, "Money", lambda: Money)):
    _l_(469295)

    def __init__(self, amount='0'):
        _l_(469294)

        _c_(469292, _a_(469290, _n_(469289, "super", lambda: super)(), "__init__"), amount=_n_(469291, "amount", lambda: amount), currency='USD')
        _l_(469293)
a = _c_(469297, _n_(469296, "Money", lambda: Money), 0,'USD')
_l_(469298)
b = _c_(469300, _n_(469299, "Money", lambda: Money), -360,'USD')
_l_(469301)
a += _n_(469302, "b", lambda: b)
_l_(469303)
_c_(469306, _n_(469304, "print", lambda: print), _n_(469305, "a", lambda: a))
_l_(469307)
c = _c_(469309, _n_(469308, "USD", lambda: USD), 0)
_l_(469310)
d = _c_(469312, _n_(469311, "USD", lambda: USD), -360)
_l_(469313)
c += _n_(469314, "d", lambda: d)
_l_(469315)
_c_(469318, _n_(469316, "print", lambda: print), _n_(469317, "c", lambda: c))
_l_(469319)