# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49000930/django-attributeerror-tag-object-has-no-attribute-summary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Tag(_a_(670789, _n_(670788, "models", lambda: models), "Model")):
    _l_(670803)


    name = _c_(670791, _a_(670790, models, "CharField"), max_length=255)
    _l_(670792)
    description = _c_(670794, _a_(670793, models, "TextField"), null=True, blank=True)
    _l_(670795)
    created_at = _c_(670797, _a_(670796, models, "DateTimeField"), auto_now_add=True)
    _l_(670798)

    def __str__(self):
        _l_(670802)

        aux = _a_(670800, _n_(670799, "self", lambda: self), "name")
        _l_(670801)
        return aux