# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60381236/undefined-name-error-in-python-socket-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import socket
    _l_(658227)

except ImportError:
    pass
try:
    import sys
    _l_(658229)

except ImportError:
    pass

serverPort = 6789
_l_(658230)
serverSocket = _c_(658234, _n_(658231, "socket", lambda: socket), _n_(658232, "AF_INET", lambda: AF_INET), _n_(658233, "SOCK_STREAM", lambda: SOCK_STREAM))
_l_(658235)