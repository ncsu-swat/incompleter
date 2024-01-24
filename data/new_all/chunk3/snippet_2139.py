# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61720078/django-typeerror-tuple-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(562374)

except ImportError:
    pass

# Create your models here.

class Product(_a_(562376, _n_(562375, "models", lambda: models), "Model")):
    _l_(562379)

    ##contain all product information

    CONDITION_TYPE = _c_(562377, ("New" , "New"), "Used" , "Used")
    _l_(562378)

name = _c_(562382, _a_(562381, _n_(562380, "models", lambda: models), "CharField"), max_length=100)
_l_(562383)
description = _c_(562386, _a_(562385, _n_(562384, "models", lambda: models), "TextField"), max_length=500)
_l_(562387)
condition = _c_(562391, _a_(562389, _n_(562388, "models", lambda: models), "CharField"), max_length=100 , choices=_n_(562390, "CONDITION_TYPE", lambda: CONDITION_TYPE))
_l_(562392)
price = _c_(562395, _a_(562394, _n_(562393, "models", lambda: models), "DecimalField"), max_digits=10, decimal_places=5)
_l_(562396)
created = _c_(562399, _a_(562398, _n_(562397, "models", lambda: models), "DateTimeField"))
_l_(562400)