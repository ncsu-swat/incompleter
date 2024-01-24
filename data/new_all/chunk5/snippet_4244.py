# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from app import app, conn, bcrypt
    _l_(702952)

except ImportError:
    pass
try:
    from flask import request, jsonify
    _l_(702954)

except ImportError:
    pass
try:
    from flask_bcrypt import Bcrypt, check_password_hash
    _l_(702956)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(702958)

except ImportError:
    pass
try:
    import logging
    _l_(702960)

except ImportError:
    pass
try:
    from flask_jwt_extended import create_access_token
    _l_(702962)

except ImportError:
    pass

# registration api #################################################33


@_c_(702965, _a_(702964, _n_(702963, "app", lambda: app), "route"), '/users/register', methods=['POST'])
def register():
    _l_(703042)


    try:
        _l_(703041)

        cur = _c_(702968, _a_(702967, _n_(702966, "conn", lambda: conn), "cursor"))
        _l_(702969)
        first_name = _c_(702972, _a_(702971, _n_(702970, "request", lambda: request), "get_json"))['first_name']
        _l_(702973)
        last_name = _c_(702976, _a_(702975, _n_(702974, "request", lambda: request), "get_json"))['last_name']
        _l_(702977)
        email = _c_(702980, _a_(702979, _n_(702978, "request", lambda: request), "get_json"))['email']
        _l_(702981)
        password = _c_(702989, _a_(702988, _c_(702987, _a_(702983, _n_(702982, "bcrypt", lambda: bcrypt), "generate_password_hash"), _c_(702986, _a_(702985, _n_(702984, "request", lambda: request), "get_json"))['password']), "decode"), 'utf-8')
        _l_(702990)
        created = _c_(702993, _a_(702992, _n_(702991, "datetime", lambda: datetime), "utcnow"))
        _l_(702994)

        _c_(703012, _a_(702996, _n_(702995, "cur", lambda: cur), "execute"), "INSERT INTO admin.admin(first_name,last_name,email,password,created) VALUES('" +
                    _c_(702999, _n_(702997, "str", lambda: str), _n_(702998, "first_name", lambda: first_name)) + "','" +
                    _c_(703002, _n_(703000, "str", lambda: str), _n_(703001, "last_name", lambda: last_name)) + "','" +
                    _c_(703005, _n_(703003, "str", lambda: str), _n_(703004, "email", lambda: email)) + "','" +
                    _c_(703008, _n_(703006, "str", lambda: str), _n_(703007, "password", lambda: password)) + "','" +
                    _c_(703011, _n_(703009, "str", lambda: str), _n_(703010, "created", lambda: created)) + "')")
        _l_(703013)
        _c_(703016, _a_(703015, _n_(703014, "conn", lambda: conn), "commit"))
        _l_(703017)
        result = {
            "first_name": _n_(703018, "first_name", lambda: first_name),
            "last_name": _n_(703019, "last_name", lambda: last_name),
            "email": _n_(703020, "email", lambda: email),
            "password": _n_(703021, "password", lambda: password),
            "created": _n_(703022, "created", lambda: created)
        }
        _l_(703023)
        aux = _c_(703026, _n_(703024, "jsonify", lambda: jsonify), {"result": _n_(703025, "result", lambda: result)})
        _l_(703027)
        return aux
    except _n_(703028, "Exception", lambda: Exception) as e:
        _l_(703040)

        _c_(703031, _a_(703030, _n_(703029, "conn", lambda: conn), "rollback"))
        _l_(703032)
        _c_(703038, _a_(703034, _n_(703033, "logging", lambda: logging), "error"), _c_(703037, _a_(703035, "db error:{}", "format"), _n_(703036, "e", lambda: e)))
        _l_(703039)

##########################LOGIN API#######################################


@_c_(703045, _a_(703044, _n_(703043, "app", lambda: app), "route"), '/users/login', methods=['POST'])
def login():
    _l_(703091)



    cur = _c_(703048, _a_(703047, _n_(703046, "conn", lambda: conn), "cursor"))
    _l_(703049)
    email = _c_(703052, _a_(703051, _n_(703050, "request", lambda: request), "get_json"))['email']
    _l_(703053)
    password = _c_(703056, _a_(703055, _n_(703054, "request", lambda: request), "get_json"))['password']
    _l_(703057)
    result = ""
    _l_(703058)
    _c_(703064, _a_(703060, _n_(703059, "cur", lambda: cur), "execute"), "SELECT * FROM admin.admin WHERE email='" +
                _c_(703063, _n_(703061, "str", lambda: str), _n_(703062, "email", lambda: email)) + "'")
    _l_(703065)
    rv = _c_(703068, _a_(703067, _n_(703066, "cur", lambda: cur), "fetchone"))
    _l_(703069)

    if _c_(703074, _a_(703071, _n_(703070, "bcrypt", lambda: bcrypt), "check_password_hash"), _n_(703072, "rv", lambda: rv)['password'], _n_(703073, "password", lambda: password)):
        _l_(703090)


        access_token = _c_(703079, _n_(703075, "create_access_token", lambda: create_access_token), identity={'first_name': _n_(703076, "rv", lambda: rv)['first_name'], 'last_name': _n_(703077, "rv", lambda: rv)['last_name'], 'email': _n_(703078, "rv", lambda: rv)['email']})
        _l_(703080)
        result = _c_(703083, _n_(703081, "jsonify", lambda: jsonify), {"token": _n_(703082, "access_token", lambda: access_token)})
        _l_(703084)
    else:
        result = _c_(703086, _n_(703085, "jsonify", lambda: jsonify), {"error": "invalid username and password"})
        _l_(703087)
        aux = _n_(703088, "result", lambda: result)
        _l_(703089)
        return aux