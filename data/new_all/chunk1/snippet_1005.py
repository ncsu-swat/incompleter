# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57203454/why-does-python-raise-a-nameerror-for-conditional-list-comprehensions-inside-cla
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import namedtuple
    _l_(386697)

except ImportError:
    pass

class StateDatabase:
    _l_(386705)

    State = _c_(386699, _n_(386698, "namedtuple", lambda: namedtuple), 'State', ['name', 'capital'])
    _l_(386700)
    db = [_c_(386703, _n_(386701, "State", lambda: State), *_n_(386702, "args", lambda: args)) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]
    _l_(386704)