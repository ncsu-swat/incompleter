# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55593541/getting-a-nameerror-in-an-if-else-statement-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ld = 2
_l_(338003)
rd = 0
_l_(338004)
hd = 1
_l_(338005)
vhd = 1
_l_(338006)

if(_n_(338007, "rd", lambda: rd)>= 1):
    _l_(338036)

    rt = (4*_n_(338008, "rd", lambda: rd)) + 2
    _l_(338009)

elif(_n_(338010, "hd", lambda: hd)>=1 and _n_(338011, "rd", lambda: rd)==0):
    _l_(338035)

    st = (4*_n_(338012, "hd", lambda: hd) + 2)
    _l_(338013)

elif(_n_(338014, "ld", lambda: ld)>=1 and _n_(338015, "rd", lambda: rd)==0 and _n_(338016, "hd", lambda: hd)==0):
    _l_(338034)

    lt = (4*_n_(338017, "ld", lambda: ld) + 2)
    _l_(338018)

elif(_n_(338019, "ld", lambda: ld)>=1):
    _l_(338033)

    lt = 4*_n_(338020, "ld", lambda: ld)
    _l_(338021)

elif(_n_(338022, "hd", lambda: hd)>=1):
    _l_(338032)

    st = _n_(338023, "hd", lambda: hd)
    _l_(338024)

elif(_n_(338025, "vhd", lambda: vhd)>=1):
    _l_(338031)

    spt = _n_(338026, "vhd", lambda: vhd)
    _l_(338027)

else: 
    _c_(338029, _n_(338028, "print", lambda: print), 'Error!')
    _l_(338030)

_c_(338039, _n_(338037, "print", lambda: print), _n_(338038, "spt", lambda: spt))
_l_(338040)