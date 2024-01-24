# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42725239/trick-to-solve-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(677013)

except ImportError:
    pass

serverName = '127.0.0.1'
_l_(677014)
serverPort = 12000
_l_(677015)
clientSocket = _c_(677019, _n_(677016, "socket", lambda: socket), _n_(677017, "AF_INET", lambda: AF_INET), _n_(677018, "SOCK_DGRAM", lambda: SOCK_DGRAM))
_l_(677020)
message = _c_(677022, _n_(677021, "input", lambda: input), 'Input lowercase sentence:')
_l_(677023)
_c_(677029, _a_(677025, _n_(677024, "clientSocket", lambda: clientSocket), "sendto"), _n_(677026, "message", lambda: message),(_n_(677027, "serverName", lambda: serverName), _n_(677028, "serverPort", lambda: serverPort)))
_l_(677030)
modifiedMessage, serverAddress = _c_(677033, _a_(677032, _n_(677031, "clientSocket", lambda: clientSocket), "recvfrom"), 2048)
_l_(677034)
_c_(677037, _n_(677035, "print", lambda: print), _n_(677036, "modifiedMessage", lambda: modifiedMessage))
_l_(677038)
_c_(677041, _a_(677040, _n_(677039, "clientSocket", lambda: clientSocket), "close"))
_l_(677042)