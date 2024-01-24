# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75358233/ctypes-argumenterror-argument-1-typeerror-dont-know-how-to-convert-parameter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ctypes
    _l_(601602)

except ImportError:
    pass
try:
    import win32security
    _l_(601604)

except ImportError:
    pass

h_token = _c_(601614, _a_(601606, _n_(601605, "win32security", lambda: win32security), "OpenProcessToken"), _c_(601611, _a_(601610, _a_(601609, _a_(601608, _n_(601607, "ctypes", lambda: ctypes), "windll"), "kernel32"), "GetCurrentProcess")), _a_(601613, _n_(601612, "win32security", lambda: win32security), "TOKEN_ALL_ACCESS"))
_l_(601615)

lpApplicationName = _c_(601618, _a_(601617, _n_(601616, "ctypes", lambda: ctypes), "c_wchar_p"), rf"C:\\Windows\\System32\\cmd.exe")
_l_(601619)
lpCommandLine = _c_(601622, _a_(601621, _n_(601620, "ctypes", lambda: ctypes), "c_wchar_p"), "")
_l_(601623)
dwCreationFlags = 0x00000010
_l_(601624)
lpEnvironment = None
_l_(601625)
lpProcessAttributes = None
_l_(601626)
lpThreadAttributes = None
_l_(601627)
bInheritHandles = False
_l_(601628)

_c_(601641, _a_(601632, _a_(601631, _a_(601630, _n_(601629, "ctypes", lambda: ctypes), "windll"), "advapi32"), "CreateProcessWithTokenW"), _n_(601633, "h_token", lambda: h_token), 0, _n_(601634, "lpApplicationName", lambda: lpApplicationName), _n_(601635, "lpCommandLine", lambda: lpCommandLine), _n_(601636, "dwCreationFlags", lambda: dwCreationFlags), _n_(601637, "lpEnvironment", lambda: lpEnvironment), None, _n_(601638, "lpProcessAttributes", lambda: lpProcessAttributes), _n_(601639, "lpThreadAttributes", lambda: lpThreadAttributes), _n_(601640, "bInheritHandles", lambda: bInheritHandles))
_l_(601642)