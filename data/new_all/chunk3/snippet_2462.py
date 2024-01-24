# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77687579/attributeerror-module-django-conf-global-settings-has-no-attribute-root-urlc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(538175)

except ImportError:
    pass
try:
    from django.core.wsgi import get_wsgi_application
    _l_(538177)

except ImportError:
    pass


_c_(538181, _a_(538180, _a_(538179, _n_(538178, "os", lambda: os), "environ"), "setdefault"), 'DJANGO_SETTINGS_MODULE', 'mojspecjalista.settings')
_l_(538182)

application = _c_(538184, _n_(538183, "get_wsgi_application", lambda: get_wsgi_application))
_l_(538185)