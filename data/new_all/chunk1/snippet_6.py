# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/3969726/attributeerror-module-object-has-no-attribute-urlopen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib
    _l_(403122)

except ImportError:
    pass

file = _c_(403125, _a_(403124, _n_(403123, "urllib", lambda: urllib), "urlopen"), "http://www.python.org")
_l_(403126)
s = _c_(403129, _a_(403128, _n_(403127, "file", lambda: file), "read"))
_l_(403130)
_c_(403133, _a_(403132, _n_(403131, "f", lambda: f), "close"))
_l_(403134)

#I'm guessing this would output the html source code?
_c_(403137, _n_(403135, "print", lambda: print), _n_(403136, "s", lambda: s))
_l_(403138)