# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
count = 0
_l_(1538569)
while True:
    _l_(1538601)

    count += 1
    _l_(1538570)
    if _n_(1538571, "count", lambda: count) > 3:
        _l_(1538600)

        break
        _l_(1538572)
    else:
        try:
            _l_(1538599)

            x = _c_(1538576, _n_(1538573, "int", lambda: int), _c_(1538575, _n_(1538574, "input", lambda: input), "Enter your lock number here: "))
            _l_(1538577)

            if _n_(1538578, "x", lambda: x) == 586:
                _l_(1538587)

                _c_(1538580, _n_(1538579, "print", lambda: print), "Your lock has unlocked :)")
                _l_(1538581)

                break
                _l_(1538582)
            else:
                _c_(1538584, _n_(1538583, "print", lambda: print), "Try again!!")
                _l_(1538585)

                continue
                _l_(1538586)

        except:
            _l_(1538591)

            _c_(1538589, _n_(1538588, "print", lambda: print), "Invalid entry!!")
            _l_(1538590)
        finally:
            _l_(1538598)

            _c_(1538596, _n_(1538592, "print", lambda: print), _c_(1538595, _a_(1538593, "Your Attempts: {}", "format"), _n_(1538594, "count", lambda: count)))
            _l_(1538597)

count = 0
_l_(1538602)

while True:
    _l_(1538633)

    count += 1
    _l_(1538603)
    if _n_(1538604, "count", lambda: count) > 3:
        _l_(1538632)

        break
        _l_(1538605)
    else:
        try:
            _l_(1538625)

            x = _c_(1538609, _n_(1538606, "int", lambda: int), _c_(1538608, _n_(1538607, "input", lambda: input), "Enter your lock number here: "))
            _l_(1538610)

            if _n_(1538611, "x", lambda: x) == 586:
                _l_(1538620)

                _c_(1538613, _n_(1538612, "print", lambda: print), "Your lock has unlocked :)")
                _l_(1538614)

                break
                _l_(1538615)
            else:
                _c_(1538617, _n_(1538616, "print", lambda: print), "Try again!!")
                _l_(1538618)

                continue
                _l_(1538619)

        except:
            _l_(1538624)

            _c_(1538622, _n_(1538621, "print", lambda: print), "Invalid entry!!")
            _l_(1538623)

        _c_(1538630, _n_(1538626, "print", lambda: print), _c_(1538629, _a_(1538627, "Your Attempts: {}", "format"), _n_(1538628, "count", lambda: count)))
        _l_(1538631)

