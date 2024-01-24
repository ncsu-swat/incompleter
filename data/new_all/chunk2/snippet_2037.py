# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67953308/python-pywin32-typeerror-there-is-no-interface-object-registered-that-supports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pythoncom
    _l_(458779)

except ImportError:
    pass
try:
    import pywintypes
    _l_(458781)

except ImportError:
    pass


clsid = _c_(458784, _a_(458783, _n_(458782, "pywintypes", lambda: pywintypes), "IID"), '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}')  # CLSID_ShellWindow
_l_(458785)  # CLSID_ShellWindow
iid = _c_(458788, _a_(458787, _n_(458786, "pywintypes", lambda: pywintypes), "IID"), '{85CB6900-4D95-11CF-960C-0080C7F4EE85}')  # IID_IShellWindow
_l_(458789)  # IID_IShellWindow
_c_(458796, _a_(458791, _n_(458790, "pythoncom", lambda: pythoncom), "CoCreateInstance"), _n_(458792, "clsid", lambda: clsid), None, _a_(458794, _n_(458793, "pythoncom", lambda: pythoncom), "CLSCTX_ALL"), _n_(458795, "iid", lambda: iid))
_l_(458797)