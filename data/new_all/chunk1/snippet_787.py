# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53092781/why-does-my-scan-function-from-the-python-nmap-module-show-str-attribute-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import nmap
    _l_(399369)

except ImportError:
    pass
ns = _a_(399371, _n_(399370, "nmap", lambda: nmap), "PortScanner")
_l_(399372)
_c_(399375, _a_(399374, _n_(399373, "ns", lambda: ns), "scan"), 'My.IP.Add.ress', '1-1024', '-v')
_l_(399376)
_c_(399381, _n_(399377, "print", lambda: print), _c_(399380, _a_(399379, _n_(399378, "ns", lambda: ns), "scaninfo")))
_l_(399382)