# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55572280/python-sockets-typeerror-error-bytes-like-object-is-required-not-str-with-se
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(663965)

except ImportError:
    pass

serverName = '127.0.0.1'
_l_(663966)
serverPort = 12000
_l_(663967)
clientSocket = _c_(663971, _n_(663968, "socket", lambda: socket), _n_(663969, "AF_INET", lambda: AF_INET), _n_(663970, "SOCK_DGRAM", lambda: SOCK_DGRAM))
_l_(663972)
message = _c_(663974, _n_(663973, "input", lambda: input), 'Input lowercase sentence:')
_l_(663975)
_c_(663981, _a_(663977, _n_(663976, "clientSocket", lambda: clientSocket), "sendto"), _n_(663978, "message", lambda: message),(_n_(663979, "serverName", lambda: serverName), _n_(663980, "serverPort", lambda: serverPort)))
_l_(663982)
modifiedMessage, serverAddress = _c_(663985, _a_(663984, _n_(663983, "clientSocket", lambda: clientSocket), "recvfrom"), 2048)
_l_(663986)
_c_(663989, _n_(663987, "print", lambda: print), _n_(663988, "modifiedMessage", lambda: modifiedMessage))
_l_(663990)
_c_(663993, _a_(663992, _n_(663991, "clientSocket", lambda: clientSocket), "close"))
_l_(663994)