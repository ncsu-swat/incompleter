# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46776974/sqlalchemy-1-2-attributeerror-list-object-has-no-attribute-session
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import sessionmaker
    _l_(680119)

except ImportError:
    pass
try:
    from .models import Deals, db_connect, create_deals_table
    _l_(680121)

except ImportError:
    pass

class Test(_n_(680122, "object", lambda: object)):
    _l_(680153)


    def __init__(self, args):
        _l_(680135)

        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = _c_(680124, _n_(680123, "db_connect", lambda: db_connect))
        _l_(680125)
        _c_(680128, _n_(680126, "create_deals_table", lambda: create_deals_table), _n_(680127, "engine", lambda: engine))
        _l_(680129)
        _n_(680130, "self", lambda: self).Session = _c_(680133, _n_(680131, "sessionmaker", lambda: sessionmaker), bind=_n_(680132, "engine", lambda: engine))
        _l_(680134)

    def add_item(self):
        _l_(680152)


        session = _c_(680138, _a_(680137, _n_(680136, "self", lambda: self), "Session"))
        _l_(680139)

        tester = _c_(680141, _n_(680140, "Deals", lambda: Deals), title="test 3 deal",location='here', price=2.00)
        _l_(680142)
        _c_(680146, _a_(680144, _n_(680143, "session", lambda: session), "add"), _n_(680145, "tester", lambda: tester))
        _l_(680147)
        _c_(680150, _a_(680149, _n_(680148, "session", lambda: session), "commit"))
        _l_(680151)