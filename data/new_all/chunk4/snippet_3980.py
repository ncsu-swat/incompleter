# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64723527/how-to-fix-the-error-typeerror-a-bytes-like-object-is-required-not-str-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(583200)

except ImportError:
    pass

serverName = '127.0.0.1'
_l_(583201)
serverPort = 12000
_l_(583202)
clientSocket = _c_(583206, _n_(583203, "socket", lambda: socket), _n_(583204, "AF_INET", lambda: AF_INET), _n_(583205, "SOCK_DGRAM", lambda: SOCK_DGRAM))
_l_(583207)
message = _c_(583209, _n_(583208, "input", lambda: input), 'Input lowercase sentence:')
_l_(583210)
_c_(583216, _a_(583212, _n_(583211, "clientSocket", lambda: clientSocket), "sendto"), _n_(583213, "message", lambda: message),(_n_(583214, "serverName", lambda: serverName), _n_(583215, "serverPort", lambda: serverPort)))
_l_(583217)
modifiedMessage, serverAddress = _c_(583220, _a_(583219, _n_(583218, "clientSocket", lambda: clientSocket), "recvfrom"), 2048)
_l_(583221)
_c_(583224, _n_(583222, "print", lambda: print), _n_(583223, "modifiedMessage", lambda: modifiedMessage))
_l_(583225)
_c_(583228, _a_(583227, _n_(583226, "clientSocket", lambda: clientSocket), "close"))
_l_(583229)