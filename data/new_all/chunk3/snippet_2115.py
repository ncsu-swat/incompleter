# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62977585/im-getting-a-error-when-i-run-my-setup-py-on-cx-freeze-typeerror-expected-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cx_Freeze
    _l_(533302)

except ImportError:
    pass
try:
    import sys
    _l_(533304)

except ImportError:
    pass
try:
    import pandas
    _l_(533306)

except ImportError:
    pass
try:
    import numpy
    _l_(533308)

except ImportError:
    pass

base = None
_l_(533309)

if _a_(533311, _n_(533310, "sys", lambda: sys), "platform") == 'win32':
    _l_(533313)

    base = "Win32GUI"
    _l_(533312)

executables = [_c_(533317, _a_(533315, _n_(533314, "cx_Freeze", lambda: cx_Freeze), "Executable"), "app.py", base=_n_(533316, "base", lambda: base), icon="myicon.ico")]
_l_(533318)

_c_(533322, _a_(533320, _n_(533319, "cx_Freeze", lambda: cx_Freeze), "setup"), name = "Correlation-Generator",
    options = {"build_exe": {"packages":["tkinter","pandas","numpy"], "include_files":["myicon.ico"]}},
    version = "0.01",
    description = "A GUI Application which takes in metrics for generating a correlation value",
    executables = _n_(533321, "executables", lambda: executables)
    )
_l_(533323)