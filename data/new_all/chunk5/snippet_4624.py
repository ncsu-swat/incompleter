# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(665682)

except ImportError:
    pass

database_url = "mysql+pymysql://root:xxxx@localhost:3306/db1"
_l_(665683)
dbbind_url = "oracle://dbuser:xxxx@10.0.0.1:1521/db2" 
_l_(665684) 

_a_(665686, _n_(665685, "app", lambda: app), "config")["SQLALCHEMY_DATABASE_URI"] = _n_(665687, "database_url", lambda: database_url)
_l_(665688)
_a_(665690, _n_(665689, "app", lambda: app), "config")["SQLALCHEMY_BINDS"] = {
    'oracle': _n_(665691, "dbbind_url", lambda: dbbind_url)
     }
_l_(665692)
_a_(665694, _n_(665693, "app", lambda: app), "config")["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
_l_(665695) 

db = _c_(665698, _n_(665696, "SQLAlchemy", lambda: SQLAlchemy), _n_(665697, "app", lambda: app))
_l_(665699)