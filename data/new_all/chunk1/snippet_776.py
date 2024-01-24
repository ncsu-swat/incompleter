# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55708257/flask-attributeerror-module-object-has-no-attribute-app
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(384378)

except ImportError:
    pass
try:
    import click
    _l_(384380)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(384382)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(384384)

except ImportError:
    pass
try:
    import flask_lab.tmp.test.demo
    _l_(384386)

except ImportError:
    pass

app = _c_(384389, _n_(384387, "Flask", lambda: Flask), _n_(384388, "__name__", lambda: __name__))
_l_(384390)
prefix = 'sqlite:////'
_l_(384391)
_a_(384393, _n_(384392, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = _n_(384394, "prefix", lambda: prefix) + _c_(384400, _a_(384397, _a_(384396, _n_(384395, "os", lambda: os), "path"), "join"), _a_(384399, _n_(384398, "app", lambda: app), "root_path"), 'data.db')
_l_(384401)
db = _c_(384404, _n_(384402, "SQLAlchemy", lambda: SQLAlchemy), _n_(384403, "app", lambda: app))
_l_(384405)

class User(_a_(384407, _n_(384406, "db", lambda: db), "Model")):
    _l_(384421)

    id = _c_(384412, _a_(384409, _n_(384408, "db", lambda: db), "Column"), _a_(384411, _n_(384410, "db", lambda: db), "Integer"), primary_key=True) 
    _l_(384413) 
    name = _c_(384419, _a_(384415, _n_(384414, "db", lambda: db), "Column"), _c_(384418, _a_(384417, _n_(384416, "db", lambda: db), "String"), 20))
    _l_(384420)

_c_(384425, _a_(384424, _a_(384423, _a_(384422, flask_lab, "tmp"), "test"), "demo"))
_l_(384426)