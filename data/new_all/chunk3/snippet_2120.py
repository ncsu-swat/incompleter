# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62953908/attributeerror-tuple-object-has-no-attribute-get-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(522997)

except ImportError:
    pass

# Create your models here.
class ModelClas(_a_(522999, _n_(522998, "models", lambda: models), "Model")):
    _l_(523024)

    fname = _c_(523002, _a_(523001, _n_(523000, "models", lambda: models), "CharField"), max_length=30)
    _l_(523003)
    lname = _c_(523006, _a_(523005, _n_(523004, "models", lambda: models), "CharField"), max_length=30)
    _l_(523007)
    email = _c_(523010, _a_(523009, _n_(523008, "models", lambda: models), "EmailField"))
    _l_(523011)
    mobile = _c_(523014, _a_(523013, _n_(523012, "models", lambda: models), "IntegerField"))
    _l_(523015)
    passw = _c_(523018, _a_(523017, _n_(523016, "models", lambda: models), "CharField"), max_length=30)
    _l_(523019)
    repass = _c_(523022, _a_(523021, _n_(523020, "models", lambda: models), "CharField"), max_length=30)
    _l_(523023)