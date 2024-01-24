# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57987388/typeerror-unsupported-operand-types-for-str-and-str-how-to-solve-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wmi
    _l_(343666)

except ImportError:
    pass
c = _c_(343669, _a_(343668, _n_(343667, "wmi", lambda: wmi), "WMI"))
_l_(343670)

for process in _c_(343673, _a_(343672, _n_(343671, "c", lambda: c), "Win32_Process")):
    _l_(343684)

    #print (process.Name)
    if _a_(343675, _n_(343674, "process", lambda: process), "Name") == "chrome.exe" & _a_(343677, _n_(343676, "process", lambda: process), "Name") > 1:
        _l_(343683)

        _c_(343681, _n_(343678, "print", lambda: print), _a_(343680, _n_(343679, "process", lambda: process), "Name"))
        _l_(343682)