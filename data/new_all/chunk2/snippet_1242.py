# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(438202)

except ImportError:
    pass
try:
    from django.urls import path,include
    _l_(438204)

except ImportError:
    pass
try:
    from rest_framework.authtoken.views import obtain_auth_token
    _l_(438206)

except ImportError:
    pass

urlpatterns = [
    _c_(438211, _n_(438207, "path", lambda: path), 'admin/', _a_(438210, _a_(438209, _n_(438208, "admin", lambda: admin), "site"), "urls")),
    _c_(438215, _n_(438212, "path", lambda: path), 'ap1/',_c_(438214, _n_(438213, "include", lambda: include), 'ap1.urls')),
    _c_(438218, _n_(438216, "path", lambda: path), 'auth/',_n_(438217, "obtain_auth_token", lambda: obtain_auth_token)),
]
_l_(438219)