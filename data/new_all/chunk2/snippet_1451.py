# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56915197/attributeerror-str-object-has-no-attribute-sleep
#!/usr/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(474407)

except ImportError:
    pass
try:
    import json
    _l_(474409)

except ImportError:
    pass
try:
    import datetime
    _l_(474411)

except ImportError:
    pass
try:
    import cgi
    _l_(474413)

except ImportError:
    pass
try:
    import time
    _l_(474415)

except ImportError:
    pass

def save(number_input, current_time):
    _l_(474441)

    i = 0
    _l_(474416)
    while _c_(474423, _a_(474419, _a_(474418, _n_(474417, "os", lambda: os), "path"), "exists"), _c_(474422, _a_(474420, "datei/datei{}.txt", "format"), _n_(474421, "i", lambda: i))):
        _l_(474425)

        i += 1
        _l_(474424)

    datei = {
        "input": _n_(474426, "number_input", lambda: number_input),
        "zeit": _n_(474427, "current_time", lambda: current_time)
    }
    _l_(474428)

    with _c_(474433, _n_(474429, "open", lambda: open), _c_(474432, _a_(474430, "datei/datei{}.txt", "format"), _n_(474431, "i", lambda: i)), "w+") as file:
        _l_(474440)

        _c_(474438, _a_(474435, _n_(474434, "json", lambda: json), "dump"), _n_(474436, "datei", lambda: datei), _n_(474437, "file", lambda: file))
        _l_(474439)

form = _c_(474444, _a_(474443, _n_(474442, "cgi", lambda: cgi), "FieldStorage"), encoding="utf-8")
_l_(474445)

number = _c_(474448, _a_(474447, _n_(474446, "form", lambda: form), "getvalue"), "first")
_l_(474449)
time = _c_(474455, _a_(474454, _c_(474453, _a_(474452, _a_(474451, _n_(474450, "datetime", lambda: datetime), "datetime"), "today")), "strftime"), "%d.%m.%Y %H:%M:%S")
_l_(474456)

_c_(474460, _n_(474457, "save", lambda: save), _n_(474458, "number", lambda: number), _n_(474459, "time", lambda: time))
_l_(474461)

_c_(474466, _n_(474462, "print", lambda: print), _c_(474465, _a_(474463, "<p>Sie haben {} in einer .txt Datei gespeichert!              </p>", "format"), _n_(474464, "number", lambda: number)))                              
_l_(474467)                              
_c_(474470, _a_(474469, _n_(474468, "time", lambda: time), "sleep"), 4)
_l_(474471)
_c_(474473, _n_(474472, "print", lambda: print), "Location: main.py")
_l_(474474)
_c_(474476, _n_(474475, "print", lambda: print))
_l_(474477)