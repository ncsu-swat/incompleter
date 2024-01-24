# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53995821/typeerror-str-object-is-not-callable-when-making-a-peewee-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
db = _c_(541323, _n_(541322, "SqliteDatabase", lambda: SqliteDatabase), "scores.db")
_l_(541324)


class Score(_n_(541325, "Model", lambda: Model)):
    _l_(541333)

    save = _c_(541326, CharField)
    _l_(541327)
    score = _c_(541328, IntegerField)
    _l_(541329)

    class Meta:
        _l_(541332)

        database = _n_(541330, "db", lambda: db)
        _l_(541331)