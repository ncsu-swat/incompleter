# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, re_path
    _l_(443454)

except ImportError:
    pass
try:
    from .views import ThreadView, InboxView
    _l_(443456)

except ImportError:
    pass

app_name = 'qkchat'
_l_(443457)
urlpatterns = [
    _c_(443462, _n_(443458, "path", lambda: path), '', _c_(443461, _a_(443460, _n_(443459, "InboxView", lambda: InboxView), "as_view"))),
    _c_(443467, _n_(443463, "re_path", lambda: re_path), r'^(?P<username>[\w.@+-]+)/$', _c_(443466, _a_(443465, _n_(443464, "ThreadView", lambda: ThreadView), "as_view"))),
]
_l_(443468)