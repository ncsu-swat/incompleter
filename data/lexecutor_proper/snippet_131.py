# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
## Standalone boilerplate before relative imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(61766, "__package__", lambda: __package__) is None:
    _l_(61786)

    DIR = _a_(61772, _c_(61771, _a_(61770, _c_(61769, _n_(61767, "Path", lambda: Path), _n_(61768, "__file__", lambda: __file__)), "resolve")), "parent")
    _l_(61773)
    _c_(61781, _a_(61776, _a_(61775, _n_(61774, "sys", lambda: sys), "path"), "insert"), 0, _c_(61780, _n_(61777, "str", lambda: str), _a_(61779, _n_(61778, "DIR", lambda: DIR), "parent")))
    _l_(61782)
    __package__ = _a_(61784, _n_(61783, "DIR", lambda: DIR), "name")
    _l_(61785)
try:
    from . import variable_in__init__py
    _l_(61788)

except ImportError:
    pass
try:
    from . import other_module_in_package
    _l_(61790)

except ImportError:
    pass

