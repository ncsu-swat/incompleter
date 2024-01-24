# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50672941/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf import settings
    _l_(528310)

except ImportError:
    pass
try:
    from django.db import models
    _l_(528312)

except ImportError:
    pass

# Create your models here.


class Tweet(_a_(528314, _n_(528313, "models", lambda: models), "Model")):
    _l_(528341)

    # user
    user = _c_(528321, _a_(528316, _n_(528315, "models", lambda: models), "ForeignKey"), _a_(528318, _n_(528317, "settings", lambda: settings), "AUTH_USER_MODEL"), on_delete=_a_(528320, _n_(528319, "models", lambda: models), "CASCADE"))
    _l_(528322)
    content = _c_(528325, _a_(528324, _n_(528323, "models", lambda: models), "CharField"), max_length=140)
    _l_(528326)
    updated = _c_(528329, _a_(528328, _n_(528327, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(528330)
    timestamp = _c_(528333, _a_(528332, _n_(528331, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(528334)

    def __str__(self):
        _l_(528340)

        aux = _c_(528338, _n_(528335, "str", lambda: str), _a_(528337, _n_(528336, "self", lambda: self), "content"))
        _l_(528339)
        return aux