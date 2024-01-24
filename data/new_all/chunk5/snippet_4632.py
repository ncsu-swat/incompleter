# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53949270/sqlalchemy-flask-bind-not-working-nameerror-name-table-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(684605)

except ImportError:
    pass

database_url = "mysql+pymysql://root:xxxx@localhost:3306/db1"
_l_(684606)
dbbind_url = "oracle://dbuser:xxxx@10.0.0.1:1521/db2" 
_l_(684607) 

_a_(684609, _n_(684608, "app", lambda: app), "config")["SQLALCHEMY_DATABASE_URI"] = _n_(684610, "database_url", lambda: database_url)
_l_(684611)
_a_(684613, _n_(684612, "app", lambda: app), "config")["SQLALCHEMY_BINDS"] = {
    'oracle': _n_(684614, "dbbind_url", lambda: dbbind_url)
     }
_l_(684615)
_a_(684617, _n_(684616, "app", lambda: app), "config")["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
_l_(684618) 

db = _c_(684621, _n_(684619, "SQLAlchemy", lambda: SQLAlchemy), _n_(684620, "app", lambda: app))
_l_(684622)