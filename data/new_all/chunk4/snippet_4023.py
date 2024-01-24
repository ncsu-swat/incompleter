# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63885766/python-error-typeerror-module-object-is-notcallable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(645899)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(645901)

except ImportError:
    pass
try:
    import pyAesCrypt
    _l_(645903)

except ImportError:
    pass

app = _c_(645906, _n_(645904, "Flask", lambda: Flask), _n_(645905, "__name__", lambda: __name__))
_l_(645907)
_a_(645909, _n_(645908, "app", lambda: app), "config")["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data-users2.sqlite"
_l_(645910)
db = _c_(645913, _n_(645911, "SQLAlchemy", lambda: SQLAlchemy), _n_(645912, "app", lambda: app))
_l_(645914)


class User(_a_(645916, _n_(645915, "db", lambda: db), "Model")):
    _l_(645955)

    __tablename__ = "user"
    _l_(645917)
    id = _c_(645923, _a_(645919, _n_(645918, "db", lambda: db), "Column"), _c_(645922, _a_(645921, _n_(645920, "db", lambda: db), "Integer")), primary_key=True, autoincrement=True)
    _l_(645924)
    username = _c_(645930, _a_(645926, _n_(645925, "db", lambda: db), "Column"), _c_(645929, _a_(645928, _n_(645927, "db", lambda: db), "String"), 64), unique=True)
    _l_(645931)
    pwd = _c_(645937, _a_(645933, _n_(645932, "db", lambda: db), "Column"), _c_(645936, _a_(645935, _n_(645934, "db", lambda: db), "LargeBinary")), unique=True)
    _l_(645938)

    def __init__(self, id, username, pwd):
        _l_(645954)

        p = _c_(645940, _n_(645939, "pyAesCrypt", lambda: pyAesCrypt), encoding=False)
        _l_(645941)
        _n_(645942, "self", lambda: self).id = _n_(645943, "id", lambda: id)
        _l_(645944)
        _n_(645945, "self", lambda: self).username = _n_(645946, "username", lambda: username)
        _l_(645947)
        _n_(645948, "self", lambda: self).pwd = _c_(645952, _a_(645950, _n_(645949, "p", lambda: p), "encrypt"), "password",_n_(645951, "pwd", lambda: pwd))
        _l_(645953)