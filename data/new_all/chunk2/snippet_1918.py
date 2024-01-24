# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32247006/python-attributeerror-module-object-has-no-attribute-goslate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import goslate
    _l_(437259)

except ImportError:
    pass
gs = _c_(437262, _a_(437261, _n_(437260, "goslate", lambda: goslate), "Goslate"))
_l_(437263)
_c_(437268, _n_(437264, "print", lambda: print), _c_(437267, _a_(437266, _n_(437265, "gs", lambda: gs), "translate"), 'hello world', 'bn'))
_l_(437269)