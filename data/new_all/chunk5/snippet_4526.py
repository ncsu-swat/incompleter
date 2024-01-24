# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(676330)

except ImportError:
    pass
try:
    from django.db import models
    _l_(676332)

except ImportError:
    pass

class UserRegistrar(_a_(676334, _n_(676333, "forms", lambda: forms), "Form")):
    _l_(676349)

    first_name = _c_(676340, _a_(676336, _n_(676335, "forms", lambda: forms), "CharField"), required=True, widget=_c_(676339, _a_(676338, _n_(676337, "forms", lambda: forms), "TextInput"), attrs={'class': 'form-control'} ))
    _l_(676341)
    last_name = _c_(676347, _a_(676343, _n_(676342, "forms", lambda: forms), "CharField"), required=True, widget=_c_(676346, _a_(676345, _n_(676344, "forms", lambda: forms), "TextInput"), attrs={'class': 'form-control'}  ))
    _l_(676348)