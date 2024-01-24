# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65410481/filenotfounderror-errno-2-no-such-file-or-directory-bliblibc-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scapy.all as scapy
    _l_(390286)

except ImportError:
    pass
def scan(ip):
    _l_(390292)

    _c_(390290, _a_(390288, _n_(390287, "scapy", lambda: scapy), "arping"), _n_(390289, "ip", lambda: ip))
    _l_(390291)
_c_(390294, _n_(390293, "scan", lambda: scan), "192.168.196.0")
_l_(390295)