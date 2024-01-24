# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(393715)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(393717)

except ImportError:
    pass
try:
    from sqlalchemy.ext.declarative import declarative_base
    _l_(393719)

except ImportError:
    pass
try:
    from sqlalchemy.orm import sessionmaker
    _l_(393721)

except ImportError:
    pass

SQLALCHEMY_DATABASE_URL = _a_(393723, _n_(393722, "os", lambda: os), "environ")["POSTGRES_LINK"]
_l_(393724)
engine = _c_(393727, _n_(393725, "create_engine", lambda: create_engine), _n_(393726, "SQLALCHEMY_DATABASE_URL", lambda: SQLALCHEMY_DATABASE_URL))
_l_(393728)
SessionLocal = _c_(393731, _n_(393729, "sessionmaker", lambda: sessionmaker), autocommit=False, autoflush=False, bind=_n_(393730, "engine", lambda: engine))
_l_(393732)

Base = _c_(393734, _n_(393733, "declarative_base", lambda: declarative_base))
_l_(393735)