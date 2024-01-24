# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(681774)

except ImportError:
    pass

class List(_a_(681776, _n_(681775, "models", lambda: models), "Model")):
    _l_(681778)

    pass
    _l_(681777)

class Item(_a_(681780, _n_(681779, "models", lambda: models), "Model")):
    _l_(681792)

    text = _c_(681783, _a_(681782, _n_(681781, "models", lambda: models), "TextField"), default='')
    _l_(681784)
    list = _c_(681790, _a_(681786, _n_(681785, "models", lambda: models), "ForeignKey"), _n_(681787, "List", lambda: List), default='', null=True, blank=True, on_delete = _a_(681789, _n_(681788, "models", lambda: models), "CASCADE"))
    _l_(681791)