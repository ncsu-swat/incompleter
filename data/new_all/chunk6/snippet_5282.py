# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73725398/i-am-getting-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(358130)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(358132)

except ImportError:
    pass

urlpatterns = [
    _c_(358136, _n_(358133, "path", lambda: path), '', _c_(358135, _n_(358134, "include", lambda: include), 'webarticles.urls')),
]
_l_(358137)