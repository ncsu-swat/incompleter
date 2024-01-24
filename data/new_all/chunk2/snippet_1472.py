# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54570871/attributeerror-sqlalchemy-object-has-no-attribute-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(424060)

except ImportError:
    pass
try:
    from flask import Flask, render_template, url_for,flash,redirect
    _l_(424062)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(424064)

except ImportError:
    pass
try:
    from forms import RegistrationForm, LoginForm
    _l_(424066)

except ImportError:
    pass

app = _c_(424069, _n_(424067, "Flask", lambda: Flask), _n_(424068, "__name__", lambda: __name__))    #name of the module
_l_(424070)    #name of the module
_a_(424072, _n_(424071, "app", lambda: app), "config")['SECRET_KEY']= 'b2ffa54db1c495dab1f21973b39c400a'
_l_(424073)
_a_(424075, _n_(424074, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
_l_(424076)
db =  _c_(424079, _n_(424077, "SQLAlchemy", lambda: SQLAlchemy), _n_(424078, "app", lambda: app))
_l_(424080)


class User(_a_(424082, _n_(424081, "db", lambda: db), "Model")):
    _l_(424129)

    id = _c_(424087, _a_(424084, _n_(424083, "db", lambda: db), "column"), _a_(424086, _n_(424085, "db", lambda: db), "integer"), primary_key=True)
    _l_(424088)
    username = _c_(424094, _a_(424090, _n_(424089, "db", lambda: db), "column"), _c_(424093, _a_(424092, _n_(424091, "db", lambda: db), "string"), 25), unique=True, 
nullable=False)
    _l_(424095)
    email = _c_(424101, _a_(424097, _n_(424096, "db", lambda: db), "column"), _c_(424100, _a_(424099, _n_(424098, "db", lambda: db), "string"), 100), unique=True, nullable=False)
    _l_(424102)
    password = _c_(424108, _a_(424104, _n_(424103, "db", lambda: db), "column"), _c_(424107, _a_(424106, _n_(424105, "db", lambda: db), "string"), 100), unique=True, 
nullable=False)
    _l_(424109)
    image_file = _c_(424115, _a_(424111, _n_(424110, "db", lambda: db), "column"), _c_(424114, _a_(424113, _n_(424112, "db", lambda: db), "string"), 20), nullable=False, 
default='default.jpg')
    _l_(424116)
    posts = _c_(424119, _a_(424118, _n_(424117, "db", lambda: db), "relationship"), 'Post', backreff='author', lazy=True)
    _l_(424120)


    def __repr__(self):
        _l_(424128)

        aux = f"user('{_a_(424122, _n_(424121, 'self', lambda: self), 'username')}','{_a_(424124, _n_(424123, 'self', lambda: self), 'email')}', '{_a_(424126, _n_(424125, 'self', lambda: self), 'image_file')}')"
        _l_(424127)
        return aux

class Post(_a_(424131, _n_(424130, "db", lambda: db), "Model")):
    _l_(424159)

    id = _c_(424136, _a_(424133, _n_(424132, "db", lambda: db), "column"), _a_(424135, _n_(424134, "db", lambda: db), "integer"), primary_key=True)
    _l_(424137)
    title = _c_(424143, _a_(424139, _n_(424138, "db", lambda: db), "column"), _c_(424142, _a_(424141, _n_(424140, "db", lambda: db), "String"), 120), nullable=False)
    _l_(424144)
    date_posted = _c_(424151, _a_(424146, _n_(424145, "db", lambda: db), "column"), _a_(424148, _n_(424147, "db", lambda: db), "DateTime"), nullable=False, default=_a_(424150, _n_(424149, "datetime", lambda: datetime), "utcnow"))
    _l_(424152)
    content = _c_(424157, _a_(424154, _n_(424153, "db", lambda: db), "column"), _a_(424156, _n_(424155, "db", lambda: db), "Text"), nullable=False)
    _l_(424158)

def __repr__(self):
    _l_(424165)

    aux = f"post('{_a_(424161, _n_(424160, 'self', lambda: self), 'title')}','{_a_(424163, _n_(424162, 'self', lambda: self), 'date_posted')}')"
    _l_(424164)
    return aux