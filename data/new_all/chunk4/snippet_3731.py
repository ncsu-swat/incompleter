# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import include, url
    _l_(596591)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(596593)

except ImportError:
    pass

urlpatterns = [
    _c_(596598, _n_(596594, "url", lambda: url), r'^admin/', _a_(596597, _a_(596596, _n_(596595, "admin", lambda: admin), "site"), "urls")),
    _c_(596604, _n_(596599, "url", lambda: url), r'^logs/', _c_(596603, _n_(596600, "include", lambda: include), _a_(596602, _n_(596601, "logs", lambda: logs), "urls"))),
]
_l_(596605)