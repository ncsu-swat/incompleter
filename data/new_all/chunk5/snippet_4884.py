# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42725239/trick-to-solve-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(664502)

except ImportError:
    pass

serverName = '127.0.0.1'
_l_(664503)
serverPort = 12000
_l_(664504)
clientSocket = _c_(664508, _n_(664505, "socket", lambda: socket), _n_(664506, "AF_INET", lambda: AF_INET), _n_(664507, "SOCK_DGRAM", lambda: SOCK_DGRAM))
_l_(664509)
message = _c_(664511, _n_(664510, "input", lambda: input), 'Input lowercase sentence:')
_l_(664512)
_c_(664518, _a_(664514, _n_(664513, "clientSocket", lambda: clientSocket), "sendto"), _n_(664515, "message", lambda: message),(_n_(664516, "serverName", lambda: serverName), _n_(664517, "serverPort", lambda: serverPort)))
_l_(664519)
modifiedMessage, serverAddress = _c_(664522, _a_(664521, _n_(664520, "clientSocket", lambda: clientSocket), "recvfrom"), 2048)
_l_(664523)
_c_(664526, _n_(664524, "print", lambda: print), _n_(664525, "modifiedMessage", lambda: modifiedMessage))
_l_(664527)
_c_(664530, _a_(664529, _n_(664528, "clientSocket", lambda: clientSocket), "close"))
_l_(664531)