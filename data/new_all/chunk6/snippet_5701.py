# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48912755/nameerror-name-guessestaken-is-not-defined-issue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import random
  _l_(337013)

except ImportError:
  pass

def Loop():
  _l_(337015)


  guessesTaken = 0
  _l_(337014)

_c_(337017, _n_(337016, "print", lambda: print), 'Hello! What is your name?')
_l_(337018)
myName = _c_(337020, _n_(337019, "input", lambda: input))
_l_(337021)

number = _c_(337024, _a_(337023, _n_(337022, "random", lambda: random), "randint"), 1, 100)
_l_(337025)
_c_(337028, _n_(337026, "print", lambda: print), 'Hi, ' + _n_(337027, "myName", lambda: myName) + ', I am thinking of a number between 1 and 100.')
_l_(337029)

mod = _n_(337030, "number", lambda: number) % 2
_l_(337031)
if _n_(337032, "mod", lambda: mod) > 0:
  _l_(337039)

  _c_(337034, _n_(337033, "print", lambda: print), "The number I am thinking of is odd.")
  _l_(337035)
else:
    _c_(337037, _n_(337036, "print", lambda: print), "The number I am thinking of is even.")
    _l_(337038)


while _n_(337040, "guessesTaken", lambda: guessesTaken) < 10:
  _l_(337080)

  _c_(337042, _n_(337041, "print", lambda: print), 'Take a guess.')
  _l_(337043)
  guess = _c_(337045, _n_(337044, "input", lambda: input))
  _l_(337046)
  guess = _c_(337049, _n_(337047, "int", lambda: int), _n_(337048, "guess", lambda: guess))
  _l_(337050)

  guessesTaken = _n_(337051, "guessesTaken", lambda: guessesTaken) + 1
  _l_(337052)

  if _n_(337053, "guess", lambda: guess) < _n_(337054, "number", lambda: number):
    _l_(337058)

    _c_(337056, _n_(337055, "print", lambda: print), 'Your guess is too low.') 
    _l_(337057) 

  if _n_(337059, "guess", lambda: guess) > _n_(337060, "number", lambda: number):
    _l_(337068)

    _c_(337062, _n_(337061, "print", lambda: print), 'Your guess is too high.')
    _l_(337063)
    if _n_(337064, "guess", lambda: guess) == _n_(337065, "number", lambda: number):
      _l_(337067)

      break
      _l_(337066)

  if _n_(337069, "guess", lambda: guess) == _n_(337070, "number", lambda: number):
    _l_(337079)

    _c_(337076, _n_(337071, "print", lambda: print), 'Good job, ' + _n_(337072, "myName", lambda: myName) + '! You guessed my number in ' + _c_(337075, _n_(337073, "str", lambda: str), _n_(337074, "guessesTaken", lambda: guessesTaken)) + ' guesses!')
    _l_(337077)
    guessesTaken = 10
    _l_(337078)




if _n_(337081, "guess", lambda: guess) != _n_(337082, "number", lambda: number):
  _l_(337105)

  _c_(337087, _n_(337083, "print", lambda: print), 'Nope. The number I was thinking of was ' + _c_(337086, _n_(337084, "str", lambda: str), _n_(337085, "number", lambda: number)))
  _l_(337088)

  playagain = _c_(337090, _n_(337089, "input", lambda: input), 'Would you like to play again')
  _l_(337091)
  if _n_(337092, "playagain", lambda: playagain) == "yes":
    _l_(337096)

    _c_(337094, _n_(337093, "Loop", lambda: Loop))
    _l_(337095)
  if _n_(337097, "playagain", lambda: playagain) == "no":
    _l_(337104)

    _c_(337099, _n_(337098, "print", lambda: print), 'Goodbye :)')
    _l_(337100)
    _c_(337102, _n_(337101, "Loop", lambda: Loop))
    _l_(337103)