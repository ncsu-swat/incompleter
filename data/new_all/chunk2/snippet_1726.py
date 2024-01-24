# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(467329)

except ImportError:
    pass
try:
    from django.urls import path,include
    _l_(467331)

except ImportError:
    pass
try:
    from django.conf.urls import url
    _l_(467333)

except ImportError:
    pass
_c_(467336, _a_(467335, _n_(467334, "admin", lambda: admin), "autodiscover"))
_l_(467337)

urlpatterns = ['',
    _c_(467342, _n_(467338, "path", lambda: path), 'admin/', _a_(467341, _a_(467340, _n_(467339, "admin", lambda: admin), "site"), "urls")),
    _c_(467346, _n_(467343, "url", lambda: url), 'myapp/', _c_(467345, _n_(467344, "include", lambda: include), 'myapp.url'))
]
_l_(467347)