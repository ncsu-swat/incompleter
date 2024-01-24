# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44344818/socket-sendall-method-throws-typeerror-a-bytes-like-object-is-required-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(407133)

except ImportError:
    pass
mysock = _c_(407140, _a_(407135, _n_(407134, "socket", lambda: socket), "socket"), _a_(407137, _n_(407136, "socket", lambda: socket), "AF_INET"), _a_(407139, _n_(407138, "socket", lambda: socket), "SOCK_STREAM"))
_l_(407141)
host = _c_(407144, _a_(407143, _n_(407142, "socket", lambda: socket), "gethostbyname"), "www.google.com")
_l_(407145)
_c_(407149, _a_(407147, _n_(407146, "mysock", lambda: mysock), "connect"), _n_(407148, "host", lambda: host), 80)
_l_(407150)
message = "GET / HTTP/1.1\r\n\r\n"
_l_(407151)
_c_(407155, _a_(407153, _n_(407152, "mysock", lambda: mysock), "sendall"), _n_(407154, "message", lambda: message))
_l_(407156)
data=_c_(407159, _a_(407158, _n_(407157, "mysock", lambda: mysock), "recv"), 1000)
_l_(407160)
_c_(407163, _a_(407162, _n_(407161, "mysock", lambda: mysock), "close"))
_l_(407164)