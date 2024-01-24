# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849950/typeerror-tuple-indices-must-be-integers-or-slices-not-str-python-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from app import app, conn, bcrypt
    _l_(647629)

except ImportError:
    pass
try:
    from flask import request, jsonify
    _l_(647631)

except ImportError:
    pass
try:
    from flask_bcrypt import Bcrypt, check_password_hash
    _l_(647633)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(647635)

except ImportError:
    pass
try:
    import logging
    _l_(647637)

except ImportError:
    pass
try:
    from flask_jwt_extended import create_access_token
    _l_(647639)

except ImportError:
    pass

# registration api #################################################33


@_c_(647642, _a_(647641, _n_(647640, "app", lambda: app), "route"), '/users/register', methods=['POST'])
def register():
    _l_(647719)


    try:
        _l_(647718)

        cur = _c_(647645, _a_(647644, _n_(647643, "conn", lambda: conn), "cursor"))
        _l_(647646)
        first_name = _c_(647649, _a_(647648, _n_(647647, "request", lambda: request), "get_json"))['first_name']
        _l_(647650)
        last_name = _c_(647653, _a_(647652, _n_(647651, "request", lambda: request), "get_json"))['last_name']
        _l_(647654)
        email = _c_(647657, _a_(647656, _n_(647655, "request", lambda: request), "get_json"))['email']
        _l_(647658)
        password = _c_(647666, _a_(647665, _c_(647664, _a_(647660, _n_(647659, "bcrypt", lambda: bcrypt), "generate_password_hash"), _c_(647663, _a_(647662, _n_(647661, "request", lambda: request), "get_json"))['password']), "decode"), 'utf-8')
        _l_(647667)
        created = _c_(647670, _a_(647669, _n_(647668, "datetime", lambda: datetime), "utcnow"))
        _l_(647671)

        _c_(647689, _a_(647673, _n_(647672, "cur", lambda: cur), "execute"), "INSERT INTO admin.admin(first_name,last_name,email,password,created) VALUES('" +
                    _c_(647676, _n_(647674, "str", lambda: str), _n_(647675, "first_name", lambda: first_name)) + "','" +
                    _c_(647679, _n_(647677, "str", lambda: str), _n_(647678, "last_name", lambda: last_name)) + "','" +
                    _c_(647682, _n_(647680, "str", lambda: str), _n_(647681, "email", lambda: email)) + "','" +
                    _c_(647685, _n_(647683, "str", lambda: str), _n_(647684, "password", lambda: password)) + "','" +
                    _c_(647688, _n_(647686, "str", lambda: str), _n_(647687, "created", lambda: created)) + "')")
        _l_(647690)
        _c_(647693, _a_(647692, _n_(647691, "conn", lambda: conn), "commit"))
        _l_(647694)
        result = {
            "first_name": _n_(647695, "first_name", lambda: first_name),
            "last_name": _n_(647696, "last_name", lambda: last_name),
            "email": _n_(647697, "email", lambda: email),
            "password": _n_(647698, "password", lambda: password),
            "created": _n_(647699, "created", lambda: created)
        }
        _l_(647700)
        aux = _c_(647703, _n_(647701, "jsonify", lambda: jsonify), {"result": _n_(647702, "result", lambda: result)})
        _l_(647704)
        return aux
    except _n_(647705, "Exception", lambda: Exception) as e:
        _l_(647717)

        _c_(647708, _a_(647707, _n_(647706, "conn", lambda: conn), "rollback"))
        _l_(647709)
        _c_(647715, _a_(647711, _n_(647710, "logging", lambda: logging), "error"), _c_(647714, _a_(647712, "db error:{}", "format"), _n_(647713, "e", lambda: e)))
        _l_(647716)

##########################LOGIN API#######################################


@_c_(647722, _a_(647721, _n_(647720, "app", lambda: app), "route"), '/users/login', methods=['POST'])
def login():
    _l_(647768)



    cur = _c_(647725, _a_(647724, _n_(647723, "conn", lambda: conn), "cursor"))
    _l_(647726)
    email = _c_(647729, _a_(647728, _n_(647727, "request", lambda: request), "get_json"))['email']
    _l_(647730)
    password = _c_(647733, _a_(647732, _n_(647731, "request", lambda: request), "get_json"))['password']
    _l_(647734)
    result = ""
    _l_(647735)
    _c_(647741, _a_(647737, _n_(647736, "cur", lambda: cur), "execute"), "SELECT * FROM admin.admin WHERE email='" +
                _c_(647740, _n_(647738, "str", lambda: str), _n_(647739, "email", lambda: email)) + "'")
    _l_(647742)
    rv = _c_(647745, _a_(647744, _n_(647743, "cur", lambda: cur), "fetchone"))
    _l_(647746)

    if _c_(647751, _a_(647748, _n_(647747, "bcrypt", lambda: bcrypt), "check_password_hash"), _n_(647749, "rv", lambda: rv)['password'], _n_(647750, "password", lambda: password)):
        _l_(647767)


        access_token = _c_(647756, _n_(647752, "create_access_token", lambda: create_access_token), identity={'first_name': _n_(647753, "rv", lambda: rv)['first_name'], 'last_name': _n_(647754, "rv", lambda: rv)['last_name'], 'email': _n_(647755, "rv", lambda: rv)['email']})
        _l_(647757)
        result = _c_(647760, _n_(647758, "jsonify", lambda: jsonify), {"token": _n_(647759, "access_token", lambda: access_token)})
        _l_(647761)
    else:
        result = _c_(647763, _n_(647762, "jsonify", lambda: jsonify), {"error": "invalid username and password"})
        _l_(647764)
        aux = _n_(647765, "result", lambda: result)
        _l_(647766)
        return aux