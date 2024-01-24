# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51715851/python-django-shell-attributeerror-article-object-has-no-attribute-title
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(567225)

except ImportError:
    pass

# Create your models here.
# A MODEL IS REPRESENTED BY CLASS

class Article(_a_(567227, _n_(567226, "models", lambda: models), "Model")):
    _l_(567248)

    title : _c_(567230, _a_(567229, _n_(567228, "models", lambda: models), "CharField"), max_length=100)
    _l_(567231)
    slug  : _c_(567234, _a_(567233, _n_(567232, "models", lambda: models), "SlugField"))
    _l_(567235)
    body  : _c_(567238, _a_(567237, _n_(567236, "models", lambda: models), "TextField"))
    _l_(567239)
    date  : _c_(567242, _a_(567241, _n_(567240, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(567243)
    # ADD IN THUMNAILL LETTER

    def __str__(self):
        _l_(567247)

        aux = _a_(567245, _n_(567244, "self", lambda: self), "title")
        _l_(567246)
        return aux