# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75028036/flask-attributeerror-mysql-object-has-no-attribute-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(354576)

except ImportError:
    pass
try:
    from application import app
    _l_(354578)

except ImportError:
    pass
try:
    from application import mysql
    _l_(354580)

except ImportError:
    pass
try:
    from flask import render_template, request, Response
    _l_(354582)

except ImportError:
    pass
try:
    from application.models import User, Course, Enrollment
    _l_(354584)

except ImportError:
    pass

@_c_(354587, _a_(354586, _n_(354585, "app", lambda: app), "route"), "/user")
def user():
    _l_(354619)

    conn = _c_(354590, _a_(354589, _n_(354588, "mysql", lambda: mysql), "connect"))
    _l_(354591)
    cursor = _c_(354594, _a_(354593, _n_(354592, "conn", lambda: conn), "cursor"))
    _l_(354595)

    _c_(354598, _a_(354597, _n_(354596, "cursor", lambda: cursor), "execute"), '''SHOW SCHEMAS;''')
    _l_(354599)
    rv = _c_(354602, _a_(354601, _n_(354600, "cursor", lambda: cursor), "fetchall"))
    _l_(354603)

    _c_(354605, _n_(354604, "User", lambda: User), user_id=1, first_name="John", last_name="Doh", email="jd@domain.com", password="abc123")
    _l_(354606)
    _c_(354608, _n_(354607, "User", lambda: User), user_id=2, first_name="Jane", last_name="Doh", email="jad@domain.com", password="abc123")
    _l_(354609)

    users = _c_(354613, _a_(354612, _a_(354611, _n_(354610, "User", lambda: User), "objects"), "all"))
    _l_(354614)
    aux = _c_(354617, _n_(354615, "render_template", lambda: render_template), "user.html", users=_n_(354616, "users", lambda: users))
    _l_(354618)

    return aux