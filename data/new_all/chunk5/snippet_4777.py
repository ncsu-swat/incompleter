# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(693792)

except ImportError:
    pass
try:
    from datetime import*
    _l_(693794)

except ImportError:
    pass
try:
    import time
    _l_(693796)

except ImportError:
    pass
try:
    from django.utils.timesince import timesince
    _l_(693798)

except ImportError:
    pass
try:
    from django.urls import*
    _l_(693800)

except ImportError:
    pass

class Task(_a_(693802, _n_(693801, "models", lambda: models), "Model")):
    _l_(693821)

    task_title = _c_(693805, _a_(693804, _n_(693803, "models", lambda: models), "CharField"), max_length=50)
    _l_(693806)
    complete = _c_(693809, _a_(693808, _n_(693807, "models", lambda: models), "BooleanField"), default=False)
    _l_(693810)

    def get_absolute_url(self):
        _l_(693816)

        aux = _c_(693814, _n_(693811, "reverse", lambda: reverse), 'todo:detail', kwargs={'pk':_a_(693813, _n_(693812, "self", lambda: self), "pk")})
        _l_(693815)
        return aux

    def __str__(self):
        _l_(693820)

        aux = _a_(693818, _n_(693817, "self", lambda: self), "task_title")
        _l_(693819)
        return aux