# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46760474/facing-error-typeerror-int-object-is-not-iterable-when-sum-total-count
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import glob
    _l_(432913)

except ImportError:
    pass

def stats():
    _l_(432942)


    commaCount = 0
    _l_(432914)

    path = 'D:/Stiudies/Data/female/*.txt'
    _l_(432915)
    inf = _c_(432919, _a_(432917, _n_(432916, "glob", lambda: glob), "glob"), _n_(432918, "path", lambda: path))
    _l_(432920)

    for name in _n_(432921, "inf", lambda: inf):
        _l_(432941)

        with _c_(432924, _n_(432922, "open", lambda: open), _n_(432923, "name", lambda: name), 'r', encoding="utf8") as input_file:
            _l_(432940)

            for line in _n_(432925, "input_file", lambda: input_file):
                _l_(432935)

                for char in _n_(432926, "line", lambda: line):
                    _l_(432934)

                    if _n_(432927, "char", lambda: char) == ',':
                        _l_(432933)

                        commaCount += 1
                        _l_(432928)

                        total = _c_(432931, _n_(432929, "sum", lambda: sum), _n_(432930, "commaCount", lambda: commaCount))
                        _l_(432932)

            _c_(432938, _n_(432936, "print", lambda: print), _n_(432937, "commaCount", lambda: commaCount))
            _l_(432939)

_c_(432944, _n_(432943, "stats", lambda: stats))
_l_(432945)