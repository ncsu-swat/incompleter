# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46776974/sqlalchemy-1-2-attributeerror-list-object-has-no-attribute-session
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import sessionmaker
    _l_(665461)

except ImportError:
    pass
try:
    from .models import Deals, db_connect, create_deals_table
    _l_(665463)

except ImportError:
    pass

class Test(_n_(665464, "object", lambda: object)):
    _l_(665495)


    def __init__(self, args):
        _l_(665477)

        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = _c_(665466, _n_(665465, "db_connect", lambda: db_connect))
        _l_(665467)
        _c_(665470, _n_(665468, "create_deals_table", lambda: create_deals_table), _n_(665469, "engine", lambda: engine))
        _l_(665471)
        _n_(665472, "self", lambda: self).Session = _c_(665475, _n_(665473, "sessionmaker", lambda: sessionmaker), bind=_n_(665474, "engine", lambda: engine))
        _l_(665476)

    def add_item(self):
        _l_(665494)


        session = _c_(665480, _a_(665479, _n_(665478, "self", lambda: self), "Session"))
        _l_(665481)

        tester = _c_(665483, _n_(665482, "Deals", lambda: Deals), title="test 3 deal",location='here', price=2.00)
        _l_(665484)
        _c_(665488, _a_(665486, _n_(665485, "session", lambda: session), "add"), _n_(665487, "tester", lambda: tester))
        _l_(665489)
        _c_(665492, _a_(665491, _n_(665490, "session", lambda: session), "commit"))
        _l_(665493)