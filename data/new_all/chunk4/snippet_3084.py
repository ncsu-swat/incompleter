# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47953230/django-queryset-count-method-raise-typeerror-unorderable-types-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(621401)

except ImportError:
    pass

class Device(_a_(621403, _n_(621402, "models", lambda: models), "Model")):
    _l_(621410)

    deviceClass     = _c_(621406, _a_(621405, _n_(621404, "models", lambda: models), "CharField"), max_length=10)
    _l_(621407)

    class Meta:
        _l_(621409)

        db_table = 'TST_G2S_DEVICE'
        _l_(621408)