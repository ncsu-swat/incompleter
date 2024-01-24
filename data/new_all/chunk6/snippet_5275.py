# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
# config.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(359600)

except ImportError:
    pass
try:
    from flask_mysql_connector import MySQL
    _l_(359602)

except ImportError:
    pass

class Config(_n_(359603, "object", lambda: object)):
    _l_(359613)

    SECRET_KEY = _c_(359607, _a_(359606, _a_(359605, _n_(359604, "os", lambda: os), "environ"), "get"), 'SECRET_KEY') or 'djfdsjdsj4skldjess85'
    _l_(359608)

    MYSQL_DATABASE_HOST = 'localhost'
    _l_(359609)
    MYSQL_DATABASE_USER = 'flasker'
    _l_(359610)
    MYSQL_DATABASE_PASSWORD = '**********'
    _l_(359611)
    MYSQL_DATABASE_DB = 'UTA_Enrollment'
    _l_(359612)