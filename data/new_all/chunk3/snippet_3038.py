# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48221043/typeerror-not-supported-between-instances-of-str-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(576691)

except ImportError:
    pass
secret = _c_(576694, _a_(576693, _n_(576692, "random", lambda: random), "randint"), 1,99)
_l_(576695)
guess = 0
_l_(576696)
tries = 0
_l_(576697)
_c_(576699, _n_(576698, "print", lambda: print), " AHOY! I'm the Dead Pirate Roberts, and I have a secret!")
_l_(576700)
_c_(576702, _n_(576701, "print", lambda: print), "It is a number from 1 to 99. I'll give you 6 tries.")
_l_(576703)
while _n_(576704, "guess", lambda: guess) != _n_(576705, "secret", lambda: secret) and _n_(576706, "tries", lambda: tries) < 6:
    _l_(576724)

    guess = _c_(576708, _n_(576707, "input", lambda: input), "What's yer guess?")
    _l_(576709)
    if _n_(576710, "guess", lambda: guess) < _n_(576711, "secret", lambda: secret):
        _l_(576721)

        _c_(576713, _n_(576712, "print", lambda: print), "Too low, ye scurvy dog!")
        _l_(576714)
    elif _n_(576715, "guess", lambda: guess) > _n_(576716, "secret", lambda: secret):
        _l_(576720)

        _c_(576718, _n_(576717, "print", lambda: print), "Too high, landlubber!")
        _l_(576719)

    tries = _n_(576722, "tries", lambda: tries) + 1
    _l_(576723)

if _n_(576725, "guess", lambda: guess) == _n_(576726, "secret", lambda: secret):
    _l_(576737)

    _c_(576728, _n_(576727, "print", lambda: print), "Avast! Ye got it ! Found my secret, ye did!")
    _l_(576729)
else:
    _c_(576731, _n_(576730, "print", lambda: print), "No more guesses! Better luck next time, matey!")
    _l_(576732)
    _c_(576734, _n_(576733, "print", lambda: print), "The secret number was "), _n_(576735, "secret", lambda: secret)
    _l_(576736)