# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url, include
    _l_(396588)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(396590)

except ImportError:
    pass
try:
    from rest_framework import routers
    _l_(396592)

except ImportError:
    pass
try:
    from developers import views
    _l_(396594)

except ImportError:
    pass

router = _c_(396597, _a_(396596, _n_(396595, "routers", lambda: routers), "DefaultRouter"))
_l_(396598)
_c_(396603, _a_(396600, _n_(396599, "router", lambda: router), "register"), r'developers', _a_(396602, _n_(396601, "views", lambda: views), "DevViewSet"))
_l_(396604)

urlpatterns = [
    _c_(396609, _n_(396605, "url", lambda: url), r'^admin', _a_(396608, _a_(396607, _n_(396606, "admin", lambda: admin), "site"), "urls")),
    _c_(396615, _n_(396610, "url", lambda: url), r'^api_demo', _c_(396614, _n_(396611, "include", lambda: include), _a_(396613, _n_(396612, "router", lambda: router), "urls"))),
]
_l_(396616)