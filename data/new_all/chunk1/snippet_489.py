# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51466319/django2-attributeerror-in-urls-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(382386)

except ImportError:
    pass
try:
    from django.urls import path
    _l_(382388)

except ImportError:
    pass
try:
    from django.conf.urls import url
    _l_(382390)

except ImportError:
    pass
try:
    from core import views as coreviews
    _l_(382392)

except ImportError:
    pass

urlpatterns = ['',
    _c_(382396, _n_(382393, "url", lambda: url), r'^$', _a_(382395, _n_(382394, "coreviews", lambda: coreviews), "home")), 
    _c_(382401, _n_(382397, "path", lambda: path), 'admin/', _a_(382400, _a_(382399, _n_(382398, "admin", lambda: admin), "site"), "urls"))
]
_l_(382402)