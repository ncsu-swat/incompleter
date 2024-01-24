# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73190803/migrations-error-in-django-attributeerror-str-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(617265)

except ImportError:
    pass
try:
    from genre.models import Genre
    _l_(617267)

except ImportError:
    pass
try:
    from reader.models import Reader
    _l_(617269)

except ImportError:
    pass

class Book(_a_(617271, _n_(617270, "models", lambda: models), "Model")):
    _l_(617336)

    isbn = _c_(617274, _a_(617273, _n_(617272, "models", lambda: models), "CharField"), max_length=13,primary_key=True)
    _l_(617275)
    title = _c_(617278, _a_(617277, _n_(617276, "models", lambda: models), "CharField"), max_length=255)
    _l_(617279)
    description = _c_(617282, _a_(617281, _n_(617280, "models", lambda: models), "TextField"))
    _l_(617283)
    photo_url = _c_(617286, _a_(617285, _n_(617284, "models", lambda: models), "CharField"), max_length=255)
    _l_(617287)
    page_count = _c_(617290, _a_(617289, _n_(617288, "models", lambda: models), "IntegerField"))
    _l_(617291)
    created_at = _c_(617294, _a_(617293, _n_(617292, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(617295)
    updated_at = _c_(617298, _a_(617297, _n_(617296, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(617299)
    genres = _c_(617303, _a_(617301, _n_(617300, "models", lambda: models), "ManyToManyField"), _n_(617302, "Genre", lambda: Genre))
    _l_(617304)
    authors = _c_(617308, _a_(617306, _n_(617305, "models", lambda: models), "ManyToManyField"), _n_(617307, "Reader", lambda: Reader), related_name='authored_books')
    _l_(617309)

    class Meta:
        _l_(617311)

        db_table = 'book'
        _l_(617310)
    def __str__(self):
        _l_(617335)

        aux = {
            'isbn': _a_(617313, _n_(617312, "self", lambda: self), "isbn"),
            'title': _a_(617315, _n_(617314, "self", lambda: self), "title"),
            'description': _a_(617317, _n_(617316, "self", lambda: self), "description"),
            'photo_url': _a_(617319, _n_(617318, "self", lambda: self), "photo_url"),
            'page_count': _a_(617321, _n_(617320, "self", lambda: self), "page_count"),
            'created_at': _a_(617323, _n_(617322, "self", lambda: self), "created_at"),
            'updated_at': _a_(617325, _n_(617324, "self", lambda: self), "updated_at"),
            'genres': _c_(617329, _a_(617328, _a_(617327, _n_(617326, "self", lambda: self), "genres"), "all")),
            'authors': _c_(617333, _a_(617332, _a_(617331, _n_(617330, "self", lambda: self), "authors"), "all")),
        }
        _l_(617334)
        return aux