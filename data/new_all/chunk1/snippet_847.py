# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63101250/i-am-getting-an-attribute-error-while-trying-to-build-a-user-registration-form-u
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django import forms
    _l_(396837)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(396839)

except ImportError:
    pass
try:
    from basic_app.models import UserProfileInfo
    _l_(396841)

except ImportError:
    pass

class UserForm(_a_(396843, _n_(396842, "forms", lambda: forms), "ModelForm")):
    _l_(396855)

    password = _c_(396849, _a_(396845, _n_(396844, "forms", lambda: forms), "CharField"), widget=_c_(396848, _a_(396847, _n_(396846, "forms", lambda: forms), "PasswordInput")))
    _l_(396850)

    class Meta():
        _l_(396854)

        model = _n_(396851, "User", lambda: User)
        _l_(396852)
        fields = ('username', 'email', 'password')
        _l_(396853)

class UserProfileInfoForm(_a_(396857, _n_(396856, "forms", lambda: forms), "ModelForm")):
    _l_(396862)

    class Meta():
        _l_(396861)

        model = _n_(396858, "UserProfileInfo", lambda: UserProfileInfo)
        _l_(396859)
        fields = ('portfolio_site', 'profile_pic')
        _l_(396860)