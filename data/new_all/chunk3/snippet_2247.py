# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56009331/how-do-i-fix-this-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = _c_(529163, _a_(529162, _n_(529161, "socket", lambda: socket), "socket"))
_l_(529164)
host = '127.0.0.1'
_l_(529165)
port = 12345
_l_(529166)
_c_(529171, _a_(529168, _n_(529167, "s", lambda: s), "bind"), (_n_(529169, "host", lambda: host), _n_(529170, "port", lambda: port)))
_l_(529172)

_c_(529175, _a_(529174, _n_(529173, "s", lambda: s), "listen"), 5)
_l_(529176)
while True:
    _l_(529193)

    c, addr = _c_(529179, _a_(529178, _n_(529177, "s", lambda: s), "accept"))
    _l_(529180)
    _c_(529183, _n_(529181, "print", lambda: print), 'Got connection from', _n_(529182, "addr", lambda: addr))
    _l_(529184)
    _c_(529187, _a_(529186, _n_(529185, "c", lambda: c), "send"), 'Thank you for connecting')
    _l_(529188)
    _c_(529191, _a_(529190, _n_(529189, "c", lambda: c), "close"))
    _l_(529192)