# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41058857/python-list-comprehension-causes-nameerror-when-assigned-to-static-varible
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import namedtuple
    _l_(447330)

except ImportError:
    pass

class StateDatabase:
    _l_(447338)

    State = _c_(447332, _n_(447331, "namedtuple", lambda: namedtuple), 'State', ['name', 'capital'])
    _l_(447333)
    db = [_c_(447336, _n_(447334, "State", lambda: State), *_n_(447335, "args", lambda: args)) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]
    _l_(447337)