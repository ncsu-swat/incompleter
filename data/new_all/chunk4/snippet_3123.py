# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
from __future__ import unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(622837)
try:
    from django.contrib.auth.models import Permission, User
    _l_(622839)

except ImportError:
    pass
try:
    from django.db import models
    _l_(622841)

except ImportError:
    pass


# Create your models here.
class profile(_a_(622843, _n_(622842, "models", lambda: models), "Model")):
    _l_(622856)

    name = _c_(622846, _a_(622845, _n_(622844, "models", lambda: models), "CharField"), max_length=120)
    _l_(622847)
    description = _c_(622850, _a_(622849, _n_(622848, "models", lambda: models), "TextField"), default='description default text')
    _l_(622851)

    def __unicode__(self):
        _l_(622855)

        aux = _a_(622853, _n_(622852, "self", lambda: self), "name")
        _l_(622854)
        return aux


class Album(_a_(622858, _n_(622857, "models", lambda: models), "Model")):
    _l_(622876)

    user = _c_(622862, _a_(622860, _n_(622859, "models", lambda: models), "ForeignKey"), _n_(622861, "User", lambda: User), default=1)
    _l_(622863)
    image = _c_(622866, _a_(622865, _n_(622864, "models", lambda: models), "FileField"))
    _l_(622867)
    follow = _c_(622870, _a_(622869, _n_(622868, "models", lambda: models), "ManyToManyField"), 'self', blank=True)
    _l_(622871)

    def __unicode__(self):
        _l_(622875)

        aux = _a_(622873, _n_(622872, "self", lambda: self), "user")
        _l_(622874)
        return aux