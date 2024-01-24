# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(460533)

except ImportError:
    pass

class ComposeForm(_a_(460535, _n_(460534, "forms", lambda: forms), "Form")):
    _l_(460543)

    message = _c_(460541, _a_(460537, _n_(460536, "forms", lambda: forms), "CharField"), widget=_c_(460540, _a_(460539, _n_(460538, "forms", lambda: forms), "TextInput"), attrs={"class": "form-control",
                }
            )
        )
    _l_(460542)