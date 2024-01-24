# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66086091/peewee-query-typeerror-not-supported-between-instances-of-modelcompounds
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class People(_n_(555399, "Model", lambda: Model)):
    _l_(555404)

    name = _c_(555400, CharField)
    _l_(555401)
    parent = _c_(555402, ForeignKeyField, 'self', backref='children', null=True, on_delete='CASCADE')
    _l_(555403)