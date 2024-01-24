# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67081201/django-throws-attributeerror-str-object-has-no-attribute-meta-when-i-regis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(578142)

except ImportError:
    pass
try:
    from .models import *
    _l_(578144)

except ImportError:
    pass

_c_(578148, _a_(578147, _a_(578146, _n_(578145, "admin", lambda: admin), "site"), "register"), 'Post')
_l_(578149)