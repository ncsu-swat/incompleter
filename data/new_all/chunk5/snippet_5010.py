# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17093400/cx-freeze-yields-nameerror-name-build-exe-options-is-not-defined-on-build-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(667852)

except ImportError:
    pass
try:
    from cx_Freeze import setup, Executable
    _l_(667854)

except ImportError:
    pass

_c_(667860, _n_(667855, "setup", lambda: setup), name = "Duplicate Finder x86",
    version = "1.0",
    description = "Duplicate Finder x86",
    options = {"build_exe": _n_(667856, "build_exe_options", lambda: build_exe_options)},
    executables = [_c_(667859, _n_(667857, "Executable", lambda: Executable), "Comparator Source.py", base=_n_(667858, "base", lambda: base))])
_l_(667861)