# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(668824)

except ImportError:
    pass
try:
    from django.db import models
    _l_(668826)

except ImportError:
    pass

class UserRegistrar(_a_(668828, _n_(668827, "forms", lambda: forms), "Form")):
    _l_(668843)

    first_name = _c_(668834, _a_(668830, _n_(668829, "forms", lambda: forms), "CharField"), required=True, widget=_c_(668833, _a_(668832, _n_(668831, "forms", lambda: forms), "TextInput"), attrs={'class': 'form-control'} ))
    _l_(668835)
    last_name = _c_(668841, _a_(668837, _n_(668836, "forms", lambda: forms), "CharField"), required=True, widget=_c_(668840, _a_(668839, _n_(668838, "forms", lambda: forms), "TextInput"), attrs={'class': 'form-control'}  ))
    _l_(668842)