# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72340707/python-namedtuple-attributeerror-tuple-object-has-no-attribute-end-pos
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import namedtuple
    _l_(542171)

except ImportError:
    pass

class Parser:
    _l_(542175)

    Rule = _c_(542173, _n_(542172, "namedtuple", lambda: namedtuple), 'Rule', ['lhs', 'rhs', 'dot_pos', 'start_pos', 'end_pos'])
    _l_(542174)