# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53620627/python-from-import-works-but-import-throws-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(707600)

except ImportError:
    pass
try:
    import k8s.instance
    _l_(707602)

except ImportError:
    pass
try:
    from k8s.projects_v2 import Projects
    _l_(707604)

except ImportError:
    pass
try:
    from typing import Union
    _l_(707606)

except ImportError:
    pass

CELL_KEY: _n_(707607, "str", lambda: str) = 'cell'
_l_(707608)

CELLS_KEY: _n_(707609, "str", lambda: str) = 'cells'
_l_(707610)

EXTENDS_KEY: _n_(707611, "str", lambda: str) = 'extends'
_l_(707612)


_logging = _c_(707616, _a_(707614, _n_(707613, "logging", lambda: logging), "getLogger"), _n_(707615, "__name__", lambda: __name__))
_l_(707617)


class Cell(_a_(707619, _a_(707618, k8s, "instance"), "Instance")):
    _l_(707629)


    def __init__(self):
        _l_(707628)

        _c_(707622, _a_(707621, _n_(707620, "super", lambda: super)(), "__init__"))
        _l_(707623)

        _n_(707624, "self", lambda: self).__projects = _c_(707626, _n_(707625, "Projects", lambda: Projects))
        _l_(707627)