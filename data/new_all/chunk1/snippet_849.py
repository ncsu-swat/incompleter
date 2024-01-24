# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63101250/i-am-getting-an-attribute-error-while-trying-to-build-a-user-registration-form-u
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(412942)

except ImportError:
    pass
try:
    from basic_app.forms import UserForm, UserProfileInfoForm
    _l_(412944)

except ImportError:
    pass
try:
    from . import forms
    _l_(412946)

except ImportError:
    pass
# Create your views here.
def index(request):
    _l_(412951)

    aux = _c_(412949, _n_(412947, "render", lambda: render), _n_(412948, "request", lambda: request), 'basic_app/index.html')
    _l_(412950)
    return aux

def reqister(request):
    _l_(413026)

    registered = False
    _l_(412952)

    if _a_(412954, _n_(412953, "request", lambda: request), "method") == "POST":
        _l_(413018)

        user_form = _c_(412958, _n_(412955, "UserForm", lambda: UserForm), data=_a_(412957, _n_(412956, "request", lambda: request), "POST"))
        _l_(412959)
        profile_form = _c_(412963, _n_(412960, "UserProfileInfoForm", lambda: UserProfileInfoForm), data=_a_(412962, _n_(412961, "request", lambda: request), "POST"))
        _l_(412964)

        if _c_(412967, _a_(412966, _n_(412965, "user_form", lambda: user_form), "is_valid")) and _c_(412970, _a_(412969, _n_(412968, "profile_form", lambda: profile_form), "is_valid")):
            _l_(413011)

            user = _c_(412973, _a_(412972, _n_(412971, "user_form", lambda: user_form), "save"))
            _l_(412974)
            _c_(412979, _a_(412976, _n_(412975, "user", lambda: user), "set_password"), _a_(412978, _n_(412977, "user", lambda: user), "password")) #this one
            _l_(412980) #this one
            _c_(412983, _a_(412982, _n_(412981, "user", lambda: user), "save"))
            _l_(412984)

            profile = _c_(412987, _a_(412986, _n_(412985, "profile_form", lambda: profile_form), "save"), commit=False)
            _l_(412988)
            _n_(412989, "profile", lambda: profile).user = _n_(412990, "user", lambda: user)
            _l_(412991)

            if 'profile_pic' in _a_(412993, _n_(412992, "request", lambda: request), "FILES"):
                _l_(412998)

                _n_(412994, "profile", lambda: profile).profile_pic = _a_(412996, _n_(412995, "request", lambda: request), "FILES")['profile_pic']
                _l_(412997)

            _c_(413001, _a_(413000, _n_(412999, "profile", lambda: profile), "save"))
            _l_(413002)

            registered = True
            _l_(413003)

        else:
            _c_(413009, _n_(413004, "print", lambda: print), _a_(413006, _n_(413005, "user_form", lambda: user_form), "errors"), _a_(413008, _n_(413007, "profile_form", lambda: profile_form), "errors"))
            _l_(413010)

    else:
        user_form = _c_(413013, _n_(413012, "UserForm", lambda: UserForm))
        _l_(413014)
        profile_form = _c_(413016, _n_(413015, "UserProfileInfoForm", lambda: UserProfileInfoForm))
        _l_(413017)
    aux = _c_(413024, _n_(413019, "render", lambda: render), _n_(413020, "request", lambda: request), 'basic_app/registration.html',
                            {'user_form':_n_(413021, "user_form", lambda: user_form),
                            'profile_form': _n_(413022, "profile_form", lambda: profile_form),
                            'registered': _n_(413023, "registered", lambda: registered)})
    _l_(413025)

    return aux