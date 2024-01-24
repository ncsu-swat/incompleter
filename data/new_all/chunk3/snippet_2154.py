# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(534392)

except ImportError:
    pass
try:
    import unittest
    _l_(534394)

except ImportError:
    pass
try:
    from flask_script import Manager
    _l_(534396)

except ImportError:
    pass
try:
    from api import blueprint
    _l_(534398)

except ImportError:
    pass
try:
    from api.database import  db
    _l_(534400)

except ImportError:
    pass
try:
    from api.database.db import Location, Essential
    _l_(534402)

except ImportError:
    pass

app = _c_(534405, _a_(534404, _n_(534403, "db", lambda: db), "init_app"))
_l_(534406)
_c_(534410, _a_(534408, _n_(534407, "app", lambda: app), "register_blueprint"), _n_(534409, "blueprint", lambda: blueprint))
_l_(534411)

_c_(534416, _a_(534415, _c_(534414, _a_(534413, _n_(534412, "app", lambda: app), "app_context")), "push"))
_l_(534417)

manager = _c_(534420, _n_(534418, "Manager", lambda: Manager), _n_(534419, "app", lambda: app))
_l_(534421)

@_a_(534423, _n_(534422, "manager", lambda: manager), "command")
def run():
    _l_(534428)

    _c_(534426, _a_(534425, _n_(534424, "app", lambda: app), "run"))
    _l_(534427)


if _n_(534429, "__name__", lambda: __name__) == '__main__':
    _l_(534434)

    _c_(534432, _a_(534431, _n_(534430, "manager", lambda: manager), "run"))
    _l_(534433)