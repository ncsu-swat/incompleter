# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(607127)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(607129)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(607131)

except ImportError:
    pass
try:
    from django.conf.urls.static import static
    _l_(607133)

except ImportError:
    pass

urlpatterns = [
    _c_(607138, _n_(607134, "path", lambda: path), 'admin/', _a_(607137, _a_(607136, _n_(607135, "admin", lambda: admin), "site"), "urls")),
    _c_(607142, _n_(607139, "path", lambda: path), '', _c_(607141, _n_(607140, "include", lambda: include), 'chat.url'))
] + _c_(607148, _n_(607143, "static", lambda: static), _a_(607145, _n_(607144, "settings", lambda: settings), "STATIC_URL"), document_root=_a_(607147, _n_(607146, "settings", lambda: settings), "STATIC_ROOT"))
_l_(607149)