# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(63709)

    _c_(63704, _n_(63703, "do_something", lambda: do_something))
    _l_(63705)
except _n_(63706, "Exception", lambda: Exception):
    _l_(63708)

    pass
    _l_(63707)

try:
    _l_(63719)

    _c_(63711, _n_(63710, "do_something", lambda: do_something))
    _l_(63712)
except _n_(63713, "Exception", lambda: Exception):
    _l_(63718)

    _c_(63716, _a_(63715, _n_(63714, "sys", lambda: sys), "exc_clear"))
    _l_(63717)

