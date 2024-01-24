# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43237853/python-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(379015)

except ImportError:
    pass
target_host = "www.google.com"
_l_(379016)
target_port = 80
_l_(379017)

client = _c_(379024, _a_(379019, _n_(379018, "socket", lambda: socket), "socket"), _a_(379021, _n_(379020, "socket", lambda: socket), "AF_INET"), _a_(379023, _n_(379022, "socket", lambda: socket), "SOCK_STREAM"))
_l_(379025)
_c_(379030, _a_(379027, _n_(379026, "client", lambda: client), "connect"), (_n_(379028, "target_host", lambda: target_host),_n_(379029, "target_port", lambda: target_port)))
_l_(379031)
_c_(379034, _a_(379033, _n_(379032, "client", lambda: client), "send"), "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
_l_(379035)
response = _c_(379038, _a_(379037, _n_(379036, "client", lambda: client), "recv"), 4096)
_l_(379039)
_c_(379042, _n_(379040, "print", lambda: print), _n_(379041, "response", lambda: response))
_l_(379043)