# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43903884/attributeerror-when-assigning-to-a-manager-dict-in-a-child-process
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(546858)

except ImportError:
    pass
try:
    from socketserver import UDPServer, ForkingMixIn, DatagramRequestHandler
    _l_(546860)

except ImportError:
    pass
try:
    from socket import socket, AF_INET, SOCK_DGRAM
    _l_(546862)

except ImportError:
    pass
try:
    from settings import host, port, number_of_connections
    _l_(546864)

except ImportError:
    pass

class ChatHandler(_n_(546865, "DatagramRequestHandler", lambda: DatagramRequestHandler)):
    _l_(546891)


    def handle(self):
        _l_(546890)

        cur_process = _c_(546868, _a_(546867, _n_(546866, "multiprocessing", lambda: multiprocessing), "current_process"))
        _l_(546869)
        data = _c_(546873, _a_(546872, _a_(546871, _n_(546870, "self", lambda: self), "request")[0], "strip"))
        _l_(546874)
        socket = _a_(546876, _n_(546875, "self", lambda: self), "request")[1]
        _l_(546877)
        _c_(546883, _a_(546880, _a_(546879, _n_(546878, "ChatHandler", lambda: ChatHandler), "clients"), "append"), _a_(546882, _n_(546881, "self", lambda: self), "client_address")) # error here
        _l_(546884) # error here
        _c_(546888, _n_(546885, "print", lambda: print), _a_(546887, _n_(546886, "ChatHandler", lambda: ChatHandler), "clients"))
        _l_(546889)


class ChatServer(_n_(546892, "ForkingMixIn", lambda: ForkingMixIn), _n_(546893, "UDPServer", lambda: UDPServer)):
    _l_(546895)

    pass
    _l_(546894)


if _n_(546896, "__name__", lambda: __name__) == '__main__':
    _l_(546922)

    server = _c_(546901, _n_(546897, "ChatServer", lambda: ChatServer), (_n_(546898, "host", lambda: host), _n_(546899, "port", lambda: port)), _n_(546900, "ChatHandler", lambda: ChatHandler))
    _l_(546902)
    _n_(546903, "ChatHandler", lambda: ChatHandler).clients = _c_(546908, _a_(546907, _c_(546906, _a_(546905, _n_(546904, "multiprocessing", lambda: multiprocessing), "Manager")), "list"))
    _l_(546909)
    server_process = _c_(546914, _a_(546911, _n_(546910, "multiprocessing", lambda: multiprocessing), "Process"), target=_a_(546913, _n_(546912, "server", lambda: server), "serve_forever"))
    _l_(546915)
    _n_(546916, "server_process", lambda: server_process).daemon = False
    _l_(546917)
    _c_(546920, _a_(546919, _n_(546918, "server_process", lambda: server_process), "start"))
    _l_(546921)