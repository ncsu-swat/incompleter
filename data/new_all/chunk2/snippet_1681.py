# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63840651/how-to-handle-this-typeerror-in-string-requires-string-as-left-operand-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(460761)

except ImportError:
    pass
try:
    from os import path
    _l_(460763)

except ImportError:
    pass
try:
    import shutil
    _l_(460765)

except ImportError:
    pass

src = "D:/folder2"
_l_(460766)
dst = "D:/folder1"
_l_(460767)

files = [_n_(460768, "i", lambda: i) for i in _c_(460772, _a_(460770, _n_(460769, "os", lambda: os), "listdir"), _n_(460771, "src", lambda: src)) if ('7809.txt','988876.txt') in _n_(460773, "i", lambda: i) and _c_(460781, _a_(460775, _n_(460774, "path", lambda: path), "isfile"), _c_(460780, _a_(460777, _n_(460776, "path", lambda: path), "join"), _n_(460778, "src", lambda: src), _n_(460779, "i", lambda: i)))]
_l_(460782)
for f in _n_(460783, "files", lambda: files):
    _l_(460794)

    _c_(460792, _a_(460785, _n_(460784, "shutil", lambda: shutil), "copy"), _c_(460790, _a_(460787, _n_(460786, "path", lambda: path), "join"), _n_(460788, "src", lambda: src), _n_(460789, "f", lambda: f)), _n_(460791, "dst", lambda: dst))
    _l_(460793)