# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59889563/typeerror-init-got-an-unexpected-keyword-argument-attrs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.forms import UserCreationForm
    _l_(546934)

except ImportError:
    pass
try:
    from django.forms import ModelForm
    _l_(546936)

except ImportError:
    pass
try:
    from django import forms
    _l_(546938)

except ImportError:
    pass
try:
    from . models import Profile
    _l_(546940)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(546942)

except ImportError:
    pass

ACCOUNT_TYPE = [
    ('SPO', 'SPO'),
    ('Call Agent', 'Call Agent'),
    ('Accountant', 'Accountant'),
]
_l_(546943)

class CreateUserForm(_n_(546944, "UserCreationForm", lambda: UserCreationForm)):
    _l_(546965)

    name            = _c_(546947, _a_(546946, _n_(546945, "forms", lambda: forms), "CharField"), max_length=255, required=False)
    _l_(546948)
    account_type    = _c_(546952, _a_(546950, _n_(546949, "forms", lambda: forms), "ChoiceField"), choices = _n_(546951, "ACCOUNT_TYPE", lambda: ACCOUNT_TYPE))
    _l_(546953)

    
    class Meta:
        _l_(546964)

        model = _n_(546954, "User", lambda: User)
        _l_(546955)
        fields = ['username', 'email', 'password1', 'password2']
        _l_(546956)

        widgets = {
            'name': _c_(546959, _a_(546958, _n_(546957, "forms", lambda: forms), "CharField"), attrs={'class': 'form-control','required':'required'}),
            'account_type': _c_(546962, _a_(546961, _n_(546960, "forms", lambda: forms), "ChoiceField"), attrs={'class': 'form-control','required':'required'})
        }
        _l_(546963)