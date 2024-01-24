# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(636200)

except ImportError:
    pass
try:
    from . import views
    _l_(636202)

except ImportError:
    pass

urlpatterns = [
    _c_(636206, _n_(636203, "url", lambda: url), r'^$/', _a_(636205, _n_(636204, "views", lambda: views), "index"), name='index'),
]
_l_(636207)