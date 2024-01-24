# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(666854)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(666856)

except ImportError:
    pass
try:
    from django.db.models.signals import pre_save, post_save
    _l_(666858)

except ImportError:
    pass
try:
    from softforest.utils import unique_slug_generator
    _l_(666860)

except ImportError:
    pass

# Create your models here.

user = _a_(666862, _n_(666861, "settings", lambda: settings), "AUTH_USER_MODEL")
_l_(666863)


class Project(_a_(666865, _n_(666864, "models", lambda: models), "Model")):
    _l_(666912)

    user = _c_(666871, _a_(666867, _n_(666866, "models", lambda: models), "ForeignKey"), _n_(666868, "user", lambda: user), null=True, blank=True, on_delete=_a_(666870, _n_(666869, "models", lambda: models), "CASCADE"))
    _l_(666872)
    title = _c_(666875, _a_(666874, _n_(666873, "models", lambda: models), "CharField"), max_length=255)
    _l_(666876)
    slug = _c_(666879, _a_(666878, _n_(666877, "models", lambda: models), "SlugField"), blank=True, unique=True)
    _l_(666880)
    description = _c_(666883, _a_(666882, _n_(666881, "models", lambda: models), "TextField"))
    _l_(666884)
    price = _c_(666887, _a_(666886, _n_(666885, "models", lambda: models), "DecimalField"), default=0.00, max_digits=100, decimal_places=2)
    _l_(666888)
    ratings = _c_(666891, _a_(666890, _n_(666889, "models", lambda: models), "DecimalField"), default=0.0, max_digits=50, decimal_places=2, blank=True, null=True)
    _l_(666892)
    updated = _c_(666895, _a_(666894, _n_(666893, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(666896)
    timestamp = _c_(666899, _a_(666898, _n_(666897, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(666900)

    def __str__(self):
        _l_(666904)

        aux = _a_(666902, _n_(666901, "self", lambda: self), "title")
        _l_(666903)
        return aux

    @_n_(666905, "property", lambda: property)
    def modules(self):
        _l_(666911)

        aux = _c_(666909, _a_(666908, _a_(666907, _n_(666906, "self", lambda: self), "module_set"), "all"))
        _l_(666910)
        return aux


class Module(_a_(666914, _n_(666913, "models", lambda: models), "Model")):
    _l_(666930)

    project = _c_(666920, _a_(666916, _n_(666915, "models", lambda: models), "ForeignKey"), _n_(666917, "Project", lambda: Project), related_name='modules', on_delete=_a_(666919, _n_(666918, "models", lambda: models), "CASCADE"))
    _l_(666921)
    name = _c_(666924, _a_(666923, _n_(666922, "models", lambda: models), "CharField"), max_length=120)
    _l_(666925)

    def __str__(self):
        _l_(666929)

        aux = _a_(666927, _n_(666926, "self", lambda: self), "name")
        _l_(666928)
        return aux


class Technology(_a_(666932, _n_(666931, "models", lambda: models), "Model")):
    _l_(666948)

    project = _c_(666938, _a_(666934, _n_(666933, "models", lambda: models), "ForeignKey"), _n_(666935, "Project", lambda: Project), related_name='technologies', on_delete=_a_(666937, _n_(666936, "models", lambda: models), "CASCADE"))
    _l_(666939)
    name = _c_(666942, _a_(666941, _n_(666940, "models", lambda: models), "CharField"), max_length=120)
    _l_(666943)

    def __str__(self):
        _l_(666947)

        aux = _a_(666945, _n_(666944, "self", lambda: self), "name")
        _l_(666946)
        return aux


class Requirement(_a_(666950, _n_(666949, "models", lambda: models), "Model")):
    _l_(666966)

    project = _c_(666956, _a_(666952, _n_(666951, "models", lambda: models), "ForeignKey"), _n_(666953, "Project", lambda: Project), related_name='requirements', on_delete=_a_(666955, _n_(666954, "models", lambda: models), "CASCADE"))
    _l_(666957)
    name = _c_(666960, _a_(666959, _n_(666958, "models", lambda: models), "CharField"), max_length=120)
    _l_(666961)

    def __str__(self):
        _l_(666965)

        aux = _a_(666963, _n_(666962, "self", lambda: self), "name")
        _l_(666964)
        return aux


def project_pre_receiver(sender, instance, *args, **kwargs):
    _l_(666975)

    if not _a_(666968, _n_(666967, "instance", lambda: instance), "slug"):
        _l_(666974)

        _n_(666969, "instance", lambda: instance).slug = _c_(666972, _n_(666970, "unique_slug_generator", lambda: unique_slug_generator), _n_(666971, "instance", lambda: instance))
        _l_(666973)


_c_(666980, _a_(666977, _n_(666976, "pre_save", lambda: pre_save), "connect"), _n_(666978, "project_pre_receiver", lambda: project_pre_receiver), sender=_n_(666979, "Project", lambda: Project))
_l_(666981)