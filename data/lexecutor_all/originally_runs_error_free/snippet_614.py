# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import re
     _l_(1540444)

except ImportError:
     pass

name = ["A1B1", "djdd", "B2C4", "C2H2", "jdoi","1A4V"]
_l_(1540445)

# Match names.
for element in _n_(1540446, "name", lambda: name):
     _l_(1540460)

     m = _c_(1540450, _a_(1540448, _n_(1540447, "re", lambda: re), "match"), "(^[A-Z]\d[A-Z]\d)", _n_(1540449, "element", lambda: element))
     _l_(1540451)
     if _n_(1540452, "m", lambda: m):
          _l_(1540459)

          _c_(1540457, _n_(1540453, "print", lambda: print), _c_(1540456, _a_(1540455, _n_(1540454, "m", lambda: m), "groups")))
          _l_(1540458)

