# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64691365/name-error-in-one-program-whereas-syntax-error-in-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Z = _c_(334823, _n_(334822, "input", lambda: input), "Enter a character: ")
_l_(334824)
if _c_(334827, _n_(334825, "type", lambda: type), _n_(334826, "Z", lambda: Z)) == _n_(334828, "int", lambda: int):
   _l_(334852)

   _c_(334831, _n_(334829, "print", lambda: print), _n_(334830, "Z", lambda: Z), "is a numeral")
   _l_(334832)
else: 
   if (_n_(334833, "Z", lambda: Z)=='A' or _n_(334834, "Z", lambda: Z)=='a' or _n_(334835, "Z", lambda: Z) =='E' or _n_(334836, "Z", lambda: Z)=='e' or _n_(334837, "Z", lambda: Z)=='I'or _n_(334838, "Z", lambda: Z)=='i'
        or _n_(334839, "Z", lambda: Z)=='O' or _n_(334840, "Z", lambda: Z)=='o' or _n_(334841, "Z", lambda: Z)=='U' or _n_(334842, "Z", lambda: Z)=='u'):
      _l_(334851)

      _c_(334845, _n_(334843, "print", lambda: print), _n_(334844, "Z", lambda: Z), "is a Vowel")
      _l_(334846)
   else:
      _c_(334849, _n_(334847, "print", lambda: print), _n_(334848, "Z", lambda: Z), "is a Consonant")
      _l_(334850)