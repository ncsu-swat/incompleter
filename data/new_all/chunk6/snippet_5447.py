# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import include, url
    _l_(334958)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(334960)

except ImportError:
    pass

urlpatterns = [
    _c_(334965, _n_(334961, "url", lambda: url), r'^admin/', _a_(334964, _a_(334963, _n_(334962, "admin", lambda: admin), "site"), "urls")),
    _c_(334971, _n_(334966, "url", lambda: url), r'^logs/', _c_(334970, _n_(334967, "include", lambda: include), _a_(334969, _n_(334968, "logs", lambda: logs), "urls"))),
]
_l_(334972)