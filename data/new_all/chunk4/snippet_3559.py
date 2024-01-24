# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72217488/django-typeerror-field-id-expected-a-number-but-got-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(597572)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(597574)

except ImportError:
    pass


class Notebook(_a_(597576, _n_(597575, "models", lambda: models), "Model")):
    _l_(597592)

    user = _c_(597582, _a_(597578, _n_(597577, "models", lambda: models), "ForeignKey"), _n_(597579, "User", lambda: User), on_delete=_a_(597581, _n_(597580, "models", lambda: models), "CASCADE"), null=True, blank=True)
    _l_(597583)
    name = _c_(597586, _a_(597585, _n_(597584, "models", lambda: models), "CharField"), max_length=300, null=True)
    _l_(597587)

    def __str__(self):
        _l_(597591)

        aux = _a_(597589, _n_(597588, "self", lambda: self), "name")
        _l_(597590)
        return aux


class Notes(_a_(597594, _n_(597593, "models", lambda: models), "Model")):
    _l_(597625)

    notebook = _c_(597600, _a_(597596, _n_(597595, "models", lambda: models), "ForeignKey"), _n_(597597, "Notebook", lambda: Notebook), on_delete=_a_(597599, _n_(597598, "models", lambda: models), "CASCADE"))
    _l_(597601)
    user = _c_(597607, _a_(597603, _n_(597602, "models", lambda: models), "ForeignKey"), _n_(597604, "User", lambda: User), on_delete=_a_(597606, _n_(597605, "models", lambda: models), "CASCADE"), null=True, blank=True)
    _l_(597608)
    title = _c_(597611, _a_(597610, _n_(597609, "models", lambda: models), "CharField"), max_length=255, null=True)
    _l_(597612)
    content = _c_(597615, _a_(597614, _n_(597613, "models", lambda: models), "TextField"), null=True, blank=True)
    _l_(597616)
    date_created = _c_(597619, _a_(597618, _n_(597617, "models", lambda: models), "DateField"), auto_now_add=True)
    _l_(597620)

    def __str__(self):
        _l_(597624)

        aux = _a_(597622, _n_(597621, "self", lambda: self), "title")
        _l_(597623)
        return aux