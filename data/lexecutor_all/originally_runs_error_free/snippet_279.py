# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime, time
    _l_(1544930)

except ImportError:
    pass
ls = ['31/1/2007', '14/2/2017']
_l_(1544931)
for d in _n_(1544932, "ls", lambda: ls):
    _l_(1544949)

    dt = _c_(1544937, _a_(1544935, _a_(1544934, _n_(1544933, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(1544936, "d", lambda: d), "%d/%m/%Y")
    _l_(1544938)
    _c_(1544941, _n_(1544939, "print", lambda: print), _n_(1544940, "dt", lambda: dt))
    _l_(1544942)
    _c_(1544947, _n_(1544943, "print", lambda: print), _c_(1544946, _a_(1544945, _n_(1544944, "dt", lambda: dt), "strftime"), "%A"))
    _l_(1544948)

