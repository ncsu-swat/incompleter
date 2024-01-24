# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, jsonify, request, json
    _l_(668193)

except ImportError:
    pass
try:
    import psycopg2
    _l_(668195)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(668197)

except ImportError:
    pass
try:
    from flask_cors import CORS
    _l_(668199)

except ImportError:
    pass
try:
    from flask_bcrypt import Bcrypt
    _l_(668201)

except ImportError:
    pass
try:
    from flask_jwt_extended import JWTManager
    _l_(668203)

except ImportError:
    pass
try:
    from flask_jwt_extended import create_access_token
    _l_(668205)

except ImportError:
    pass


app = _c_(668208, _n_(668206, "Flask", lambda: Flask), _n_(668207, "__name__", lambda: __name__))
_l_(668209)
conn = _c_(668212, _a_(668211, _n_(668210, "psycopg2", lambda: psycopg2), "connect"), host="localhost", database="practise",
                        user="postgres", password="dbA@pr3mium")
_l_(668213)
bcrypt = _c_(668216, _n_(668214, "Bcrypt", lambda: Bcrypt), _n_(668215, "app", lambda: app))
_l_(668217)
jwt = _c_(668220, _n_(668218, "JWTManager", lambda: JWTManager), _n_(668219, "app", lambda: app))
_l_(668221)
_c_(668224, _n_(668222, "CORS", lambda: CORS), _n_(668223, "app", lambda: app))
_l_(668225)
try:
    import login
    _l_(668227)

except ImportError:
    pass