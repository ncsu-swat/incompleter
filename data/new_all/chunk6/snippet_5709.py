# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57987388/typeerror-unsupported-operand-types-for-str-and-str-how-to-solve-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wmi
    _l_(360764)

except ImportError:
    pass
c = _c_(360767, _a_(360766, _n_(360765, "wmi", lambda: wmi), "WMI"))
_l_(360768)

for process in _c_(360771, _a_(360770, _n_(360769, "c", lambda: c), "Win32_Process")):
    _l_(360782)

    #print (process.Name)
    if _a_(360773, _n_(360772, "process", lambda: process), "Name") == "chrome.exe" & _a_(360775, _n_(360774, "process", lambda: process), "Name") > 1:
        _l_(360781)

        _c_(360779, _n_(360776, "print", lambda: print), _a_(360778, _n_(360777, "process", lambda: process), "Name"))
        _l_(360780)