# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66258583/mypy-cannot-detect-nameerror-undefined-variable-unresolved-reference-within-a-fu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def configure():
    _l_(600614)

    _n_(600612, "undefined_obj", lambda: undefined_obj).length = 10  # expect NameError: name 'undefined_car' is not defined
    _l_(600613)  # expect NameError: name 'undefined_car' is not defined

_c_(600616, _n_(600615, "configure", lambda: configure))
_l_(600617)