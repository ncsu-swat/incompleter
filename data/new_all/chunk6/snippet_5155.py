# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73786094/error-attributeerror-connection-object-has-no-attribute-fetchall
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sqlalchemy as sch
    _l_(357426)

except ImportError:
    pass
try:
    from config import Config
    _l_(357428)

except ImportError:
    pass

db_uri = _a_(357430, _n_(357429, "os", lambda: os), "environ")["SQLALCHEMY_DATABASE_URI"] + _a_(357432, _n_(357431, "os", lambda: os), "environ")["DB_NAME"]
_l_(357433)