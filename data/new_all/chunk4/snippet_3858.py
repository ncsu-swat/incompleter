# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66471225/sqlalchemypython-typeerror-can-only-concatenate-tuple-not-rowproxy-to-tu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(605052, _a_(605051, _n_(605050, "sqlalchemy_engine", lambda: sqlalchemy_engine), "connect")) as conn:
    _l_(605065)

    ids = _c_(605059, _n_(605053, "sum", lambda: sum), _c_(605058, _n_(605054, "tuple", lambda: tuple), _c_(605057, _a_(605056, _n_(605055, "conn", lambda: conn), "execute"), 'select id from some_database.some_table')), ())   # statement causing error
    _l_(605060)   # statement causing error
    _c_(605063, _n_(605061, "print", lambda: print), _n_(605062, "ids", lambda: ids))
    _l_(605064)