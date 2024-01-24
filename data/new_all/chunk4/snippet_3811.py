# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67369750/attributeerror-socket-object-attribute-send-is-read-only
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(627293)

except ImportError:
    pass

target_host = "google.com"
_l_(627294)

target_port = 80
_l_(627295)

client = _c_(627302, _a_(627297, _n_(627296, "socket", lambda: socket), "socket"), _a_(627299, _n_(627298, "socket", lambda: socket), "AF_INET"),_a_(627301, _n_(627300, "socket", lambda: socket), "SOCK_STREAM"))
_l_(627303)

_c_(627308, _a_(627305, _n_(627304, "client", lambda: client), "connect"), (_n_(627306, "target_host", lambda: target_host),_n_(627307, "target_port", lambda: target_port)))
_l_(627309)


_n_(627310, "client", lambda: client).send = ("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
_l_(627311)

response = _c_(627314, _a_(627313, _n_(627312, "client", lambda: client), "recv"), 4096)
_l_(627315)