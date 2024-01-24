# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(414521)

except ImportError:
    pass
try:
    from django.core.wsgi import get_wsgi_application
    _l_(414523)

except ImportError:
    pass

_c_(414527, _a_(414526, _a_(414525, _n_(414524, "os", lambda: os), "environ"), "setdefault"), "DJANGO_SETTINGS_MODULE", "StackOverflow.settings")
_l_(414528)

application = _c_(414530, _n_(414529, "get_wsgi_application", lambda: get_wsgi_application))
_l_(414531)