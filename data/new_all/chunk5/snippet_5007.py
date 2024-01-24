# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17093400/cx-freeze-yields-nameerror-name-build-exe-options-is-not-defined-on-build-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(687709)

except ImportError:
    pass
try:
    from cx_Freeze import setup, Executable
    _l_(687711)

except ImportError:
    pass

_c_(687717, _n_(687712, "setup", lambda: setup), name = "Duplicate Finder x86",
    version = "1.0",
    description = "Duplicate Finder x86",
    options = {"build_exe": _n_(687713, "build_exe_options", lambda: build_exe_options)},
    executables = [_c_(687716, _n_(687714, "Executable", lambda: Executable), "Comparator Source.py", base=_n_(687715, "base", lambda: base))])
_l_(687718)