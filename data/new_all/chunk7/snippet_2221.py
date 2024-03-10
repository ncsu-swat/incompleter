# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57291924/code-to-detect-if-a-line-in-a-file-is-unicode-typeerror-string-argument-withou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(569066)

except ImportError:
    pass
try:
    from chardet.universaldetector import UniversalDetector
    _l_(569068)

except ImportError:
    pass

detector = _c_(569070, _n_(569069, "UniversalDetector", lambda: UniversalDetector))
_l_(569071)
files = _c_(569074, _a_(569073, _n_(569072, "glob", lambda: glob), "glob"), r'C:\Users\name\Documents\folder\*.txt')
_l_(569075)

for filename in _n_(569076, "files", lambda: files):
    _l_(569106)

    _c_(569081, _n_(569077, "print", lambda: print), _c_(569080, _a_(569079, _n_(569078, "filename", lambda: filename), "ljust"), 60))
    _l_(569082)
    _c_(569085, _a_(569084, _n_(569083, "detector", lambda: detector), "reset"))
    _l_(569086)
    for line in _n_(569087, "filename", lambda: filename):
        _l_(569096)

        _c_(569091, _a_(569089, _n_(569088, "detector", lambda: detector), "feed"), _n_(569090, "line", lambda: line))
        _l_(569092)
        if _a_(569094, _n_(569093, "detector", lambda: detector), "done"):
            _l_(569095)

break    _c_(569099, _a_(569098, _n_(569097, "detector", lambda: detector), "close"))
    _l_(569100)
    _c_(569104, _n_(569101, "print", lambda: print), _a_(569103, _n_(569102, "detector", lambda: detector), "result"))
    _l_(569105)