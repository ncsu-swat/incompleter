# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import include, url
    _l_(339662)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(339664)

except ImportError:
    pass

urlpatterns = [
    _c_(339669, _n_(339665, "url", lambda: url), r'^admin/', _a_(339668, _a_(339667, _n_(339666, "admin", lambda: admin), "site"), "urls")),
    _c_(339675, _n_(339670, "url", lambda: url), r'^logs/', _c_(339674, _n_(339671, "include", lambda: include), _a_(339673, _n_(339672, "logs", lambda: logs), "urls"))),
]
_l_(339676)