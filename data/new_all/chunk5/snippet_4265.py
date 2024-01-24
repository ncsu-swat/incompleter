# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60559859/typeerror-list-expected-at-most-1-arguments-got-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(698351)

except ImportError:
    pass
try:
    import sys
    _l_(698353)

except ImportError:
    pass
listed=[]
_l_(698354)
for folderName,subfolders,filenames in _c_(698357, _a_(698356, _n_(698355, "os", lambda: os), "walk"), '/'):
    _l_(698380)

    for filename in _n_(698358, "filenames", lambda: filenames):
        _l_(698379)

        if _c_(698361, _a_(698360, _n_(698359, "filename", lambda: filename), "endswith"), '.png'):
            _l_(698378)

            _c_(698365, _a_(698363, _n_(698362, "listed", lambda: listed), "append"), _n_(698364, "filename", lambda: filename))
            _l_(698366)
            for name in _c_(698372, _n_(698367, "range", lambda: range), _c_(698371, _n_(698368, "len", lambda: len), _c_(698370, _n_(698369, "list", lambda: list), 0,10))):
                _l_(698377)

                _c_(698375, _n_(698373, "print", lambda: print), _n_(698374, "name", lambda: name))
                _l_(698376)