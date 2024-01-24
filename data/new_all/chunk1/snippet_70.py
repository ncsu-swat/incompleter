# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/8120019/typeerror-float-object-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count=7
_l_(380949)
for i in _n_(380950, "count", lambda: count):
    _l_(380965)

    num = _c_(380954, _n_(380951, "float", lambda: float), _c_(380953, _n_(380952, "input", lambda: input), "Type a number, any number:"))
    _l_(380955)
    if _n_(380956, "num", lambda: num) == 0:
        _l_(380964)

        zero+=1
        _l_(380957)
    elif _n_(380958, "num", lambda: num) > 0:
        _l_(380963)

        positive+=1
        _l_(380959)
    elif _n_(380960, "num", lambda: num) < 0:
        _l_(380962)

        negative+=1
        _l_(380961)

_c_(380968, _n_(380966, "print", lambda: print), _n_(380967, "positive", lambda: positive))
_l_(380969)
_c_(380972, _n_(380970, "print", lambda: print), _n_(380971, "negative", lambda: negative))
_l_(380973)
_c_(380976, _n_(380974, "print", lambda: print), _n_(380975, "zero", lambda: zero))
_l_(380977)