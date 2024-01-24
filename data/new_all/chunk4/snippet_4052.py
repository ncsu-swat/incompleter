# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63543246/django-polling-app-typeerror-between-nonetype-and-datetime-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(638123)

except ImportError:
    pass
try:
    from django.db import models
    _l_(638125)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(638127)

except ImportError:
    pass

# Create your models here.


class Question(_a_(638129, _n_(638128, "models", lambda: models), "Model")):
    _l_(638152)

    question_text = _c_(638132, _a_(638131, _n_(638130, "models", lambda: models), "CharField"), max_length=200)
    _l_(638133)
    pub_date = _c_(638136, _a_(638135, _n_(638134, "models", lambda: models), "DateTimeField"), 'date published')
    _l_(638137)

    def __str__(self):
        _l_(638141)

        aux = _a_(638139, _n_(638138, "self", lambda: self), "question_text")
        _l_(638140)
        return aux

    def was_published_recently(self):
        _l_(638151)

        aux = _a_(638143, _n_(638142, "self", lambda: self), "pub_date") >= _c_(638146, _a_(638145, _n_(638144, "timezone", lambda: timezone), "now")) - _c_(638149, _a_(638148, _n_(638147, "datetime", lambda: datetime), "timedelta"), days=1)
        _l_(638150)
        # now = timezone.now()
        return aux


class Choice(_a_(638154, _n_(638153, "models", lambda: models), "Model")):
    _l_(638174)

    question = _c_(638160, _a_(638156, _n_(638155, "models", lambda: models), "ForeignKey"), _n_(638157, "Question", lambda: Question), on_delete=_a_(638159, _n_(638158, "models", lambda: models), "CASCADE"))
    _l_(638161)
    choice_text = _c_(638164, _a_(638163, _n_(638162, "models", lambda: models), "CharField"), max_length=200)
    _l_(638165)
    votes = _c_(638168, _a_(638167, _n_(638166, "models", lambda: models), "IntegerField"), default=0)
    _l_(638169)

    def __str__(self):
        _l_(638173)

        aux = _a_(638171, _n_(638170, "self", lambda: self), "choice_text")
        _l_(638172)
        return aux