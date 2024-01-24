# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62347145/how-to-resolve-typeerror-builtin-function-or-method-object-is-not-iterable-on
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
f = _a_(654166, _c_(654165, _n_(654163, "open", lambda: open), _n_(654164, "fileFirst", lambda: fileFirst),'r'), "readlines")
_l_(654167)
sf = _a_(654171, _c_(654170, _n_(654168, "open", lambda: open), _n_(654169, "fileSecond", lambda: fileSecond),'r'), "readlines")
_l_(654172)
result = _c_(654175, _a_(654174, _n_(654173, "difflib", lambda: difflib), "HtmlDiff"))
_l_(654176)
diff = _c_(654183, _a_(654178, _n_(654177, "result", lambda: result), "make_file"), _n_(654179, "ff", lambda: ff), _n_(654180, "sf", lambda: sf), _n_(654181, "fileFirst", lambda: fileFirst), _n_(654182, "fileSecond", lambda: fileSecond))
_l_(654184)