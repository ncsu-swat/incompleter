# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56035632/peewee-model-has-no-select-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from peewee import *
    _l_(567590)

except ImportError:
    pass
try:
    from models.basemodel import BaseModel
    _l_(567592)

except ImportError:
    pass


class Course(_n_(567593, "BaseModel", lambda: BaseModel)):
    _l_(567602)

    cid = _c_(567594, PrimaryKeyField)
    _l_(567595)
    title = _c_(567596, TextField)
    _l_(567597)
    active = _c_(567598, BooleanField)
    _l_(567599)

    class Meta:
        _l_(567601)

        table_name = 'courses'
        _l_(567600)