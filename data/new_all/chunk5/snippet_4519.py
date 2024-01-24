# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56347107/nameerror-name-values-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(649283)

except ImportError:
    pass
...
_l_(649284)

class Car(_a_(649286, _n_(649285, "models", lambda: models), "Model"), _n_(649287, "values", lambda: values)):
    _l_(649295)

    name = _c_(649290, _a_(649289, _n_(649288, "models", lambda: models), "CharField"), max_length=200)
    _l_(649291)
    brand = values['brand']
    _l_(649292)
    year = values['year']
    _l_(649293)
    mpg = values['mpg']
    _l_(649294)