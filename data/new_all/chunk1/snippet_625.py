# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50716931/unittest-mock-and-multiple-inheritance-typeerror-metaclass-conflict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(404646)

except ImportError:
    pass
try:
    from unittest import mock
    _l_(404648)

except ImportError:
    pass

# inspired by https://stackoverflow.com/a/37363830/1860757
MOCK_MODULES = ['class_a', ]
_l_(404649)
_c_(404658, _a_(404652, _a_(404651, _n_(404650, "sys", lambda: sys), "modules"), "update"), ((_n_(404653, "mod_name", lambda: mod_name), _c_(404656, _a_(404655, _n_(404654, "mock", lambda: mock), "MagicMock"))) for mod_name in _n_(404657, "MOCK_MODULES", lambda: MOCK_MODULES)))
_l_(404659)
try:
    import code
    _l_(404661)

except ImportError:
    pass

_c_(404664, _a_(404663, _n_(404662, "code", lambda: code), "C"))
_l_(404665)