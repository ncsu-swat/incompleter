# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlalchemy
    _l_(452571)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(452573)

except ImportError:
    pass
try:
    from sqlalchemy.ext.declarative import declarative_base
    _l_(452575)

except ImportError:
    pass
try:
    from sqlalchemy.orm import sessionmaker
    _l_(452577)

except ImportError:
    pass

schema_name = 'Traffic'
_l_(452578)

engine = _c_(452580, _n_(452579, "create_engine", lambda: create_engine), 'postgresql://xxx:xxx@localhost:5432/xxx')
_l_(452581)

if not _c_(452587, _a_(452584, _a_(452583, _n_(452582, "engine", lambda: engine), "dialect"), "has_schema"), _n_(452585, "engine", lambda: engine), _n_(452586, "schema_name", lambda: schema_name)):
    _l_(452597)

    _c_(452595, _a_(452589, _n_(452588, "engine", lambda: engine), "execute"), _c_(452594, _a_(452592, _a_(452591, _n_(452590, "sqlalchemy", lambda: sqlalchemy), "schema"), "CreateSchema"), _n_(452593, "schema_name", lambda: schema_name)))
    _l_(452596)

Session = _c_(452600, _n_(452598, "sessionmaker", lambda: sessionmaker), bind=_n_(452599, "engine", lambda: engine))
_l_(452601)
session = _c_(452603, _n_(452602, "Session", lambda: Session))
_l_(452604)
Base = _c_(452606, _n_(452605, "declarative_base", lambda: declarative_base))
_l_(452607)