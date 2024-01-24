# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43092055/traceback-most-recent-call-last-typeerror-unsupported-operand-types-for
#!/usr/bin/python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(464423)

except ImportError:
    pass
try:
    import random
    _l_(464425)

except ImportError:
    pass
try:
    import struct
    _l_(464427)

except ImportError:
    pass
try:
    import select
    _l_(464429)

except ImportError:
    pass
try:
    import socket
    _l_(464431)

except ImportError:
    pass


def chk(data):
    _l_(464452)

    x = _c_(464439, _n_(464432, "sum", lambda: sum), (_n_(464433, "x", lambda: x) << 8 if _n_(464434, "i", lambda: i) % 2 else _n_(464435, "x", lambda: x) for i, x in _c_(464438, _n_(464436, "enumerate", lambda: enumerate), _n_(464437, "data", lambda: data)))) & 0xFFFFFFFF
    _l_(464440)
    x = (_n_(464441, "x", lambda: x) >> 16) + (_n_(464442, "x", lambda: x) & 0xFFFF)
    _l_(464443)
    x = (_n_(464444, "x", lambda: x) >> 16) + (_n_(464445, "x", lambda: x) & 0xFFFF)
    _l_(464446)
    aux = _c_(464450, _a_(464448, _n_(464447, "struct", lambda: struct), "pack"), '<H', ~_n_(464449, "x", lambda: x) & 0xFFFF)
    _l_(464451)
    return aux


def ping(addr, timeout=1, number=1, data=b''):
    _l_(464528)

    conn = _c_(464461, _a_(464454, _n_(464453, "socket", lambda: socket), "socket"), _a_(464456, _n_(464455, "socket", lambda: socket), "AF_INET"), _a_(464458, _n_(464457, "socket", lambda: socket), "SOCK_RAW"),  _a_(464460, _n_(464459, "socket", lambda: socket), "IPPROTO_ICMP"))
    _l_(464462)
    payload = _c_(464469, _a_(464464, _n_(464463, "struct", lambda: struct), "pack"), '!HH', _c_(464467, _a_(464466, _n_(464465, "random", lambda: random), "randrange"), 0, 65536), _n_(464468, "number", lambda: number)) + _n_(464470, "data", lambda: data)
    _l_(464471)

    _c_(464475, _a_(464473, _n_(464472, "conn", lambda: conn), "connect"), (_n_(464474, "addr", lambda: addr), 80))
    _l_(464476)
    _c_(464483, _a_(464478, _n_(464477, "conn", lambda: conn), "sendall"), b'\x08\0' + _c_(464481, _n_(464479, "chk", lambda: chk), b'\x08\0\0\0' + _n_(464480, "payload", lambda: payload)) + _n_(464482, "payload", lambda: payload))
    _l_(464484)
    start = _c_(464487, _a_(464486, _n_(464485, "time", lambda: time), "time"))
    _l_(464488)

    while _c_(464499, _a_(464490, _n_(464489, "select", lambda: select), "select"), [_n_(464491, "conn", lambda: conn)], [], [], _c_(464498, _n_(464492, "max", lambda: max), 0, _n_(464493, "start", lambda: start) + _n_(464494, "timeout", lambda: timeout) - _c_(464497, _a_(464496, _n_(464495, "time", lambda: time), "time"))))[0]:
        _l_(464527)

        data = _c_(464502, _a_(464501, _n_(464500, "conn", lambda: conn), "recv"), 65536)
        _l_(464503)
        if _c_(464506, _n_(464504, "len", lambda: len), _n_(464505, "data", lambda: data)) < 20 or _c_(464509, _n_(464507, "len", lambda: len), _n_(464508, "data", lambda: data)) < _c_(464513, _a_(464511, _n_(464510, "struct", lambda: struct), "unpack_from"), '!xxH', _n_(464512, "data", lambda: data))[0]:
            _l_(464515)

            continue
            _l_(464514)
        if _n_(464516, "data", lambda: data)[20:] == b'\0\0' + _c_(464519, _n_(464517, "chk", lambda: chk), b'\0\0\0\0' + _n_(464518, "payload", lambda: payload)) + _n_(464520, "payload", lambda: payload):
            _l_(464526)

            aux = _c_(464523, _a_(464522, _n_(464521, "time", lambda: time), "time")) - _n_(464524, "start", lambda: start)
            _l_(464525)
            return aux


if _n_(464529, "__name__", lambda: __name__) == '__main__':
    _l_(464539)

    target = _c_(464531, _n_(464530, "raw_input", lambda: raw_input), "Please enter a IP Adress: ")
    _l_(464532)
    _c_(464537, _n_(464533, "print", lambda: print), _c_(464536, _n_(464534, "ping", lambda: ping), _n_(464535, "target", lambda: target)))
    _l_(464538)