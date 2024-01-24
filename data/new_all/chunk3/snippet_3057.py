# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51105996/scapy-attributeerror-nonetype-object-has-no-attribute-getlayer
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(566536)

except ImportError:
    pass
_c_(566543, _a_(566540, _c_(566539, _a_(566538, _n_(566537, "logging", lambda: logging), "getLogger"), "scapy.runtime"), "setLevel"), _a_(566542, _n_(566541, "logging", lambda: logging), "ERROR"))
_l_(566544)
try:
    from scapy.all import *
    _l_(566546)

except ImportError:
    pass

def portscan(host,dst_port):
    _l_(566594)

    src_port = _c_(566548, _n_(566547, "RandShort", lambda: RandShort))
    _l_(566549)
    SYNACK = 0x12
    _l_(566550)
    RSTACK = 0x14
    _l_(566551)
    tcp_connect = _c_(566560, _n_(566552, "sr1", lambda: sr1), _c_(566555, _n_(566553, "IP", lambda: IP), dst=_n_(566554, "host", lambda: host))/_c_(566559, _n_(566556, "TCP", lambda: TCP), sport=_n_(566557, "src_port", lambda: src_port),dport=_n_(566558, "dst_port", lambda: dst_port),flags="S"),verbose=0,timeout=2)
    _l_(566561)

    if(_a_(566566, _c_(566565, _a_(566563, _n_(566562, "tcp_connect", lambda: tcp_connect), "getlayer"), _n_(566564, "TCP", lambda: TCP)), "flags") == _n_(566567, "SYNACK", lambda: SYNACK)):
        _l_(566593)

        send_rst = _c_(566576, _n_(566568, "sr", lambda: sr), _c_(566571, _n_(566569, "IP", lambda: IP), dst=_n_(566570, "host", lambda: host))/_c_(566575, _n_(566572, "TCP", lambda: TCP), sport=_n_(566573, "src_port", lambda: src_port),dport=_n_(566574, "dst_port", lambda: dst_port),flags="AR"),verbose=0,timeout=2)
        _l_(566577)
        _c_(566580, _n_(566578, "print", lambda: print), _n_(566579, "dst_port", lambda: dst_port),"is open")
        _l_(566581)

    elif (_a_(566586, _c_(566585, _a_(566583, _n_(566582, "tcp_connect", lambda: tcp_connect), "getlayer"), _n_(566584, "TCP", lambda: TCP)), "flags") == _n_(566587, "RSTACK", lambda: RSTACK)):
        _l_(566592)

        _c_(566590, _n_(566588, "print", lambda: print), _n_(566589, "dst_port", lambda: dst_port),"is closed")
        _l_(566591)

if _n_(566595, "__name__", lambda: __name__) == '__main__':
    _l_(566603)

    host = '192.168.0.40'
    _l_(566596)
    port = 80
    _l_(566597)
    _c_(566601, _n_(566598, "portscan", lambda: portscan), _n_(566599, "host", lambda: host),_n_(566600, "port", lambda: port))
    _l_(566602)