# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73452966/python-error-typeerror-float-argument-must-be-a-string-or-a-real-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(374174)

except ImportError:
    pass
name = _c_(374176, _n_(374175, "input", lambda: input), 'Enter File: ')
_l_(374177)
if _c_(374180, _n_(374178, "len", lambda: len), _n_(374179, "name", lambda: name)) < 1 :
    _l_(374182)

    name = 'sample.txt'
    _l_(374181)
handle = _c_(374185, _n_(374183, "open", lambda: open), _n_(374184, "name", lambda: name))
_l_(374186)
numlist = _c_(374188, _n_(374187, "list", lambda: list))
_l_(374189)
for line in _n_(374190, "handle", lambda: handle) :
    _l_(374213)

    line = _c_(374193, _a_(374192, _n_(374191, "line", lambda: line), "rstrip"))
    _l_(374194)
    items = _c_(374198, _a_(374196, _n_(374195, "re", lambda: re), "findall"), '[0-9]+', _n_(374197, "line", lambda: line))
    _l_(374199)
    if _c_(374202, _n_(374200, "len", lambda: len), _n_(374201, "items", lambda: items)) > 0 :
        _l_(374212)

        #print(items)
        num = _c_(374205, _n_(374203, "float", lambda: float), _n_(374204, "items", lambda: items)[0: ])
        _l_(374206)
        _c_(374210, _a_(374208, _n_(374207, "numlist", lambda: numlist), "append"), _n_(374209, "num", lambda: num))
        _l_(374211)
_c_(374218, _n_(374214, "print", lambda: print), _c_(374217, _n_(374215, "sum", lambda: sum), _n_(374216, "numlist", lambda: numlist)))
_l_(374219)