# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68417215/typeerror-float-object-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xfile = _c_(645302, _n_(645301, "open", lambda: open), '/Users/Documents/python/mbox-short.txt')
_l_(645303)
for line in _n_(645304, "xfile", lambda: xfile):
    _l_(645333)

    if not _c_(645307, _a_(645306, _n_(645305, "line", lambda: line), "startswith"), "X-DSPAM-Confidence:"):
        _l_(645309)

        continue
        _l_(645308)
    xf = _c_(645312, _a_(645311, _n_(645310, "line", lambda: line), "rstrip"))
    _l_(645313)
    ## Start Counting Lines
    count = 0 
    _l_(645314) 
    for numlines in _n_(645315, "xf", lambda: xf):
        _l_(645318)

        count = _n_(645316, "count", lambda: count) + 1
        _l_(645317)
    ## total count of lines with value <<<< code works up to this point
    values = _c_(645321, _n_(645319, "float", lambda: float), _n_(645320, "line", lambda: line)[20:])
    _l_(645322)
    _c_(645325, _n_(645323, "print", lambda: print), _n_(645324, "values", lambda: values))
    _l_(645326)
    for n in _n_(645327, "values", lambda: values):
        _l_(645332)

        _c_(645330, _n_(645328, "print", lambda: print), _n_(645329, "n", lambda: n)) 
        _l_(645331) 