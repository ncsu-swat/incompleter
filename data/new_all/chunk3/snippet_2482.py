# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76101117/attributeerror-module-prtscnr-has-no-attribute-portscanner
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import prtscnr
    _l_(560222)

except ImportError:
    pass

def menu():
    _l_(560252)

    _c_(560224, _n_(560223, "print", lambda: print), "****** Recon ******")
    _l_(560225)
    _c_(560227, _n_(560226, "print", lambda: print), "1- PortScanner")
    _l_(560228)
    _c_(560230, _n_(560229, "print", lambda: print), "2- Subdomain Finder")
    _l_(560231)
    _c_(560233, _n_(560232, "print", lambda: print), "3- Hash Decryption ")
    _l_(560234)
    _c_(560236, _n_(560235, "print", lambda: print), "4- Çıkış ")
    _l_(560237)
    msecim = _c_(560241, _n_(560238, "int", lambda: int), _c_(560240, _n_(560239, "input", lambda: input), "Seçimini yap: "))
    _l_(560242)
    if _n_(560243, "msecim", lambda: msecim) == 1 :
        _l_(560251)

        _c_(560245, _n_(560244, "print", lambda: print), "Portscanner'a hoşgeldin...")
        _l_(560246)
        _c_(560249, _a_(560248, _n_(560247, "prtscnr", lambda: prtscnr), "portscanner"))
        _l_(560250)