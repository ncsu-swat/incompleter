# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50995772/python3-socket-attributeerror-io-bufferedreader-object-has-no-attribute-en
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(534084)

except ImportError:
    pass
try:
    import os
    _l_(534086)

except ImportError:
    pass

s = _c_(534093, _a_(534088, _n_(534087, "socket", lambda: socket), "socket"), _a_(534090, _n_(534089, "socket", lambda: socket), "AF_INET"), _a_(534092, _n_(534091, "socket", lambda: socket), "SOCK_STREAM"))
_l_(534094)

host = "127.0.0.1"
_l_(534095)
port = 5460
_l_(534096)

def myC_F():
    _l_(534149)


    try:
        _l_(534112)

        _c_(534101, _a_(534098, _n_(534097, "s", lambda: s), "connect"), (_n_(534099, "host", lambda: host), _n_(534100, "port", lambda: port)))
        _l_(534102)
        _c_(534104, _n_(534103, "print", lambda: print), "connected to socket")
        _l_(534105)
    except:
        _l_(534111)

        _c_(534109, _n_(534106, "print", lambda: print), "failed connecting to: ", _n_(534107, "host", lambda: host), _n_(534108, "port", lambda: port))
        _l_(534110)

    fPath = _c_(534114, _n_(534113, "input", lambda: input), "Enter file to send:> ")
    _l_(534115)
    fSize = _c_(534120, _a_(534118, _a_(534117, _n_(534116, "os", lambda: os), "path"), "getsize"), _n_(534119, "fPath", lambda: fPath))
    _l_(534121)
    fSize = _c_(534124, _n_(534122, "str", lambda: str), _n_(534123, "fSize", lambda: fSize))
    _l_(534125)
    _c_(534131, _a_(534127, _n_(534126, "s", lambda: s), "send"), _c_(534130, _a_(534129, _n_(534128, "fSize", lambda: fSize), "encode")))
    _l_(534132)
    _c_(534135, _n_(534133, "print", lambda: print), "...DONE SENDING SIZE :", _n_(534134, "fSize", lambda: fSize))
    _l_(534136)
    while True:
        _l_(534148)

        with _c_(534139, _n_(534137, "open", lambda: open), _n_(534138, "fPath", lambda: fPath), "rb") as f:
            _l_(534147)

            _c_(534145, _a_(534141, _n_(534140, "s", lambda: s), "sendall"), _c_(534144, _a_(534143, _n_(534142, "f", lambda: f), "encode")))
            _l_(534146)


_c_(534151, _n_(534150, "myC_F", lambda: myC_F))
_l_(534152)