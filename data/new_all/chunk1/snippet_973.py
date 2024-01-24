# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61211424/python-cx-freeze-filenotfounderror-errno-2-in-library-zip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from cx_Freeze import setup, Executable
    _l_(407508)

except ImportError:
    pass
includefiles = ['table.csv']
_l_(407509)
zipincludes = ['table.csv']
_l_(407510)
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = _c_(407514, _n_(407511, "dict", lambda: dict), packages = [], excludes = [], include_files = _n_(407512, "includefiles", lambda: includefiles), zip_includes = _n_(407513, "zipincludes", lambda: zipincludes))
_l_(407515)
include_package_data=True
_l_(407516)
base = 'Console'
_l_(407517)

executables = [
    _c_(407520, _n_(407518, "Executable", lambda: Executable), 'ReportGenerator.py', base=_n_(407519, "base", lambda: base), targetName = 'report_generator')
]
_l_(407521)

_c_(407527, _n_(407522, "setup", lambda: setup), name='test13',
    version = '1.0',
    description = 'test13',
    options = _c_(407525, _n_(407523, "dict", lambda: dict), build_exe = _n_(407524, "buildOptions", lambda: buildOptions)),
    executables = _n_(407526, "executables", lambda: executables))
_l_(407528)