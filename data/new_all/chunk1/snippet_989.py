# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth import get_user_model
    _l_(380093)

except ImportError:
    pass
try:
    from django.contrib.auth.forms import UserCreationForm
    _l_(380095)

except ImportError:
    pass

class userCreateForm(_n_(380096, "UserCreationForm", lambda: UserCreationForm)):
    _l_(380115)


    class Meta:
        _l_(380101)

        fields = ('username', 'email', 'password1', 'password2')
        _l_(380097)
        model = _c_(380099, _n_(380098, "get_user_model", lambda: get_user_model))
        _l_(380100)

    def __init__(self,*args,**kwargs):
        _l_(380114)

        _c_(380106, _a_(380103, _n_(380102, "super", lambda: super)(), "__init__"), *_n_(380104, "args", lambda: args),**_n_(380105, "kwargs", lambda: kwargs))
        _l_(380107)
        _a_(380109, _n_(380108, "self", lambda: self), "fields")['username'].label = 'Username'
        _l_(380110)
        _a_(380112, _n_(380111, "self", lambda: self), "fields")['email'].label = 'E-mail Address'
        _l_(380113)