# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
## Mysql Model (working)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CUSTOMERS (_a_(670853, _n_(670852, "db", lambda: db), "Model")):
    _l_(670863)

    id = _c_(670856, _a_(670854, db, "Column"), _a_(670855, db, "Integer"), primary_key=True)
    _l_(670857)
    name = _c_(670861, _a_(670858, db, "Column"), _c_(670860, _a_(670859, db, "String"), 255))
    _l_(670862)
## Oracle Model (not working)
class ACCOUNT(_a_(670865, _n_(670864, "db", lambda: db), "Model")):
    _l_(670877)

    __tablename__ = 'ACCOUNT'
    _l_(670866)
    __bind_key__ = 'oracle'
    _l_(670867)
    account_id = _c_(670870, _a_(670868, db, "Column"), _a_(670869, db, "Integer"), unique=True, nullable=False, primary_key=True)
    _l_(670871)
    account = _c_(670875, _a_(670872, db, "Column"), _c_(670874, _a_(670873, db, "String"), 400), nullable=False)
    _l_(670876)