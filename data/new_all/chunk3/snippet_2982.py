# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56035632/peewee-model-has-no-select-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from peewee import *
    _l_(552512)

except ImportError:
    pass

db = _c_(552514, _n_(552513, "SqliteDatabase", lambda: SqliteDatabase), 'database/attendance.db')
_l_(552515)


class BaseModel:
    _l_(552519)


    class Meta:
        _l_(552518)

        database = _n_(552516, "db", lambda: db)
        _l_(552517)