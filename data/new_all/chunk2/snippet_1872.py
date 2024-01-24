# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45906514/attribute-error-while-using-cx-freeze
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cx_Freeze
    _l_(426987)

except ImportError:
    pass
try:
    import os
    _l_(426989)

except ImportError:
    pass

_a_(426991, _n_(426990, "os", lambda: os), "environ")['TCL_LIBRARY'] = "C:\\Users\Vinayak Singla\\Appdata\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
_l_(426992)
_a_(426994, _n_(426993, "os", lambda: os), "environ")['TK_LIBRARY'] = "C:\\Users\Vinayak Singla\\Appdata\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
_l_(426995)

executables = [_c_(426998, _a_(426997, _n_(426996, "cx_Freeze", lambda: cx_Freeze), "Executable"), "pong.py")]
_l_(426999)

_c_(427003, _a_(427001, _n_(427000, "cx_Freeze", lambda: cx_Freeze), "setup"), name="Pongy",
    options={"build_exe": {"packages":["pygame","sys","random","time"],"include_files":["boing.wav","out.wav"]}},
    executables = _n_(427002, "executables", lambda: executables)
)
_l_(427004)