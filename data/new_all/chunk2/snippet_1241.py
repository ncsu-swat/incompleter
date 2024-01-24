# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path,include
    _l_(454638)

except ImportError:
    pass
try:
    from rest_framework import routers
    _l_(454640)

except ImportError:
    pass
try:
    from .views import BookViewSet
    _l_(454642)

except ImportError:
    pass

router=_c_(454645, _a_(454644, _n_(454643, "routers", lambda: routers), "DefaultRouter"))
_l_(454646)
_c_(454650, _a_(454648, _n_(454647, "router", lambda: router), "register"), 'books',_n_(454649, "BookViewSet", lambda: BookViewSet))
_l_(454651)
urlpatterns=[
    _c_(454657, _n_(454652, "path", lambda: path), 'check',_c_(454656, _n_(454653, "include", lambda: include), _a_(454655, _n_(454654, "router", lambda: router), "urls"))),
]
_l_(454658)