# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68417215/typeerror-float-object-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xfile = _c_(586397, _n_(586396, "open", lambda: open), '/Users/Documents/python/mbox-short.txt')
_l_(586398)
for line in _n_(586399, "xfile", lambda: xfile):
    _l_(586428)

    if not _c_(586402, _a_(586401, _n_(586400, "line", lambda: line), "startswith"), "X-DSPAM-Confidence:"):
        _l_(586404)

        continue
        _l_(586403)
    xf = _c_(586407, _a_(586406, _n_(586405, "line", lambda: line), "rstrip"))
    _l_(586408)
    ## Start Counting Lines
    count = 0 
    _l_(586409) 
    for numlines in _n_(586410, "xf", lambda: xf):
        _l_(586413)

        count = _n_(586411, "count", lambda: count) + 1
        _l_(586412)
    ## total count of lines with value <<<< code works up to this point
    values = _c_(586416, _n_(586414, "float", lambda: float), _n_(586415, "line", lambda: line)[20:])
    _l_(586417)
    _c_(586420, _n_(586418, "print", lambda: print), _n_(586419, "values", lambda: values))
    _l_(586421)
    for n in _n_(586422, "values", lambda: values):
        _l_(586427)

        _c_(586425, _n_(586423, "print", lambda: print), _n_(586424, "n", lambda: n)) 
        _l_(586426) 