# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51768654/django-typeerror-at-account-register-tuple-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class RegisterView(_n_(697303, "CreateView", lambda: CreateView)):
    _l_(697377)

    model = User, UserProfile
    _l_(697304)
    form_class = RegistrationForm, UserProfileForm
    _l_(697305)

    def post(self, request, *args, **kwargs):
        _l_(697376)

        user_form = _c_(697309, _n_(697306, "RegistrationForm", lambda: RegistrationForm), data=_a_(697308, _n_(697307, "request", lambda: request), "POST"))
        _l_(697310)
        profile_form = _c_(697314, _n_(697311, "UserProfileForm", lambda: UserProfileForm), data=_a_(697313, _n_(697312, "request", lambda: request), "POST"))
        _l_(697315)
        if _c_(697318, _a_(697317, _n_(697316, "user_form", lambda: user_form), "is_valid")) and _c_(697321, _a_(697320, _n_(697319, "profile_form", lambda: profile_form), "is_valid")):
            _l_(697368)

            user = _c_(697324, _a_(697323, _n_(697322, "user_form", lambda: user_form), "save"))
            _l_(697325)
            _c_(697330, _a_(697327, _n_(697326, "user", lambda: user), "set_password"), _a_(697329, _n_(697328, "user", lambda: user), "password"))
            _l_(697331)
            _c_(697334, _a_(697333, _n_(697332, "user", lambda: user), "save"))
            _l_(697335)
            profile = _c_(697338, _a_(697337, _n_(697336, "profile_form", lambda: profile_form), "save"), commit=False)
            _l_(697339)
            _n_(697340, "profile", lambda: profile).user = _n_(697341, "user", lambda: user)
            _l_(697342)
            if 'profile_photo' in _a_(697344, _n_(697343, "request", lambda: request), "FILES"):
                _l_(697361)

                _n_(697345, "profile", lambda: profile).profile_photo = _a_(697347, _n_(697346, "request", lambda: request), "FILES")['profile_photo']
                _l_(697348)
                _c_(697351, _a_(697350, _n_(697349, "profile", lambda: profile), "save"))
                _l_(697352)
                registered = True
                _l_(697353)
            else:
                _c_(697359, _n_(697354, "print", lambda: print), _a_(697356, _n_(697355, "user_form", lambda: user_form), "errors"), _a_(697358, _n_(697357, "profile_form", lambda: profile_form), "errors"))
                _l_(697360)
        else:
            user_form = _c_(697363, _n_(697362, "RegistrationForm", lambda: RegistrationForm))
            _l_(697364)
            profile_form = _c_(697366, _n_(697365, "UserProfileForm", lambda: UserProfileForm))
            _l_(697367)
        aux = _c_(697374, _n_(697369, "render", lambda: render), _n_(697370, "request", lambda: request), 'accounts/registration.html',
                      {'user_form': _n_(697371, "user_form", lambda: user_form), 'profile_form': _n_(697372, "profile_form", lambda: profile_form), 
        'registered': _n_(697373, "registered", lambda: registered)})
        _l_(697375)

        return aux