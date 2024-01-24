# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68641918/attributeerror-character-object-has-no-attribute-set-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from Classes.character import character
  _l_(631620)

except ImportError:
  pass
try:
  from functions.yesorno import _yesorno
  _l_(631622)

except ImportError:
  pass
#character
char = _c_(631624, _n_(631623, "character", lambda: character))
_l_(631625)
while True:
  _l_(631648)

  _c_(631627, _n_(631626, "print", lambda: print), "please enter a name for your character")
  _l_(631628)
  _c_(631633, _a_(631630, _n_(631629, "char", lambda: char), "set_name"), _c_(631632, _n_(631631, "input", lambda: input)))
  _l_(631634)
  _c_(631638, _n_(631635, "print", lambda: print), "Your name is: " + _a_(631637, _n_(631636, "char", lambda: char), "name") + ". Are you happy with your choice? Type 'y' for yes, 'n' for no.")
  _l_(631639)
  if _c_(631643, _n_(631640, "_yesorno", lambda: _yesorno), _c_(631642, _n_(631641, "input", lambda: input))):
    _l_(631647)

    break
    _l_(631644)
  else:
    _n_(631645, "next", lambda: next)
    _l_(631646)