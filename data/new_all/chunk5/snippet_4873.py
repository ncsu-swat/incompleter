# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44064232/nameerror-with-echo-client-server-test-client-unable-to-send-custom-message-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tincanchat
    _l_(659091)

except ImportError:
    pass

HOST = _a_(659093, _n_(659092, "tincanchat", lambda: tincanchat), "HOST")
_l_(659094)
PORT = _a_(659096, _n_(659095, "tincanchat", lambda: tincanchat), "PORT")
_l_(659097)

def handle_client(sock, addr):
    _l_(659134)

    """ Receive data from the client via sock and echo it back """
    try:
        _l_(659133)

        msg = _c_(659101, _a_(659099, _n_(659098, "tincanchat", lambda: tincanchat), "recv_msg"), _n_(659100, "sock", lambda: sock)) # Blocks until received
        _l_(659102) # Blocks until received
                                    # complete message
        _c_(659108, _n_(659103, "print", lambda: print), _c_(659107, _a_(659104, '{}: {}', "format"), _n_(659105, "addr", lambda: addr), _n_(659106, "msg", lambda: msg)))
        _l_(659109)
        _c_(659114, _a_(659111, _n_(659110, "tincanchat", lambda: tincanchat), "send_msg"), _n_(659112, "sock", lambda: sock), _n_(659113, "msg", lambda: msg)) # Blocks until sent
        _l_(659115) # Blocks until sent
    except (_n_(659116, "ConnectionError", lambda: ConnectionError), _n_(659117, "BrokenPipeError", lambda: BrokenPipeError)):
        _l_(659121)

        _c_(659119, _n_(659118, "print", lambda: print), 'Socket error')
        _l_(659120)
    finally:
        _l_(659132)

        _c_(659126, _n_(659122, "print", lambda: print), _c_(659125, _a_(659123, 'Closed connection to {}', "format"), _n_(659124, "addr", lambda: addr)))
        _l_(659127)
        _c_(659130, _a_(659129, _n_(659128, "sock", lambda: sock), "close"))
        _l_(659131)

if _n_(659135, "__name__", lambda: __name__) == '__main__':
    _l_(659168)

    listen_sock = _c_(659140, _a_(659137, _n_(659136, "tincanchat", lambda: tincanchat), "create_listen_socket"), _n_(659138, "HOST", lambda: HOST), _n_(659139, "PORT", lambda: PORT))
    _l_(659141)
    addr = _c_(659144, _a_(659143, _n_(659142, "listen_sock", lambda: listen_sock), "getsockname"))
    _l_(659145)
    _c_(659150, _n_(659146, "print", lambda: print), _c_(659149, _a_(659147, 'Listening on {}', "format"), _n_(659148, "addr", lambda: addr)))
    _l_(659151)

    while True:
        _l_(659167)

        client_sock, addr = _c_(659154, _a_(659153, _n_(659152, "listen_sock", lambda: listen_sock), "accept"))
        _l_(659155)
        _c_(659160, _n_(659156, "print", lambda: print), _c_(659159, _a_(659157, 'Connection from {}', "format"), _n_(659158, "addr", lambda: addr)))
        _l_(659161)
        _c_(659165, _n_(659162, "handle_client", lambda: handle_client), _n_(659163, "client_sock", lambda: client_sock), _n_(659164, "addr", lambda: addr))
        _l_(659166)