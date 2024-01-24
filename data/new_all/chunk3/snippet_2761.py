# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64063104/typeerror-d-format-a-number-is-required-not-str-getting-this-error-while-cre
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import socket
    _l_(541364)

except ImportError:
    pass
try:
    import threading
    _l_(541366)

except ImportError:
    pass

bind_ip = "0.0.0.0"
_l_(541367)
bind_port = 9999
_l_(541368)

server = _c_(541375, _a_(541370, _n_(541369, "socket", lambda: socket), "socket"), _a_(541372, _n_(541371, "socket", lambda: socket), "AF_INET"), _a_(541374, _n_(541373, "socket", lambda: socket), "SOCK_STREAM"))
_l_(541376)
_c_(541381, _a_(541378, _n_(541377, "server", lambda: server), "bind"), (_n_(541379, "bind_ip", lambda: bind_ip), _n_(541380, "bind_port", lambda: bind_port)))
_l_(541382)
_c_(541385, _a_(541384, _n_(541383, "server", lambda: server), "listen"), 5)
_l_(541386)
_c_(541390, _n_(541387, "print", lambda: print), "[-#-]  Listening on %s:%d" % (_n_(541388, "bind_port", lambda: bind_port), _n_(541389, "bind_ip", lambda: bind_ip)))
_l_(541391)

# this is our clint-hanadaling thread


def handle_client(client_socket):
    _l_(541428)

    # print out what client sends
    request = _c_(541394, _a_(541393, _n_(541392, "client_socket", lambda: client_socket), "recv"), 1024)
    _l_(541395)
    _c_(541398, _n_(541396, "print", lambda: print), "[* ] Received %s " % _n_(541397, "request", lambda: request))
    _l_(541399)
    # send back a request
    _c_(541402, _a_(541401, _n_(541400, "client_socket", lambda: client_socket), "send"), "ACK!")
    _l_(541403)
    _c_(541406, _a_(541405, _n_(541404, "client_socket", lambda: client_socket), "close"))
    _l_(541407)
    while True:
        _l_(541427)

        client, addr = _c_(541410, _a_(541409, _n_(541408, "server", lambda: server), "accept"))
        _l_(541411)
        _c_(541415, _n_(541412, "print", lambda: print), "[*] Accepted connection from %s:%d" % (_n_(541413, "addr", lambda: addr)[0], _n_(541414, "addr", lambda: addr)[1]))
        _l_(541416)
        # spin up our client thread  to handle incoming data
        clinet_handler = _c_(541421, _a_(541418, _n_(541417, "threading", lambda: threading), "Thread"), target=_n_(541419, "handle_client", lambda: handle_client), args=_n_(541420, "client", lambda: client))
        _l_(541422)
        _c_(541425, _a_(541424, _n_(541423, "clinet_handler", lambda: clinet_handler), "start"))
        _l_(541426)