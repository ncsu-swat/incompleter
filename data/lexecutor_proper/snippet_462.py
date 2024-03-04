# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import inspect
    _l_(63131)

except ImportError:
    pass
method_names = [_n_(63132, "attr", lambda: attr) for attr in _c_(63135, _n_(63133, "dir", lambda: dir), _n_(63134, "self", lambda: self)) if _c_(63142, _a_(63137, _n_(63136, "inspect", lambda: inspect), "ismethod"), _c_(63141, _n_(63138, "getattr", lambda: getattr), _n_(63139, "self", lambda: self), _n_(63140, "attr", lambda: attr)))]
_l_(63143)
try:
    import inspect
    _l_(63145)

except ImportError:
    pass
methods = [_n_(63146, "member", lambda: member) for member in [_c_(63150, _n_(63147, "getattr", lambda: getattr), _n_(63148, "self", lambda: self), _n_(63149, "attr", lambda: attr)) for attr in _c_(63153, _n_(63151, "dir", lambda: dir), _n_(63152, "self", lambda: self))] if _c_(63157, _a_(63155, _n_(63154, "inspect", lambda: inspect), "ismethod"), _n_(63156, "member", lambda: member))]
_l_(63158)

