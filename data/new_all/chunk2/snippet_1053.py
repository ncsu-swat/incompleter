# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49003357/type-error-in-get-wsgi-application-in-django-2-x-with-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(457948)

except ImportError:
    pass
try:
    import sys
    _l_(457950)

except ImportError:
    pass

path = '/mypath'
_l_(457951)
if _n_(457952, "path", lambda: path) not in _a_(457954, _n_(457953, "sys", lambda: sys), "path"):
    _l_(457961)

    _c_(457959, _a_(457957, _a_(457956, _n_(457955, "sys", lambda: sys), "path"), "append"), _n_(457958, "path", lambda: path))
    _l_(457960)

_c_(457965, _a_(457964, _a_(457963, _n_(457962, "os", lambda: os), "environ"), "setdefault"), "DJANGO_SETTINGS_MODULE", "Myapplication.settings")
_l_(457966)
try:
    from django.core.wsgi import get_wsgi_application
    _l_(457968)

except ImportError:
    pass
application = _c_(457970, _n_(457969, "get_wsgi_application", lambda: get_wsgi_application))
_l_(457971)