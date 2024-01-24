# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49550834/typeerror-at-admin-jobs-job-add-tuple-does-not-support-the-buffer-interface
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(471186)

except ImportError:
    pass
try:
    from .models import Job
    _l_(471188)

except ImportError:
    pass

_c_(471193, _a_(471191, _a_(471190, _n_(471189, "admin", lambda: admin), "site"), "register"), _n_(471192, "Job", lambda: Job))
_l_(471194)