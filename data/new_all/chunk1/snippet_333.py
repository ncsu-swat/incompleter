# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30401551/in-django-1-7-python3-using-floppyforms-1-3-keep-getting-error-typeerror-ob
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import floppyforms as forms
    _l_(410730)

except ImportError:
    pass
try:
    from crispy_forms.helper import FormHelper
    _l_(410732)

except ImportError:
    pass
try:
    from crispy_forms.layout import *
    _l_(410734)

except ImportError:
    pass
try:
    from crispy_forms.bootstrap import *
    _l_(410736)

except ImportError:
    pass

class MyCustomForm(_a_(410738, _n_(410737, "forms", lambda: forms), "ModelForm")):
    _l_(410759)

    user_name = _c_(410741, _a_(410740, _n_(410739, "forms", lambda: forms), "CharField"))
    _l_(410742)
    email = _c_(410745, _a_(410744, _n_(410743, "forms", lambda: forms), "CharField"))
    _l_(410746)
    phone = _c_(410749, _a_(410748, _n_(410747, "forms", lambda: forms), "CharField"))
    _l_(410750)
    first_name = _c_(410753, _a_(410752, _n_(410751, "forms", lambda: forms), "CharField"))
    _l_(410754)
    last_name = _c_(410757, _a_(410756, _n_(410755, "forms", lambda: forms), "CharField"))
    _l_(410758)

class Meta:
    _l_(410761)

    model = MyCustomModel
    _l_(410760)