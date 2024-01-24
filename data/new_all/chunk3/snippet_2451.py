# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21957653/typeerror-when-using-cxfreeze
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(567579)

except ImportError:
    pass
try:
    from cx_Freeze import setup, Executable
    _l_(567581)

except ImportError:
    pass


exe = _c_(567583, _n_(567582, "Executable", lambda: Executable), script = 'cornell7.py',
    targetName = 'cornell7.exe',
    packages = ['header2.py'],
    targetDir = 'executable_dir',
    includes = [    'urllib.request', 'socket', 'sys', 'string', 'threading', 'time','datetime'],
    copyDependentFiles = True
    )
_l_(567584)
_c_(567587, _n_(567585, "setup", lambda: setup), name = 'cornell7.exe',
          executables = [_n_(567586, "exe", lambda: exe)]
     )
_l_(567588)