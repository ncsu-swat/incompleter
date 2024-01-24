# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(438335)

except ImportError:
    pass

class Config(_n_(438336, "object", lambda: object)):
    _l_(438347)

    SECRET_KEY = _c_(438340, _a_(438339, _a_(438338, _n_(438337, "os", lambda: os), "environ"), "get"), 'SECRET_KEY') or 'you-will-never-know'
    _l_(438341)
    DATABASE = {
        'name': 'comparteme',                        
        'engine': 'peewee.MySQLDatabase',            
        'user': 'root',
        'password': 'whatever',                
        'host': _c_(438345, _a_(438344, _a_(438343, _n_(438342, "os", lambda: os), "environ"), "get"), 'DATABASE_URL') or 'mysql://root@localhost:3306'
    }
    _l_(438346)