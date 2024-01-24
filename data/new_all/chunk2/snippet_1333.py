# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41498525/attribute-error-when-using-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class search:
   _l_(445127)

   def test(self):
      _l_(445120)

      _n_(445114, "self", lambda: self).here = 'hi'
      _l_(445115)
      _n_(445116, "self", lambda: self).gone = 'bye'
      _l_(445117)
      _n_(445118, "self", lambda: self).num = 12
      _l_(445119)

   def tester(self):
      _l_(445126)

      aux = _c_(445124, _a_(445121, "{}", "format"), _a_(445123, _n_(445122, "self", lambda: self), "here"))
      _l_(445125)
      return aux

s = _c_(445129, _n_(445128, "search", lambda: search))
_l_(445130)
_c_(445133, _a_(445132, _n_(445131, "s", lambda: s), "tester"))
_l_(445134)
_c_(445138, _n_(445135, "print", lambda: print), _a_(445137, _n_(445136, "s", lambda: s), "gone"))
_l_(445139)