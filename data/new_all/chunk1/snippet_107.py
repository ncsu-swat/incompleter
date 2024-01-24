# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56898620/typeerror-expected-str-bytes-or-os-pathlike-object-not-none-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(377892)

except ImportError:
    pass
try:
    import time
    _l_(377894)

except ImportError:
    pass
file_path = _c_(377901, _a_(377897, _a_(377896, _n_(377895, "os", lambda: os), "path"), "join"), _c_(377900, _a_(377899, _n_(377898, "os", lambda: os), "getenv"), "HOME"), "birth_day_lookup.txt")
_l_(377902)


def check_birthday():
    _l_(377934)


    lookup_file = _c_(377905, _n_(377903, "open", lambda: open), _n_(377904, "file_path", lambda: file_path), 'r')
    _l_(377906)
    today = _c_(377909, _a_(377908, _n_(377907, "time", lambda: time), "strftime"), '%d-%B')
    _l_(377910)
    flag = 0
    _l_(377911)
    for entry in _n_(377912, "lookup_file", lambda: lookup_file):
        _l_(377927)

        if _n_(377913, "today", lambda: today) in _n_(377914, "entry", lambda: entry):
            _l_(377926)

            line = _c_(377917, _a_(377916, _n_(377915, "entry", lambda: entry), "split"), ' ')
            _l_(377918)
            flag = 1
            _l_(377919)
            _c_(377924, _a_(377921, _n_(377920, "os", lambda: os), "system"), 'notify-send "Today is '+_n_(377922, "line", lambda: line)[1]+' '+_n_(377923, "line", lambda: line)[2]+'\'s Birthday"')
            _l_(377925)
    if _n_(377928, "flag", lambda: flag) == 0:
        _l_(377933)

        _c_(377931, _a_(377930, _n_(377929, "os", lambda: os), "system"), 'notify-send "No birthday for today is listed"')
        _l_(377932)

_c_(377936, _n_(377935, "check_birthday", lambda: check_birthday))
_l_(377937)