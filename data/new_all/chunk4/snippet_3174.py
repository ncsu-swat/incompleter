# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28817876/nameerror-name-record-is-not-defined-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from socket import *
    _l_(609438)

except ImportError:
    pass
try:
    from codecs import decode
    _l_(609440)

except ImportError:
    pass
try:
    from chatrecord import ChatRecord
    _l_(609442)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(609444)

except ImportError:
    pass
try:
    from time import ctime
    _l_(609446)

except ImportError:
    pass

class ClientHandler(_n_(609447, "Thread", lambda: Thread)):
    _l_(609536)


    def __init__(self, client, record):
        _l_(609459)

        _c_(609451, _a_(609449, _n_(609448, "Thread", lambda: Thread), "__init__"), _n_(609450, "self", lambda: self))
        _l_(609452)
        _n_(609453, "self", lambda: self)._client = _n_(609454, "client", lambda: client)
        _l_(609455)
        _n_(609456, "self", lambda: self)._record = _n_(609457, "record", lambda: record)
        _l_(609458)

    def run(self):
        _l_(609535)

        _c_(609466, _a_(609462, _a_(609461, _n_(609460, "self", lambda: self), "_client"), "send"), _c_(609465, _n_(609463, "bytes", lambda: bytes), 'Welcome', _n_(609464, "CODE", lambda: CODE)))
        _l_(609467)
        _n_(609468, "self", lambda: self)._name = _c_(609476, _n_(609469, "decode", lambda: decode), _c_(609474, _a_(609472, _a_(609471, _n_(609470, "self", lambda: self), "_client"), "recv"), _n_(609473, "BUFSIZE", lambda: BUFSIZE)), _n_(609475, "CODE", lambda: CODE))
        _l_(609477)
        _c_(609488, _a_(609480, _a_(609479, _n_(609478, "self", lambda: self), "_client"), "send"), _c_(609487, _n_(609481, "bytes", lambda: bytes), _c_(609485, _n_(609482, "str", lambda: str), _a_(609484, _n_(609483, "self", lambda: self), "_record")), _n_(609486, "CODE", lambda: CODE)))
        _l_(609489)
        while True:
            _l_(609534)

            message = _c_(609497, _n_(609490, "decode", lambda: decode), _c_(609495, _a_(609493, _a_(609492, _n_(609491, "self", lambda: self), "_client"), "recv"), _n_(609494, "BUFSIZE", lambda: BUFSIZE)), _n_(609496, "CODE", lambda: CODE))
            _l_(609498)
            if not _n_(609499, "message", lambda: message):
                _l_(609533)

                _c_(609501, _n_(609500, "print", lambda: print), 'Client disconnected')
                _l_(609502)
                _c_(609506, _a_(609505, _a_(609504, _n_(609503, "self", lambda: self), "_client"), "close"))
                _l_(609507)
                break
                _l_(609508)
            else:
                message = _a_(609510, _n_(609509, "self", lambda: self), "_name") + '' + \
                          _c_(609512, _n_(609511, "ctime", lambda: ctime)) + '\n' + _n_(609513, "message", lambda: message)
                _l_(609514)
                _c_(609519, _a_(609517, _a_(609516, _n_(609515, "self", lambda: self), "_record"), "add"), _n_(609518, "message", lambda: message))
                _l_(609520)
                _c_(609531, _a_(609523, _a_(609522, _n_(609521, "self", lambda: self), "_client"), "send"), _c_(609530, _n_(609524, "bytes", lambda: bytes), _c_(609528, _n_(609525, "str", lambda: str), _a_(609527, _n_(609526, "self", lambda: self), "_record")), _n_(609529, "CODE", lambda: CODE)))
                _l_(609532)


HOST = 'localhost'
_l_(609537)
PORT = 5000
_l_(609538)
BUFSIZE = 1024
_l_(609539)
ADDRESS = (_n_(609540, "HOST", lambda: HOST), _n_(609541, "PORT", lambda: PORT))
_l_(609542)
CODE = 'ascii'
_l_(609543)
server = _c_(609547, _n_(609544, "socket", lambda: socket), _n_(609545, "AF_INET", lambda: AF_INET), _n_(609546, "SOCK_STREAM", lambda: SOCK_STREAM))
_l_(609548)
_c_(609552, _a_(609550, _n_(609549, "server", lambda: server), "bind"), _n_(609551, "ADDRESS", lambda: ADDRESS))
_l_(609553)
_c_(609556, _a_(609555, _n_(609554, "server", lambda: server), "listen"), 5)
_l_(609557)

while True:
    _l_(609578)

    _c_(609559, _n_(609558, "print", lambda: print), 'Waiting for connection...')
    _l_(609560)
    client, address = _c_(609563, _a_(609562, _n_(609561, "server", lambda: server), "accept"))
    _l_(609564)
    _c_(609567, _n_(609565, "print", lambda: print), '...connected from:', _n_(609566, "address", lambda: address))
    _l_(609568)
    handler = _c_(609572, _n_(609569, "ClientHandler", lambda: ClientHandler), _n_(609570, "client", lambda: client), _n_(609571, "record", lambda: record))
    _l_(609573)
    _c_(609576, _a_(609575, _n_(609574, "handler", lambda: handler), "start"))
    _l_(609577)