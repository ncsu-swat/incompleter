# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53620627/python-from-import-works-but-import-throws-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(686160)

except ImportError:
    pass
try:
    import k8s.instance
    _l_(686162)

except ImportError:
    pass
try:
    import k8s.projects_v2
    _l_(686164)

except ImportError:
    pass
try:
    from typing import Union
    _l_(686166)

except ImportError:
    pass

CELL_KEY: _n_(686167, "str", lambda: str) = 'cell'
_l_(686168)

CELLS_KEY: _n_(686169, "str", lambda: str) = 'cells'
_l_(686170)

EXTENDS_KEY: _n_(686171, "str", lambda: str) = 'extends'
_l_(686172)


_logging = _c_(686176, _a_(686174, _n_(686173, "logging", lambda: logging), "getLogger"), _n_(686175, "__name__", lambda: __name__))
_l_(686177)


class Cell(_a_(686179, _a_(686178, k8s, "instance"), "Instance")):
    _l_(686190)


    def __init__(self):
        _l_(686189)

        _c_(686182, _a_(686181, _n_(686180, "super", lambda: super)(), "__init__"))
        _l_(686183)

        _n_(686184, "self", lambda: self).__projects = _c_(686187, _a_(686186, _a_(686185, k8s, "projects_v2"), "Projects"))
        _l_(686188)