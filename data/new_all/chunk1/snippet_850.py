# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62985644/python-django-typeerror-expected-string-or-bytes-like-object-error-object-sa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(395493)

except ImportError:
    pass
# Create your models here.
class Author(_a_(395495, _n_(395494, "models", lambda: models), "Model")):
    _l_(395508)

    def __str__(self):
        _l_(395499)

        aux = _a_(395497, _n_(395496, "self", lambda: self), "name")
        _l_(395498)
        return aux
    name = _c_(395502, _a_(395501, _n_(395500, "models", lambda: models), "CharField"), max_length=50)
    _l_(395503)
    created = _c_(395506, _a_(395505, _n_(395504, "models", lambda: models), "DateTimeField")) 
    _l_(395507) 
class Book(_a_(395510, _n_(395509, "models", lambda: models), "Model")):
    _l_(395534)

    def __str__(self):
        _l_(395514)

        aux = _a_(395512, _n_(395511, "self", lambda: self), "name")
        _l_(395513)
        return aux
    name = _c_(395517, _a_(395516, _n_(395515, "models", lambda: models), "CharField"), max_length=50) 
    _l_(395518) 
    created = _c_(395521, _a_(395520, _n_(395519, "models", lambda: models), "DateTimeField"))
    _l_(395522)
    
    author = _c_(395528, _a_(395524, _n_(395523, "models", lambda: models), "ForeignKey"), _n_(395525, "Author", lambda: Author), on_delete = _a_(395527, _n_(395526, "models", lambda: models), "CASCADE")) 
    _l_(395529) 
    price = _c_(395532, _a_(395531, _n_(395530, "models", lambda: models), "DecimalField"), decimal_places=2, max_digits=4, null=True)
    _l_(395533)