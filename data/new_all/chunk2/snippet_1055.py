# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import peewee
    _l_(447868)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(447870)

except ImportError:
    pass
try:
    from config import Config
    _l_(447872)

except ImportError:
    pass

app = _c_(447875, _n_(447873, "Flask", lambda: Flask), _n_(447874, "__name__", lambda: __name__))
_l_(447876)
_c_(447881, _a_(447879, _a_(447878, _n_(447877, "app", lambda: app), "config"), "from_object"), _n_(447880, "Config", lambda: Config))
_l_(447882)

db = _a_(447887, _c_(447886, _a_(447884, _n_(447883, "peewee", lambda: peewee), "MySQLDatabase"), _n_(447885, "app", lambda: app)), "database")
_l_(447888)
try:
    from comparteme import routes
    _l_(447890)

except ImportError:
    pass