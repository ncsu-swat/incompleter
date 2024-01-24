# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(663860)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(663862)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(663864)

except ImportError:
    pass


class post(_a_(663866, _n_(663865, "models", lambda: models), "Model")):
    _l_(663898)

    title = _c_(663869, _a_(663868, _n_(663867, "models", lambda: models), "CharField"), max_length=10)
    _l_(663870)
    content = _c_(663873, _a_(663872, _n_(663871, "models", lambda: models), "TextField"), max_length=30)
    _l_(663874)
    post_date = _c_(663879, _a_(663876, _n_(663875, "models", lambda: models), "DateTimeField"), default=_a_(663878, _n_(663877, "timezone", lambda: timezone), "now"))
    _l_(663880)
    post_update = _c_(663883, _a_(663882, _n_(663881, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(663884)
    author = _c_(663890, _a_(663886, _n_(663885, "models", lambda: models), "ForeignKey"), _n_(663887, "User", lambda: User), on_delete=_a_(663889, _n_(663888, "models", lambda: models), "CASCADE"))
    _l_(663891)

    def __str__(self):
        _l_(663895)

        aux = _a_(663893, _n_(663892, "self", lambda: self), "title")
        _l_(663894)
        return aux

    class Meta:
        _l_(663897)

        ordering = ('-post_date', )
        _l_(663896)


class Lost(_a_(663900, _n_(663899, "models", lambda: models), "Model")):
    _l_(663932)

    title = _c_(663903, _a_(663902, _n_(663901, "models", lambda: models), "CharField"), max_length=100)
    _l_(663904)
    content = _c_(663907, _a_(663906, _n_(663905, "models", lambda: models), "TextField"), max_length=300)
    _l_(663908)
    post_date = _c_(663913, _a_(663910, _n_(663909, "models", lambda: models), "DateTimeField"), default=_a_(663912, _n_(663911, "timezone", lambda: timezone), "now"))
    _l_(663914)
    post_update = _c_(663917, _a_(663916, _n_(663915, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(663918)
    author = _c_(663924, _a_(663920, _n_(663919, "models", lambda: models), "ForeignKey"), _n_(663921, "User", lambda: User), on_delete=_a_(663923, _n_(663922, "models", lambda: models), "CASCADE"))
    _l_(663925)

    def __str__(self):
        _l_(663929)

        aux = _a_(663927, _n_(663926, "self", lambda: self), "title")
        _l_(663928)
        return aux

    class Meta:
        _l_(663931)

        ordering = ('-post_date', )    
        _l_(663930)    


class Student(_a_(663934, _n_(663933, "models", lambda: models), "Model")):
    _l_(663955)

    first_name=_c_(663937, _a_(663936, _n_(663935, "models", lambda: models), "CharField"), max_length=15)
    _l_(663938)
    last_name=_c_(663941, _a_(663940, _n_(663939, "models", lambda: models), "CharField"), max_length=15)
    _l_(663942)
    age=_c_(663945, _a_(663944, _n_(663943, "models", lambda: models), "IntegerField"), default=15)
    _l_(663946)
    date_birth=_c_(663949, _a_(663948, _n_(663947, "models", lambda: models), "DateTimeField"))
    _l_(663950)
    def __str__(self):
        _l_(663954)

        aux = _a_(663952, _n_(663951, "self", lambda: self), "first_name")
        _l_(663953)
        return aux