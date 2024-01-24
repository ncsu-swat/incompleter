# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50046578/i-understad-why-i-get-typeerror-getsockaddrarg-af-inet-address-must-be-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(437271)

except ImportError:
    pass

sock = _c_(437278, _a_(437273, _n_(437272, "socket", lambda: socket), "socket"), _a_(437275, _n_(437274, "socket", lambda: socket), "AF_INET"), _a_(437277, _n_(437276, "socket", lambda: socket), "SOCK_DGRAM"))
_l_(437279)

server_address = '0.0.0.0'
_l_(437280)
server_port = 5005
_l_(437281)

server = (_n_(437282, "server_address", lambda: server_address), _n_(437283, "server_port", lambda: server_port))
_l_(437284)
_c_(437288, _a_(437286, _n_(437285, "sock", lambda: sock), "bind"), _n_(437287, "server", lambda: server))
_l_(437289)
_c_(437295, _n_(437290, "print", lambda: print), "Listening on " + _n_(437291, "server_address", lambda: server_address) + " Port: " + _c_(437294, _n_(437292, "str", lambda: str), _n_(437293, "server_port", lambda: server_port)))
_l_(437296)
_c_(437299, _a_(437298, _n_(437297, "sock", lambda: sock), "connect"), ('0.0.0.0', 5002))
_l_(437300)
while True:
    _l_(437320)

    client_address = ('0.0.0.0')
    _l_(437301)
    status = 'ok'
    _l_(437302)
    _c_(437310, _n_(437303, "print", lambda: print), "Echoing back "+ _c_(437306, _n_(437304, "str", lambda: str), _n_(437305, "status", lambda: status)) + " to " + _c_(437309, _n_(437307, "str", lambda: str), _n_(437308, "client_address", lambda: client_address)))
    _l_(437311)
    sen = _c_(437318, _a_(437313, _n_(437312, "sock", lambda: sock), "sendto"), _c_(437316, _a_(437315, _n_(437314, "status", lambda: status), "encode")),_n_(437317, "client_address", lambda: client_address))
    _l_(437319)