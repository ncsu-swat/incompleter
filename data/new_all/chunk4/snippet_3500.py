# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73190803/migrations-error-in-django-attributeerror-str-object-has-no-attribute-meta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(632654)

except ImportError:
    pass
try:
    from reader.models import Reader
    _l_(632656)

except ImportError:
    pass
try:
    from book.models import Book
    _l_(632658)

except ImportError:
    pass

class Reads(_a_(632660, _n_(632659, "models", lambda: models), "Model")):
    _l_(632709)

    status_choices = (
        ('w', 'Want to Read'),
        ('r', 'Reading'),
        ('c', 'Completed'),
    )
    _l_(632661)
    rsid = _c_(632664, _a_(632663, _n_(632662, "models", lambda: models), "AutoField"), primary_key=True)
    _l_(632665)
    reader = _c_(632671, _a_(632667, _n_(632666, "models", lambda: models), "ForeignKey"), _n_(632668, "Reader", lambda: Reader), on_delete=_a_(632670, _n_(632669, "models", lambda: models), "CASCADE"))
    _l_(632672)
    book = _c_(632678, _a_(632674, _n_(632673, "models", lambda: models), "ForeignKey"), _n_(632675, "Book", lambda: Book), on_delete=_a_(632677, _n_(632676, "models", lambda: models), "CASCADE"))
    _l_(632679)
    created_at = _c_(632682, _a_(632681, _n_(632680, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(632683)
    updated_at = _c_(632686, _a_(632685, _n_(632684, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(632687)
    status = _c_(632690, _a_(632689, _n_(632688, "models", lambda: models), "CharField"), max_length=1, choices=status_choices)
    _l_(632691)

    class Meta:
        _l_(632693)

        db_table = 'reads'
        _l_(632692)
    def __str__(self):
        _l_(632708)

        aux = {
            'reader': _a_(632697, _a_(632696, _a_(632695, _n_(632694, "self", lambda: self), "reader"), "user"), "username"),
            'book': _a_(632700, _a_(632699, _n_(632698, "self", lambda: self), "book"), "title"),
            'created_at': _a_(632702, _n_(632701, "self", lambda: self), "created_at"),
            'updated_at': _a_(632704, _n_(632703, "self", lambda: self), "updated_at"),
            'status': _a_(632706, _n_(632705, "self", lambda: self), "status"),
        }
        _l_(632707)
        return aux