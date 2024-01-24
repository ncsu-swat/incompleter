# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63873696/python-type-error-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(558218)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(558220)

except ImportError:
    pass
try:
    import pyAesCrypt
    _l_(558222)

except ImportError:
    pass

app = _c_(558225, _n_(558223, "Flask", lambda: Flask), _n_(558224, "__name__", lambda: __name__))
_l_(558226)
_a_(558228, _n_(558227, "app", lambda: app), "config")["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data-users2.sqlite"
_l_(558229)
db = _c_(558232, _n_(558230, "SQLAlchemy", lambda: SQLAlchemy), _n_(558231, "app", lambda: app))
_l_(558233)


class User(_a_(558235, _n_(558234, "db", lambda: db), "Model")):
    _l_(558274)

    __tablename__ = "user"
    _l_(558236)
    id = _c_(558242, _a_(558238, _n_(558237, "db", lambda: db), "Column"), _c_(558241, _a_(558240, _n_(558239, "db", lambda: db), "Integer")), primary_key=True, autoincrement=True)
    _l_(558243)
    username = _c_(558249, _a_(558245, _n_(558244, "db", lambda: db), "Column"), _c_(558248, _a_(558247, _n_(558246, "db", lambda: db), "String"), 64), unique=True)
    _l_(558250)
    pwd = _c_(558256, _a_(558252, _n_(558251, "db", lambda: db), "Column"), _c_(558255, _a_(558254, _n_(558253, "db", lambda: db), "LargeBinary")), unique=True)
    _l_(558257)

    def __init__(self, id, username, pwd):
        _l_(558273)

        p = _c_(558259, _n_(558258, "pyAesCrypt", lambda: pyAesCrypt), encoding=False)
        _l_(558260)
        _n_(558261, "self", lambda: self).id = _n_(558262, "id", lambda: id)
        _l_(558263)
        _n_(558264, "self", lambda: self).username = _n_(558265, "username", lambda: username)
        _l_(558266)
        _n_(558267, "self", lambda: self).pwd = _c_(558271, _a_(558269, _n_(558268, "p", lambda: p), "encrypt"), "password",_n_(558270, "pwd", lambda: pwd))
        _l_(558272)