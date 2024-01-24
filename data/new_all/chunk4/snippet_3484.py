# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(594914)

except ImportError:
    pass
try:
    import uuid
    _l_(594916)

except ImportError:
    pass

class Project(_a_(594918, _n_(594917, "models", lambda: models), "Model")):
    _l_(594961)

    title = _c_(594921, _a_(594920, _n_(594919, "models", lambda: models), "CharField"), max_length=200)
    _l_(594922)
    description = _c_(594925, _a_(594924, _n_(594923, "models", lambda: models), "TextField"), null=True, blank=True)
    _l_(594926)
    demo_link = _c_(594929, _a_(594928, _n_(594927, "models", lambda: models), "CharField"), null=True, blank=True, max_length=2000)
    _l_(594930)
    source_link = _c_(594933, _a_(594932, _n_(594931, "models", lambda: models), "CharField"), null=True, blank=True, max_length=2000)
    _l_(594934)
    created = _c_(594937, _a_(594936, _n_(594935, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(594938)
    id = _c_(594943, _a_(594940, _n_(594939, "models", lambda: models), "UUIDField"), default=_a_(594942, _n_(594941, "uuid", lambda: uuid), "uuid4"), unique=True, primary_key=True, editable=False)
    _l_(594944)
    tag = _c_(594947, _a_(594946, _n_(594945, "models", lambda: models), "ManyToManyField"), 'Tag', blank=True)
    _l_(594948)
    total_vote = _c_(594951, _a_(594950, _n_(594949, "models", lambda: models), "IntegerField"), default=0, null=True, blank=True)
    _l_(594952)
    vote_ratio = _c_(594955, _a_(594954, _n_(594953, "models", lambda: models), "IntegerField"), default=0, null=True, blank=True)
    _l_(594956)

    def __str__(self):
        _l_(594960)

        aux = _a_(594958, _n_(594957, "self", lambda: self), "title")
        _l_(594959)
        return aux


class Review(_a_(594963, _n_(594962, "models", lambda: models), "Model")):
    _l_(594994)

    VOTE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    _l_(594964)
    project = _c_(594970, _a_(594966, _n_(594965, "models", lambda: models), "ForeignKey"), _n_(594967, "Project", lambda: Project), on_delete=_a_(594969, _n_(594968, "models", lambda: models), "CASCADE"))
    _l_(594971)
    body = _c_(594974, _a_(594973, _n_(594972, "models", lambda: models), "TextField"), null=True, blank=True)
    _l_(594975)
    value = _c_(594978, _a_(594977, _n_(594976, "models", lambda: models), "CharField"), max_length=200, choices=VOTE)
    _l_(594979)
    created = _c_(594982, _a_(594981, _n_(594980, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(594983)
    id = _c_(594988, _a_(594985, _n_(594984, "models", lambda: models), "UUIDField"), default=_a_(594987, _n_(594986, "uuid", lambda: uuid), "uuid4"), unique=True, primary_key=True, editable=False)
    _l_(594989)

    def __str__(self):
        _l_(594993)

        aux = _a_(594991, _n_(594990, "self", lambda: self), "value")
        _l_(594992)
        return aux


class Tag(_a_(594996, _n_(594995, "models", lambda: models), "Model")):
    _l_(595015)

    name = _c_(594999, _a_(594998, _n_(594997, "models", lambda: models), "CharField"), max_length=200)
    _l_(595000)
    created = _c_(595003, _a_(595002, _n_(595001, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(595004)
    id = _c_(595009, _a_(595006, _n_(595005, "models", lambda: models), "UUIDField"), default=_a_(595008, _n_(595007, "uuid", lambda: uuid), "uuid4"), unique=True, primary_key=True, editable=False)
    _l_(595010)

    def __str__(self):
        _l_(595014)

        aux = _a_(595012, _n_(595011, "self", lambda: self), "name")
        _l_(595013)
        return aux