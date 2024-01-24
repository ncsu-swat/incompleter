# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71359706/flask-login-attributeerror-str-object-has-no-attribute-is-active
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Admin(_a_(622540, _n_(622539, "db", lambda: db), "Model"), _n_(622541, "UserMixin", lambda: UserMixin)):
    _l_(622556)

    id = _c_(622544, _a_(622542, db, "Column"), _a_(622543, db, "Integer"), primary_key=True, autoincrement=True)
    _l_(622545)
    username = _c_(622549, _a_(622546, db, "Column"), _c_(622548, _a_(622547, db, "String"), 50), unique=True)
    _l_(622550)
    password = _c_(622554, _a_(622551, db, "Column"), _c_(622553, _a_(622552, db, "String"), 80))
    _l_(622555)