# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64816277/why-do-i-get-a-nameerror-name-orientation-is-not-defined-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import namedtuple
    _l_(406095)

except ImportError:
    pass

class StateDatabase:
    _l_(406103)

    State = _c_(406097, _n_(406096, "namedtuple", lambda: namedtuple), 'State', ['name', 'capital'])
    _l_(406098)
    db = [_c_(406101, _n_(406099, "State", lambda: State), *_n_(406100, "args", lambda: args)) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]
    _l_(406102)