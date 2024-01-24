# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73452966/python-error-typeerror-float-argument-must-be-a-string-or-a-real-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(346126)

except ImportError:
    pass
name = _c_(346128, _n_(346127, "input", lambda: input), 'Enter File: ')
_l_(346129)
if _c_(346132, _n_(346130, "len", lambda: len), _n_(346131, "name", lambda: name)) < 1 :
    _l_(346134)

    name = 'sample.txt'
    _l_(346133)
handle = _c_(346137, _n_(346135, "open", lambda: open), _n_(346136, "name", lambda: name))
_l_(346138)
numlist = _c_(346140, _n_(346139, "list", lambda: list))
_l_(346141)
for line in _n_(346142, "handle", lambda: handle) :
    _l_(346165)

    line = _c_(346145, _a_(346144, _n_(346143, "line", lambda: line), "rstrip"))
    _l_(346146)
    items = _c_(346150, _a_(346148, _n_(346147, "re", lambda: re), "findall"), '[0-9]+', _n_(346149, "line", lambda: line))
    _l_(346151)
    if _c_(346154, _n_(346152, "len", lambda: len), _n_(346153, "items", lambda: items)) > 0 :
        _l_(346164)

        #print(items)
        num = _c_(346157, _n_(346155, "float", lambda: float), _n_(346156, "items", lambda: items)[0: ])
        _l_(346158)
        _c_(346162, _a_(346160, _n_(346159, "numlist", lambda: numlist), "append"), _n_(346161, "num", lambda: num))
        _l_(346163)
_c_(346170, _n_(346166, "print", lambda: print), _c_(346169, _n_(346167, "sum", lambda: sum), _n_(346168, "numlist", lambda: numlist)))
_l_(346171)