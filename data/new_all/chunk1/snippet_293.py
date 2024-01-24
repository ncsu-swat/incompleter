# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56303279/typeerror-a-bytes-like-object-is-required-not-str-in-python3-http-request
#!/usr/bin/env python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scapy.all as scapy
    _l_(381606)

except ImportError:
    pass
try:
    from scapy_http import http
    _l_(381608)

except ImportError:
    pass


def sniff(interface):
    _l_(381615)

    _c_(381613, _a_(381610, _n_(381609, "scapy", lambda: scapy), "sniff"), iface=_n_(381611, "interface", lambda: interface), store=False, prn=_n_(381612, "process_sniffed_packet", lambda: process_sniffed_packet))
    _l_(381614)


def process_sniffed_packet(packet):
    _l_(381626)

    if _c_(381620, _a_(381617, _n_(381616, "packet", lambda: packet), "haslayer"), _a_(381619, _n_(381618, "http", lambda: http), "HTTPRequest")):
        _l_(381625)

        _c_(381623, _n_(381621, "print", lambda: print), _n_(381622, "packet", lambda: packet))
        _l_(381624)


_c_(381628, _n_(381627, "sniff", lambda: sniff), "eth0")
_l_(381629)