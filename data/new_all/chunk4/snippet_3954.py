# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64723527/how-to-fix-the-error-typeerror-a-bytes-like-object-is-required-not-str-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(639039)

except ImportError:
    pass

serverName = '127.0.0.1'
_l_(639040)
serverPort = 12000
_l_(639041)
clientSocket = _c_(639045, _n_(639042, "socket", lambda: socket), _n_(639043, "AF_INET", lambda: AF_INET), _n_(639044, "SOCK_DGRAM", lambda: SOCK_DGRAM))
_l_(639046)
message = _c_(639048, _n_(639047, "input", lambda: input), 'Input lowercase sentence:')
_l_(639049)
_c_(639055, _a_(639051, _n_(639050, "clientSocket", lambda: clientSocket), "sendto"), _n_(639052, "message", lambda: message),(_n_(639053, "serverName", lambda: serverName), _n_(639054, "serverPort", lambda: serverPort)))
_l_(639056)
modifiedMessage, serverAddress = _c_(639059, _a_(639058, _n_(639057, "clientSocket", lambda: clientSocket), "recvfrom"), 2048)
_l_(639060)
_c_(639063, _n_(639061, "print", lambda: print), _n_(639062, "modifiedMessage", lambda: modifiedMessage))
_l_(639064)
_c_(639067, _a_(639066, _n_(639065, "clientSocket", lambda: clientSocket), "close"))
_l_(639068)