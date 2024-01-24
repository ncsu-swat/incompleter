# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import peewee
    _l_(453049)

except ImportError:
    pass
try:
    from comparteme import db
    _l_(453051)

except ImportError:
    pass


class BaseModel(_a_(453053, _n_(453052, "peewee", lambda: peewee), "Model")):
    _l_(453057)

    class Meta:
        _l_(453056)

        database = _n_(453054, "db", lambda: db)
        _l_(453055)


class User(_n_(453058, "BaseModel", lambda: BaseModel)):
    _l_(453063)

    username = _c_(453061, _a_(453060, _n_(453059, "peewee", lambda: peewee), "CharField"), unique=True)
    _l_(453062)