# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70637794/typeerror-when-using-af-inet-in-the-sockets-library
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(450679)

except ImportError:
    pass
s = _c_(450686, _a_(450681, _n_(450680, "socket", lambda: socket), "socket"), _a_(450683, _n_(450682, "socket", lambda: socket), "AF_INET"), _a_(450685, _n_(450684, "socket", lambda: socket), "SOCK_STREAM"))
_l_(450687)
_c_(450693, _a_(450689, _n_(450688, "s", lambda: s), "connect"), _c_(450692, _a_(450691, _n_(450690, "socket", lambda: socket), "gethostname")))
_l_(450694)
_c_(450696, _n_(450695, "print", lambda: print), "client successfully started")
_l_(450697)
msg = _c_(450700, _a_(450699, _n_(450698, "s", lambda: s), "recv"), 1024)
_l_(450701)
_c_(450706, _n_(450702, "print", lambda: print), _c_(450705, _a_(450704, _n_(450703, "msg", lambda: msg), "decode"), "utf-8"))
_l_(450707)