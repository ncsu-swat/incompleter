# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38994825/typeerror-unsupported-operand-types-for-or-pow-int-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
play = True
_l_(646590)

while _n_(646591, "play", lambda: play):
    _l_(646627)


    x = _c_(646593, _n_(646592, "input", lambda: input), "Enter a number: ")
    _l_(646594)
    y = _c_(646596, _n_(646595, "input", lambda: input), "Enter a number: ")
    _l_(646597)

    _c_(646601, _n_(646598, "print", lambda: print), _n_(646599, "x", lambda: x) + _n_(646600, "y", lambda: y))
    _l_(646602)
    _c_(646606, _n_(646603, "print", lambda: print), _n_(646604, "x", lambda: x) - _n_(646605, "y", lambda: y))
    _l_(646607)
    _c_(646611, _n_(646608, "print", lambda: print), _n_(646609, "x", lambda: x) * _n_(646610, "y", lambda: y))
    _l_(646612)
    _c_(646616, _n_(646613, "print", lambda: print), _n_(646614, "x", lambda: x) / _n_(646615, "y", lambda: y))
    _l_(646617)
    _c_(646621, _n_(646618, "print", lambda: print), _n_(646619, "x", lambda: x) % _n_(646620, "y", lambda: y))
    _l_(646622)

    if _c_(646624, _n_(646623, "input", lambda: input), "Play again? ") == "no":
        _l_(646626)

        play = False
        _l_(646625)