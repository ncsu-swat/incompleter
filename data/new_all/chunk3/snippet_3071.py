# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49347840/python-3-on-windows-typeerror-an-integer-is-required-got-type-str
#!/usr/bin/env python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys, os, socket
    _l_(545140)

except ImportError:
    pass

def SCAN_TCP_PORT():
    _l_(545171)

    DstIP = _c_(545142, _n_(545141, "input", lambda: input), '\nDestination IP Address: ')
    _l_(545143)
    DstPort = _c_(545145, _n_(545144, "input", lambda: input), 'Port number: ')
    _l_(545146)
    _c_(545150, _n_(545147, "print", lambda: print), 'Host %s port %s' % (_n_(545148, "DstIP", lambda: DstIP), _n_(545149, "DstPort", lambda: DstPort)))
    _l_(545151)
    s = _c_(545158, _a_(545153, _n_(545152, "socket", lambda: socket), "socket"), _a_(545155, _n_(545154, "socket", lambda: socket), "AF_INET"), _a_(545157, _n_(545156, "socket", lambda: socket), "SOCK_STREAM"))
    _l_(545159)
    _c_(545164, _a_(545161, _n_(545160, "s", lambda: s), "connect"), (_n_(545162, "DstIP", lambda: DstIP), _n_(545163, "DstPort", lambda: DstPort)))
    _l_(545165)
    _c_(545169, _n_(545166, "print", lambda: print), "%s is listening on TCP port %s" % (_n_(545167, "DstIP", lambda: DstIP), _n_(545168, "DstPort", lambda: DstPort)))
    _l_(545170)

_c_(545173, _n_(545172, "SCAN_TCP_PORT", lambda: SCAN_TCP_PORT))
_l_(545174)