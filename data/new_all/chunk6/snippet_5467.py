# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36368878/this-is-the-error-i-get-after-making-the-following-code-typeerror-unorderable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
            import random
            _l_(340966)

except ImportError:
            pass
SecretNumber=_a_(340968, _n_(340967, "random", lambda: random), "randint")
_l_(340969)

Guess=_c_(340971, _n_(340970, "input", lambda: input), "Please enter your guess: ")
_l_(340972)
NumberofGuesses=1
_l_(340973)

while _n_(340974, "Guess", lambda: Guess) != _n_(340975, "SecretNumber", lambda: SecretNumber):
            _l_(340987)

            NumberofGuesses=_n_(340976, "NumberofGuesses", lambda: NumberofGuesses)+1
            _l_(340977)


            if _n_(340978, "Guess", lambda: Guess)>_n_(340979, "SecretNumber", lambda: SecretNumber):
                        _l_(340986)

                        _c_(340981, _n_(340980, "print", lambda: print), "Please insert a smaller number")
                        _l_(340982)

            else:
               _c_(340984, _n_(340983, "print", lambda: print), "Please insert a bigger number")
               _l_(340985)

_c_(340992, _n_(340988, "print", lambda: print), _c_(340991, _a_(340989, "Number of Guesses: {0}", "format"), _n_(340990, "NumberofGuesses", lambda: NumberofGuesses)))
_l_(340993)