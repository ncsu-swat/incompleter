# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50046578/i-understad-why-i-get-typeerror-getsockaddrarg-af-inet-address-must-be-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import echoUDP
    _l_(428441)

except ImportError:
    pass

serveraddress = '0.0.0.0'
_l_(428442)
serverport = 5002
_l_(428443)

server2 = (_n_(428444, "server_address", lambda: server_address), _n_(428445, "server_port", lambda: server_port))
_l_(428446)
_c_(428450, _a_(428448, _n_(428447, "s", lambda: s), "bind"), _n_(428449, "server2", lambda: server2))
_l_(428451)
_c_(428457, _n_(428452, "print", lambda: print), "Listening on " + _n_(428453, "server_address", lambda: server_address) + ":" + _c_(428456, _n_(428454, "str", lambda: str), _n_(428455, "server_port", lambda: server_port)))
_l_(428458)
_c_(428461, _a_(428460, _n_(428459, "s", lambda: s), "connect"), ('0.0.0.0',5005))
_l_(428462)

while True:
    _l_(428482)

    client_address = ('0.0.0.0.')
    _l_(428463)
    status = 'ok'
    _l_(428464)
    _c_(428472, _n_(428465, "print", lambda: print), "Echoing back"+ _c_(428468, _n_(428466, "str", lambda: str), _n_(428467, "status", lambda: status)) + " to " + _c_(428471, _n_(428469, "str", lambda: str), _n_(428470, "client_address", lambda: client_address)))
    _l_(428473)
    sen = _c_(428480, _a_(428475, _n_(428474, "s", lambda: s), "sendto"), _c_(428478, _a_(428477, _n_(428476, "status", lambda: status), "encode")),_n_(428479, "clientaddress", lambda: clientaddress))
    _l_(428481)