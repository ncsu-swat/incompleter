# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61816692/what-should-i-dotypeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(541554)

except ImportError:
    pass

ffail = ""
_l_(541555)
with _c_(541557, _n_(541556, "open", lambda: open), "regex_sum_340933.txt", "r" , "UTF-8") as some_file:
    _l_(541562)

    ffail = _c_(541560, _a_(541559, _n_(541558, "some_file", lambda: some_file), "read"))
    _l_(541561)
count = 0
_l_(541563)

match = _c_(541567, _a_(541565, _n_(541564, "re", lambda: re), "findall"), '[0-9]+', _n_(541566, "ffail", lambda: ffail))
_l_(541568)

for II in _n_(541569, "match", lambda: match):
    _l_(541577)

    number = _c_(541572, _n_(541570, "int", lambda: int), _n_(541571, "II", lambda: II))
    _l_(541573)
    count = _n_(541574, "count", lambda: count) + _n_(541575, "number", lambda: number)
    _l_(541576)
_c_(541580, _n_(541578, "print", lambda: print), _n_(541579, "count", lambda: count))
_l_(541581)