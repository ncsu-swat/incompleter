# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77687579/attributeerror-module-django-conf-global-settings-has-no-attribute-root-urlc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(548991)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(548993)

except ImportError:
    pass


urlpatterns = [
    _c_(548997, _n_(548994, "path", lambda: path), '', _c_(548996, _n_(548995, "include", lambda: include), 'App.api.urls')),
    _c_(549002, _n_(548998, "path", lambda: path), 'admin/', _a_(549001, _a_(549000, _n_(548999, "admin", lambda: admin), "site"), "urls")),
]
_l_(549003)