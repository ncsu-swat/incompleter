# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58075064/sock-bind-typeerror-an-integer-is-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(694559)

except ImportError:
    pass
UDP_IP="localhost"
_l_(694560)
UDP_PORT="8080"
_l_(694561)
sock=_c_(694568, _a_(694563, _n_(694562, "socket", lambda: socket), "socket"), _a_(694565, _n_(694564, "socket", lambda: socket), "AF_INET"),_a_(694567, _n_(694566, "socket", lambda: socket), "SOCK_DGRAM"))
_l_(694569)
_c_(694574, _a_(694571, _n_(694570, "sock", lambda: sock), "bind"), (_n_(694572, "UDP_IP", lambda: UDP_IP),_n_(694573, "UDP_PORT", lambda: UDP_PORT)))
_l_(694575)