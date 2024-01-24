# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66471225/sqlalchemypython-typeerror-can-only-concatenate-tuple-not-rowproxy-to-tu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(634868, _a_(634867, _n_(634866, "sqlalchemy_engine", lambda: sqlalchemy_engine), "connect")) as conn:
    _l_(634881)

    ids = _c_(634875, _n_(634869, "sum", lambda: sum), _c_(634874, _n_(634870, "tuple", lambda: tuple), _c_(634873, _a_(634872, _n_(634871, "conn", lambda: conn), "execute"), 'select id from some_database.some_table')), ())   # statement causing error
    _l_(634876)   # statement causing error
    _c_(634879, _n_(634877, "print", lambda: print), _n_(634878, "ids", lambda: ids))
    _l_(634880)