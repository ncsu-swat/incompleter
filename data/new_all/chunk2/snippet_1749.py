# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58603924/attributeerror-object-has-no-attribute-user-loader
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(453197)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(453199)

except ImportError:
    pass
try:
    from flask_bcrypt import Bcrypt
    _l_(453201)

except ImportError:
    pass
try:
    from flask_login import LoginManager
    _l_(453203)

except ImportError:
    pass


app = _c_(453206, _n_(453204, "Flask", lambda: Flask), _n_(453205, "__name__", lambda: __name__))
_l_(453207)
_a_(453209, _n_(453208, "app", lambda: app), "config")['SECRET_KEY'] = 'xxx'
_l_(453210)
_a_(453212, _n_(453211, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
_l_(453213)
db = _c_(453216, _n_(453214, "SQLAlchemy", lambda: SQLAlchemy), _n_(453215, "app", lambda: app))
_l_(453217)
bcrypt = _c_(453220, _n_(453218, "Bcrypt", lambda: Bcrypt), _n_(453219, "app", lambda: app))
_l_(453221)


login_manager = _c_(453224, _n_(453222, "LoginManager", lambda: LoginManager), _n_(453223, "app", lambda: app))
_l_(453225)
_n_(453226, "login_manager", lambda: login_manager).login_view = 'login'
_l_(453227)
login_manager = login_message_category = 'info'
_l_(453228)
try:
    from flaskapp import routes
    _l_(453230)

except ImportError:
    pass