# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59348642/django-registration-type-error-at-accounts-register-get-success-url-missing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from registration.backends.simple.views import RegistrationView
    _l_(667863)

except ImportError:
    pass


# my new reg view, subclassing RegistrationView from our plugin
class MyRegistrationView(_n_(667864, "RegistrationView", lambda: RegistrationView)):
    _l_(667867)

    def get_success_url(self, request, user):
        _l_(667866)

        aux = ('registration_create_word')
        _l_(667865)
        # the named URL that we want to redirect to after
        # successful registration
        return aux