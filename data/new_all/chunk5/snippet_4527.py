# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(661095)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(661097)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(661099)

except ImportError:
    pass


class post(_a_(661101, _n_(661100, "models", lambda: models), "Model")):
    _l_(661133)

    title = _c_(661104, _a_(661103, _n_(661102, "models", lambda: models), "CharField"), max_length=10)
    _l_(661105)
    content = _c_(661108, _a_(661107, _n_(661106, "models", lambda: models), "TextField"), max_length=30)
    _l_(661109)
    post_date = _c_(661114, _a_(661111, _n_(661110, "models", lambda: models), "DateTimeField"), default=_a_(661113, _n_(661112, "timezone", lambda: timezone), "now"))
    _l_(661115)
    post_update = _c_(661118, _a_(661117, _n_(661116, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(661119)
    author = _c_(661125, _a_(661121, _n_(661120, "models", lambda: models), "ForeignKey"), _n_(661122, "User", lambda: User), on_delete=_a_(661124, _n_(661123, "models", lambda: models), "CASCADE"))
    _l_(661126)

    def __str__(self):
        _l_(661130)

        aux = _a_(661128, _n_(661127, "self", lambda: self), "title")
        _l_(661129)
        return aux

    class Meta:
        _l_(661132)

        ordering = ('-post_date', )
        _l_(661131)


class Lost(_a_(661135, _n_(661134, "models", lambda: models), "Model")):
    _l_(661167)

    title = _c_(661138, _a_(661137, _n_(661136, "models", lambda: models), "CharField"), max_length=100)
    _l_(661139)
    content = _c_(661142, _a_(661141, _n_(661140, "models", lambda: models), "TextField"), max_length=300)
    _l_(661143)
    post_date = _c_(661148, _a_(661145, _n_(661144, "models", lambda: models), "DateTimeField"), default=_a_(661147, _n_(661146, "timezone", lambda: timezone), "now"))
    _l_(661149)
    post_update = _c_(661152, _a_(661151, _n_(661150, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(661153)
    author = _c_(661159, _a_(661155, _n_(661154, "models", lambda: models), "ForeignKey"), _n_(661156, "User", lambda: User), on_delete=_a_(661158, _n_(661157, "models", lambda: models), "CASCADE"))
    _l_(661160)

    def __str__(self):
        _l_(661164)

        aux = _a_(661162, _n_(661161, "self", lambda: self), "title")
        _l_(661163)
        return aux

    class Meta:
        _l_(661166)

        ordering = ('-post_date', )    
        _l_(661165)    


class Student(_a_(661169, _n_(661168, "models", lambda: models), "Model")):
    _l_(661190)

    first_name=_c_(661172, _a_(661171, _n_(661170, "models", lambda: models), "CharField"), max_length=15)
    _l_(661173)
    last_name=_c_(661176, _a_(661175, _n_(661174, "models", lambda: models), "CharField"), max_length=15)
    _l_(661177)
    age=_c_(661180, _a_(661179, _n_(661178, "models", lambda: models), "IntegerField"), default=15)
    _l_(661181)
    date_birth=_c_(661184, _a_(661183, _n_(661182, "models", lambda: models), "DateTimeField"))
    _l_(661185)
    def __str__(self):
        _l_(661189)

        aux = _a_(661187, _n_(661186, "self", lambda: self), "first_name")
        _l_(661188)
        return aux