# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(685959)

except ImportError:
    pass

class List(_a_(685961, _n_(685960, "models", lambda: models), "Model")):
    _l_(685963)

    pass
    _l_(685962)

class Item(_a_(685965, _n_(685964, "models", lambda: models), "Model")):
    _l_(685977)

    text = _c_(685968, _a_(685967, _n_(685966, "models", lambda: models), "TextField"), default='')
    _l_(685969)
    list = _c_(685975, _a_(685971, _n_(685970, "models", lambda: models), "ForeignKey"), _n_(685972, "List", lambda: List), default='', null=True, blank=True, on_delete = _a_(685974, _n_(685973, "models", lambda: models), "CASCADE"))
    _l_(685976)