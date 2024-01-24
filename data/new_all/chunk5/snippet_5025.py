# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57213890/python-nmap-typeerror-list-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import nmap
    _l_(671854)

except ImportError:
    pass
nm_scan = _c_(671857, _a_(671856, _n_(671855, "nmap", lambda: nmap), "PortScanner"))
_l_(671858)
nm_scanner = _c_(671861, _a_(671860, _n_(671859, "nm_scan", lambda: nm_scan), "scan"), '192.168.0.1', '80', arguments='-O')
_l_(671862)
_c_(671865, _n_(671863, "print", lambda: print), "Portid: " + _n_(671864, "nm_scanner", lambda: nm_scanner)['scan']['192.168.0.1']['portused']['portid'])
_l_(671866)