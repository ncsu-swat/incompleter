# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76920172/attributeerror-module-pycaret-has-no-attribute-utils
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pycaret.classification import ClassificationExperiment
    _l_(607151)

except ImportError:
    pass
s = _c_(607153, _n_(607152, "ClassificationExperiment", lambda: ClassificationExperiment))
_l_(607154)
_c_(607158, _a_(607156, _n_(607155, "s", lambda: s), "setup"), _n_(607157, "data", lambda: data), target = 'Class variable', session_id = 123)
_l_(607159)