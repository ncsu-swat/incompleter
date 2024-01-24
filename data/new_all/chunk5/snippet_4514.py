# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56347107/nameerror-name-values-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(694884)

except ImportError:
    pass
...
_l_(694885)

class Car(_a_(694887, _n_(694886, "models", lambda: models), "Model"), _n_(694888, "values", lambda: values)):
    _l_(694896)

    name = _c_(694891, _a_(694890, _n_(694889, "models", lambda: models), "CharField"), max_length=200)
    _l_(694892)
    brand = values['brand']
    _l_(694893)
    year = values['year']
    _l_(694894)
    mpg = values['mpg']
    _l_(694895)