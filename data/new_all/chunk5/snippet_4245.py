# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, jsonify, request, json
    _l_(700626)

except ImportError:
    pass
try:
    import psycopg2
    _l_(700628)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(700630)

except ImportError:
    pass
try:
    from flask_cors import CORS
    _l_(700632)

except ImportError:
    pass
try:
    from flask_bcrypt import Bcrypt
    _l_(700634)

except ImportError:
    pass
try:
    from flask_jwt_extended import JWTManager
    _l_(700636)

except ImportError:
    pass
try:
    from flask_jwt_extended import create_access_token
    _l_(700638)

except ImportError:
    pass


app = _c_(700641, _n_(700639, "Flask", lambda: Flask), _n_(700640, "__name__", lambda: __name__))
_l_(700642)
conn = _c_(700645, _a_(700644, _n_(700643, "psycopg2", lambda: psycopg2), "connect"), host="localhost", database="practise",
                        user="postgres", password="dbA@pr3mium")
_l_(700646)
bcrypt = _c_(700649, _n_(700647, "Bcrypt", lambda: Bcrypt), _n_(700648, "app", lambda: app))
_l_(700650)
jwt = _c_(700653, _n_(700651, "JWTManager", lambda: JWTManager), _n_(700652, "app", lambda: app))
_l_(700654)
_c_(700657, _n_(700655, "CORS", lambda: CORS), _n_(700656, "app", lambda: app))
_l_(700658)
try:
    import login
    _l_(700660)

except ImportError:
    pass