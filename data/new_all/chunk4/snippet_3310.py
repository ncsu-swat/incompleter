# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75885496/nameerror-in-django-model-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(616782)

except ImportError:
    pass

# Create your models here.
class Airport(_a_(616784, _n_(616783, "models", lambda: models), "Model")):
    _l_(616799)

    code = _c_(616787, _a_(616786, _n_(616785, "models", lambda: models), "CharField"), max_length=3)
    _l_(616788)
    city = _c_(616791, _a_(616790, _n_(616789, "models", lambda: models), "CharField"), max_length=64)
    _l_(616792)

    def __str__(self):
        _l_(616798)

        aux = f"{_a_(616794, _n_(616793, 'self', lambda: self), 'city')} ({_a_(616796, _n_(616795, 'self', lambda: self), 'code')})"
        _l_(616797)
        return aux

class Flight(_a_(616801, _n_(616800, "models", lambda: models), "Model")):
    _l_(616828)

    origin = _c_(616807, _a_(616803, _n_(616802, "models", lambda: models), "ForeignKey"), _n_(616804, "Airport", lambda: Airport), on_delete =_a_(616806, _n_(616805, "models", lambda: models), "CASCADE"), related_name="departures")
    _l_(616808)
    destination = _c_(616814, _a_(616810, _n_(616809, "models", lambda: models), "ForeignKey"), _n_(616811, "Airport", lambda: Airport), on_delete=_a_(616813, _n_(616812, "models", lambda: models), "CASCADE"), related_name="arrivals")
    _l_(616815)
    duration = _c_(616818, _a_(616817, _n_(616816, "models", lambda: models), "IntegerField"))
    _l_(616819)

    def __str__(self):
        _l_(616827)

        aux = f"{_a_(616821, _n_(616820, 'self', lambda: self), 'id')}: {_a_(616823, _n_(616822, 'self', lambda: self), 'origin')} to {_a_(616825, _n_(616824, 'self', lambda: self), 'destination')}"
        _l_(616826)
        return aux