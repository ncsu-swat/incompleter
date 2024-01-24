# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63900355/flaskflask-db-init-attributeerror-module-time-has-no-attribute-clock
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(436956)

except ImportError:
    pass
try:
    import os
    _l_(436958)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(436960)

except ImportError:
    pass
try:
    from flask_migrate import Migrate
    _l_(436962)

except ImportError:
    pass

basedir = _c_(436971, _a_(436965, _a_(436964, _n_(436963, "os", lambda: os), "path"), "abspath"), _c_(436970, _a_(436968, _a_(436967, _n_(436966, "os", lambda: os), "path"), "dirname"), _n_(436969, "__file__", lambda: __file__)))   #Full directory path of the file I'm working with..here, sql1.py
_l_(436972)   #Full directory path of the file I'm working with..here, sql1.py

app = _c_(436975, _n_(436973, "Flask", lambda: Flask), _n_(436974, "__name__", lambda: __name__))
_l_(436976)
_a_(436978, _n_(436977, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + _c_(436983, _a_(436981, _a_(436980, _n_(436979, "os", lambda: os), "path"), "join"), _n_(436982, "basedir", lambda: basedir), 'data.sqlite')
_l_(436984)
_a_(436986, _n_(436985, "app", lambda: app), "config")['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
_l_(436987) 
db = _c_(436990, _n_(436988, "SQLAlchemy", lambda: SQLAlchemy), _n_(436989, "app", lambda: app))
_l_(436991)

_c_(436995, _n_(436992, "Migrate", lambda: Migrate), _n_(436993, "app", lambda: app),_n_(436994, "db", lambda: db)) #Here it connect the application "app.py"
_l_(436996) #Here it connect the application "app.py"
                # with the database "db"    
class puppy(_a_(436998, _n_(436997, "db", lambda: db), "Model")):
    _l_(437031)

    __tablename__ = 'Name Provided by me!!'
    _l_(436999)
    id = _c_(437004, _a_(437001, _n_(437000, "db", lambda: db), "Column"), _a_(437003, _n_(437002, "db", lambda: db), "Integer"),primary_key = True)
    _l_(437005)
    name = _c_(437010, _a_(437007, _n_(437006, "db", lambda: db), "Column"), _a_(437009, _n_(437008, "db", lambda: db), "Text"))
    _l_(437011)
    age = _c_(437016, _a_(437013, _n_(437012, "db", lambda: db), "Column"), _a_(437015, _n_(437014, "db", lambda: db), "Integer"))
    _l_(437017)
    
    def __init__(self,name,age):
        _l_(437024)

        _n_(437018, "self", lambda: self).name = _n_(437019, "name", lambda: name)
        _l_(437020)
        _n_(437021, "self", lambda: self).age = _n_(437022, "age", lambda: age)
        _l_(437023)
    def __repr__(self):
        _l_(437030)

        aux = f"puppy {_a_(437026, _n_(437025, 'self', lambda: self), 'name')} is {_a_(437028, _n_(437027, 'self', lambda: self), 'age')} year/s old!"
        _l_(437029)
        return aux