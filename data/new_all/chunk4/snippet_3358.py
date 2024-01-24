# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75403903/why-am-i-receiving-the-typeerror-str-object-cannot-be-interpreted-as-an-inte
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def listen():
    _l_(589046)

    host = _c_(589010, _n_(589009, "input", lambda: input), "Please enter your target host IP: ")
    _l_(589011)
    port = _c_(589013, _n_(589012, "input", lambda: input), "Please enter target port: ")
    _l_(589014)
    try:
        _l_(589030)

        _c_(589019, _a_(589016, _n_(589015, "s", lambda: s), "bind"), (_n_(589017, "host", lambda: host), _n_(589018, "port", lambda: port)))
        _l_(589020)
    except _a_(589022, _n_(589021, "socket", lambda: socket), "error") as e:
        _l_(589029)

        _c_(589027, _n_(589023, "print", lambda: print), _c_(589026, _n_(589024, "str", lambda: str), _n_(589025, "e", lambda: e)))
        _l_(589028)
    _c_(589033, _a_(589032, _n_(589031, "s", lambda: s), "listen"), 5)
    _l_(589034)
    conn, addr = _c_(589037, _a_(589036, _n_(589035, "s", lambda: s), "accept"))
    _l_(589038)
    _c_(589044, _n_(589039, "print", lambda: print), "pwned: "+_n_(589040, "addr", lambda: addr)[0]+":"+_c_(589043, _n_(589041, "str", lambda: str), _n_(589042, "addr", lambda: addr)[1]))
    _l_(589045)


_c_(589048, _n_(589047, "listen", lambda: listen))
_l_(589049)