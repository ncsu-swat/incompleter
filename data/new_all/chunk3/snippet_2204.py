# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(578998)

except ImportError:
    pass
try:
    from django.urls import path , include
    _l_(579000)

except ImportError:
    pass

urlpatterns = [
    _c_(579004, _n_(579001, "path", lambda: path), '', _c_(579003, _n_(579002, "include", lambda: include), 'calc.urls')),
    _c_(579009, _n_(579005, "path", lambda: path), 'admin/', _a_(579008, _a_(579007, _n_(579006, "admin", lambda: admin), "site"), "urls")),
]
_l_(579010)