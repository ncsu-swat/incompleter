# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61776922/python-3-exec-method-nameerror-name-of-a-defined-function-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filename = "./vir.py"
_l_(400489)
vir_globals = { "uc": 42, "cs": 12, "cycleOffset": -1 }
_l_(400490)

with _c_(400493, _n_(400491, "open", lambda: open), _n_(400492, "filename", lambda: filename), "rb") as source_file:
    _l_(400501)

    code = _c_(400499, _n_(400494, "compile", lambda: compile), _c_(400497, _a_(400496, _n_(400495, "source_file", lambda: source_file), "read")), _n_(400498, "filename", lambda: filename), "exec")
    _l_(400500)

_c_(400505, _n_(400502, "exec", lambda: exec), _n_(400503, "code", lambda: code), _n_(400504, "vir_globals", lambda: vir_globals), {} )
_l_(400506)

_c_(400509, _n_(400507, "print", lambda: print), 'exec: globals.cycleOffset', _n_(400508, "vir_globals", lambda: vir_globals)['cycleOffset'] )
_l_(400510)