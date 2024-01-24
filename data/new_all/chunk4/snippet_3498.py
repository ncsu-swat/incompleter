# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73190803/migrations-error-in-django-attributeerror-str-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(625992)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(625994)

except ImportError:
    pass

class Reader(_a_(625996, _n_(625995, "models", lambda: models), "Model")):
    _l_(626040)

    rid = _c_(625999, _a_(625998, _n_(625997, "models", lambda: models), "AutoField"), primary_key=True)
    _l_(626000)
    user = _c_(626006, _a_(626002, _n_(626001, "models", lambda: models), "OneToOneField"), _n_(626003, "User", lambda: User), on_delete=_a_(626005, _n_(626004, "models", lambda: models), "CASCADE"))
    _l_(626007)
    photo_url = _c_(626010, _a_(626009, _n_(626008, "models", lambda: models), "CharField"), max_length=200, blank=True, null=True)
    _l_(626011)
    bio = _c_(626014, _a_(626013, _n_(626012, "models", lambda: models), "CharField"), max_length=200, blank=True, null=True)
    _l_(626015)
    read_books = _c_(626018, _a_(626017, _n_(626016, "models", lambda: models), "ManyToManyField"), 'book.Book', through='reads.Reads');
    _l_(626019)

    class Meta:
        _l_(626021)

        db_table = 'reader'
        _l_(626020)
    
    def __str__(self):
        _l_(626039)

        aux = {
            'username': _a_(626024, _a_(626023, _n_(626022, "self", lambda: self), "user"), "username"),
            'first_name': _a_(626027, _a_(626026, _n_(626025, "self", lambda: self), "user"), "first_name"),
            'last_name': _a_(626030, _a_(626029, _n_(626028, "self", lambda: self), "user"), "last_name"),
            'email': _a_(626033, _a_(626032, _n_(626031, "self", lambda: self), "user"), "email"),
            'photo_url': _a_(626035, _n_(626034, "self", lambda: self), "photo_url"),
            'bio': _a_(626037, _n_(626036, "self", lambda: self), "bio"),
        }
        _l_(626038)
        return aux