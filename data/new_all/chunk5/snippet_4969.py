# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36021291/django-python3-attributeerror-module-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(655930)

except ImportError:
    pass

class EmailForm(_a_(655932, _n_(655931, "forms", lambda: forms), "Form")):
    _l_(655937)

    email = _c_(655935, _a_(655934, _n_(655933, "forms", lambda: forms), "TextInput"))
    _l_(655936)