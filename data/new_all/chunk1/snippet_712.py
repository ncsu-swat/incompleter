# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50214624/nonetype-error-converting-opengl-script-from-py-to-exe-using-cx-freeze
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(394434)

except ImportError:
    pass
try:
    from cx_Freeze import setup, Executable
    _l_(394436)

except ImportError:
    pass
#go to dir in cmd, run python setup.py build or; setup.py build... will create a folder build with name.exe
_c_(394440, _n_(394437, "setup", lambda: setup), name = "Cube",
    version = "1.1",
    description = "Cube",
    executables = [_c_(394439, _n_(394438, "Executable", lambda: Executable), "OwnCube.py", base = "Console")])
_l_(394441)