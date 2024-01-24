# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50054662/django-admin-site-register-throws-typeerror-for-models-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(390880)

except ImportError:
    pass
try:
    import inspect
    _l_(390882)

except ImportError:
    pass
try:
    from . import models
    _l_(390884)

except ImportError:
    pass

for name, obj in _c_(390888, _a_(390886, _n_(390885, "inspect", lambda: inspect), "getmembers"), _n_(390887, "models", lambda: models)):
    _l_(390900)

    if _c_(390892, _a_(390890, _n_(390889, "inspect", lambda: inspect), "isclass"), _n_(390891, "obj", lambda: obj)):
        _l_(390899)

        _c_(390897, _a_(390895, _a_(390894, _n_(390893, "admin", lambda: admin), "site"), "register"), _n_(390896, "obj", lambda: obj))
        _l_(390898)