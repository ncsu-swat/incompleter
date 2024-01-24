# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29871522/type-error-authors-is-an-invalid-key-argument-for-this-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(601998)

except ImportError:
    pass

# Create your models here.
class Publisher(_a_(602000, _n_(601999, "models", lambda: models), "Model")):
    _l_(602029)

    name = _c_(602003, _a_(602002, _n_(602001, "models", lambda: models), "CharField"), max_length=30)
    _l_(602004)
    address = _c_(602007, _a_(602006, _n_(602005, "models", lambda: models), "CharField"), max_length=50)
    _l_(602008)
    city = _c_(602011, _a_(602010, _n_(602009, "models", lambda: models), "CharField"), max_length=60)
    _l_(602012)
    state_province = _c_(602015, _a_(602014, _n_(602013, "models", lambda: models), "CharField"), max_length=30)
    _l_(602016)
    country = _c_(602019, _a_(602018, _n_(602017, "models", lambda: models), "CharField"), max_length=30)
    _l_(602020)
    website = _c_(602023, _a_(602022, _n_(602021, "models", lambda: models), "URLField"))
    _l_(602024)

    def __str__(self):
        _l_(602028)

        aux = _a_(602026, _n_(602025, "self", lambda: self), "name")
        _l_(602027)
        return aux

class Author(_a_(602031, _n_(602030, "models", lambda: models), "Model")):
    _l_(602050)

    first_name = _c_(602034, _a_(602033, _n_(602032, "models", lambda: models), "CharField"), max_length=30)
    _l_(602035)
    last_name = _c_(602038, _a_(602037, _n_(602036, "models", lambda: models), "CharField"), max_length=40)
    _l_(602039)
    email = _c_(602042, _a_(602041, _n_(602040, "models", lambda: models), "EmailField"), verbose_name=' Your E-mail')
    _l_(602043)

    def __str__(self):
        _l_(602049)

        aux = "%s %s" %(_a_(602045, _n_(602044, "self", lambda: self), "first_name"), _a_(602047, _n_(602046, "self", lambda: self), "last_name"))
        _l_(602048)
        return aux

class Book(_a_(602052, _n_(602051, "models", lambda: models), "Model")):
    _l_(602075)

    title = _c_(602055, _a_(602054, _n_(602053, "models", lambda: models), "CharField"), max_length=100)
    _l_(602056)
    authors = _c_(602060, _a_(602058, _n_(602057, "models", lambda: models), "ManyToManyField"), _n_(602059, "Author", lambda: Author))
    _l_(602061)
    publisher = _c_(602065, _a_(602063, _n_(602062, "models", lambda: models), "ForeignKey"), _n_(602064, "Publisher", lambda: Publisher))
    _l_(602066)
    publication_date = _c_(602069, _a_(602068, _n_(602067, "models", lambda: models), "DateField"), blank=True, null=True)
    _l_(602070)

    def __str__(self):
        _l_(602074)

        aux = _a_(602072, _n_(602071, "self", lambda: self), "title")
        _l_(602073)
        return aux