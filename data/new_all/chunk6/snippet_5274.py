# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# __init__.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(361968)

except ImportError:
    pass
try:
    from config import Config
    _l_(361970)

except ImportError:
    pass
try:
    from flaskext.mysql import MySQL
    _l_(361972)

except ImportError:
    pass


app = _c_(361975, _n_(361973, "Flask", lambda: Flask), _n_(361974, "__name__", lambda: __name__))
_l_(361976)
_c_(361981, _a_(361979, _a_(361978, _n_(361977, "app", lambda: app), "config"), "from_object"), _n_(361980, "Config", lambda: Config))
_l_(361982)

mysql = _c_(361984, _n_(361983, "MySQL", lambda: MySQL))
_l_(361985)
_c_(361989, _a_(361987, _n_(361986, "mysql", lambda: mysql), "init_app"), _n_(361988, "app", lambda: app))
_l_(361990)
try:
    from application import routes
    _l_(361992)

except ImportError:
    pass