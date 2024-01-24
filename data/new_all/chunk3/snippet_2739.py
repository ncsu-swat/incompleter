# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64780564/how-to-fix-attributeerror-module-tensorflow-has-no-attribute-session-in-han
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
hello = _c_(578128, _a_(578127, _n_(578126, "tf", lambda: tf), "constant"), 'Hello, TensorFlow!')
_l_(578129)
sess = _c_(578132, _a_(578131, _n_(578130, "tf", lambda: tf), "Session"))
_l_(578133)
_c_(578139, _n_(578134, "print", lambda: print), _c_(578138, _a_(578136, _n_(578135, "sess", lambda: sess), "run"), _n_(578137, "hello", lambda: hello)))
_l_(578140)