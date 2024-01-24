# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77680000/typeerror-sslcontext-wrap-socket-missing-1-required-positional-argument-soc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ssl
    _l_(567922)

except ImportError:
    pass
try:
    import socket
    _l_(567924)

except ImportError:
    pass
sock = _c_(567931, _a_(567926, _n_(567925, "socket", lambda: socket), "socket"), _a_(567928, _n_(567927, "socket", lambda: socket), "AF_INET"), _a_(567930, _n_(567929, "socket", lambda: socket), "SOCK_STREAM")) 
_l_(567932) 
ssl_sock = _c_(567937, _a_(567935, _a_(567934, _n_(567933, "ssl", lambda: ssl), "SSLContext"), "wrap_socket"), _n_(567936, "sock", lambda: sock))
_l_(567938)