# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42612002/python-sockets-error-typeerror-a-bytes-like-object-is-required-not-str-with
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = _c_(378794, _a_(378793, _n_(378792, "socket", lambda: socket), "socket"))
_l_(378795)
host = '127.0.0.1'
_l_(378796)
port = 12345
_l_(378797)
_c_(378802, _a_(378799, _n_(378798, "s", lambda: s), "bind"), (_n_(378800, "host", lambda: host), _n_(378801, "port", lambda: port)))
_l_(378803)

_c_(378806, _a_(378805, _n_(378804, "s", lambda: s), "listen"), 5)
_l_(378807)
while True:
    _l_(378824)

    c, addr = _c_(378810, _a_(378809, _n_(378808, "s", lambda: s), "accept"))
    _l_(378811)
    _c_(378814, _n_(378812, "print", lambda: print), 'Got connection from', _n_(378813, "addr", lambda: addr))
    _l_(378815)
    _c_(378818, _a_(378817, _n_(378816, "c", lambda: c), "send"), 'Thank you for connecting')
    _l_(378819)
    _c_(378822, _a_(378821, _n_(378820, "c", lambda: c), "close"))
    _l_(378823)