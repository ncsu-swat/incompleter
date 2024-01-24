# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63543246/django-polling-app-typeerror-between-nonetype-and-datetime-datetime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(589734)

except ImportError:
    pass
try:
    from django.db import models
    _l_(589736)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(589738)

except ImportError:
    pass

# Create your models here.


class Question(_a_(589740, _n_(589739, "models", lambda: models), "Model")):
    _l_(589763)

    question_text = _c_(589743, _a_(589742, _n_(589741, "models", lambda: models), "CharField"), max_length=200)
    _l_(589744)
    pub_date = _c_(589747, _a_(589746, _n_(589745, "models", lambda: models), "DateTimeField"), 'date published')
    _l_(589748)

    def __str__(self):
        _l_(589752)

        aux = _a_(589750, _n_(589749, "self", lambda: self), "question_text")
        _l_(589751)
        return aux

    def was_published_recently(self):
        _l_(589762)

        aux = _a_(589754, _n_(589753, "self", lambda: self), "pub_date") >= _c_(589757, _a_(589756, _n_(589755, "timezone", lambda: timezone), "now")) - _c_(589760, _a_(589759, _n_(589758, "datetime", lambda: datetime), "timedelta"), days=1)
        _l_(589761)
        # now = timezone.now()
        return aux


class Choice(_a_(589765, _n_(589764, "models", lambda: models), "Model")):
    _l_(589785)

    question = _c_(589771, _a_(589767, _n_(589766, "models", lambda: models), "ForeignKey"), _n_(589768, "Question", lambda: Question), on_delete=_a_(589770, _n_(589769, "models", lambda: models), "CASCADE"))
    _l_(589772)
    choice_text = _c_(589775, _a_(589774, _n_(589773, "models", lambda: models), "CharField"), max_length=200)
    _l_(589776)
    votes = _c_(589779, _a_(589778, _n_(589777, "models", lambda: models), "IntegerField"), default=0)
    _l_(589780)

    def __str__(self):
        _l_(589784)

        aux = _a_(589782, _n_(589781, "self", lambda: self), "choice_text")
        _l_(589783)
        return aux