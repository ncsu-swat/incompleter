# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42334343/when-i-write-dir-i-get-this-error-typeerror-descriptor-encode-requires-a-s
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(538949)
try:
    import socket
    _l_(538951)

except ImportError:
    pass
try:
    import sys
    _l_(538953)

except ImportError:
    pass

def socket_create():
    _l_(538973)


    try:
        _l_(538972)


        global host
        _l_(538954)
        global port
        _l_(538955)
        global s
        _l_(538956)
        host = ''
        _l_(538957)
        port = 9999
        _l_(538958)
        s = _c_(538961, _a_(538960, _n_(538959, "socket", lambda: socket), "socket"))
        _l_(538962)
    except _a_(538964, _n_(538963, "socket", lambda: socket), "error") as msg:
        _l_(538971)

        _c_(538969, _n_(538965, "print", lambda: print), "Socket creation error: " + _c_(538968, _n_(538966, "str", lambda: str), _n_(538967, "msg", lambda: msg)))
        _l_(538970)



def socket_bind():
    _l_(539006)


    try:
        _l_(539005)

        global host
        _l_(538974)
        global port
        _l_(538975)
        global  s
        _l_(538976)
        _c_(538981, _n_(538977, "print", lambda: print), "Binding socket to port: " + _c_(538980, _n_(538978, "str", lambda: str), _n_(538979, "port", lambda: port)))
        _l_(538982)
        _c_(538987, _a_(538984, _n_(538983, "s", lambda: s), "bind"), (_n_(538985, "host", lambda: host),_n_(538986, "port", lambda: port)))
        _l_(538988)
        _c_(538991, _a_(538990, _n_(538989, "s", lambda: s), "listen"), 5)
        _l_(538992)
    except _a_(538994, _n_(538993, "socket", lambda: socket), "error") as msg:
        _l_(539004)

        _c_(538999, _n_(538995, "print", lambda: print), "Socket binding error: " + _c_(538998, _n_(538996, "str", lambda: str), _n_(538997, "msg", lambda: msg)) + "\n" + "Retrying...")
        _l_(539000)
        _c_(539002, _n_(539001, "socket_bind", lambda: socket_bind))
        _l_(539003)


def socket_accept():
    _l_(539026)


    conn, address = _c_(539009, _a_(539008, _n_(539007, "s", lambda: s), "accept"))
    _l_(539010)
    _c_(539016, _n_(539011, "print", lambda: print), "Connection has been established | " + "IP " + _n_(539012, "address", lambda: address)[0] + "| Port " + _c_(539015, _n_(539013, "str", lambda: str), _n_(539014, "address", lambda: address)[1]))
    _l_(539017)
    _c_(539020, _n_(539018, "send_commands", lambda: send_commands), _n_(539019, "conn", lambda: conn))
    _l_(539021)
    _c_(539024, _a_(539023, _n_(539022, "conn", lambda: conn), "close"))
    _l_(539025)


def send_commands(conn):
    _l_(539070)


    while True:
        _l_(539069)

        cmd = _c_(539028, _n_(539027, "input", lambda: input))
        _l_(539029)
        if _n_(539030, "cmd", lambda: cmd) == 'quit':
            _l_(539043)

            _c_(539033, _a_(539032, _n_(539031, "conn", lambda: conn), "close"))
            _l_(539034)
            _c_(539037, _a_(539036, _n_(539035, "s", lambda: s), "close"))
            _l_(539038)
            _c_(539041, _a_(539040, _n_(539039, "sys", lambda: sys), "exit"))
            _l_(539042)
        if _c_(539049, _n_(539044, "len", lambda: len), _c_(539048, _a_(539046, _n_(539045, "str", lambda: str), "encode"), _n_(539047, "cmd", lambda: cmd))) > 0:
            _l_(539068)

            _c_(539056, _a_(539051, _n_(539050, "conn", lambda: conn), "send"), _c_(539055, _a_(539053, _n_(539052, "str", lambda: str), "encode"), _n_(539054, "cmd", lambda: cmd)))
            _l_(539057)
            client_response = _c_(539062, _n_(539058, "str", lambda: str), _c_(539061, _a_(539060, _n_(539059, "conn", lambda: conn), "recv"), 1024), "utf-8")
            _l_(539063)
            _c_(539066, _n_(539064, "print", lambda: print), _n_(539065, "client_response", lambda: client_response), end ="")
            _l_(539067)

def main():
    _l_(539080)


    _c_(539072, _n_(539071, "socket_create", lambda: socket_create))
    _l_(539073)
    _c_(539075, _n_(539074, "socket_bind", lambda: socket_bind))
    _l_(539076)
    _c_(539078, _n_(539077, "socket_accept", lambda: socket_accept))
    _l_(539079)

_c_(539082, _n_(539081, "main", lambda: main))
_l_(539083)