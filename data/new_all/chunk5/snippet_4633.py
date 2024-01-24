# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
## Mysql Model (working)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CUSTOMERS (_a_(688682, _n_(688681, "db", lambda: db), "Model")):
    _l_(688692)

    id = _c_(688685, _a_(688683, db, "Column"), _a_(688684, db, "Integer"), primary_key=True)
    _l_(688686)
    name = _c_(688690, _a_(688687, db, "Column"), _c_(688689, _a_(688688, db, "String"), 255))
    _l_(688691)
## Oracle Model (not working)
class ACCOUNT(_a_(688694, _n_(688693, "db", lambda: db), "Model")):
    _l_(688706)

    __tablename__ = 'ACCOUNT'
    _l_(688695)
    __bind_key__ = 'oracle'
    _l_(688696)
    account_id = _c_(688699, _a_(688697, db, "Column"), _a_(688698, db, "Integer"), unique=True, nullable=False, primary_key=True)
    _l_(688700)
    account = _c_(688704, _a_(688701, db, "Column"), _c_(688703, _a_(688702, db, "String"), 400), nullable=False)
    _l_(688705)