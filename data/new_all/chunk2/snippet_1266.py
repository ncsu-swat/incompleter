# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59207486/flask-render-template-not-working-typeerror-nonetype-object-is-not-iterabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(437435, _a_(437434, _n_(437433, "app", lambda: app), "route"), "/login", methods=["GET", "POST"])
def login_route():
    _l_(437536)

    _c_(437437, _n_(437436, "print", lambda: print), "in login route")
    _l_(437438)
    form = _c_(437440, _n_(437439, "LoginForm", lambda: LoginForm))
    _l_(437441)
    if "logged_in" in _n_(437442, "session", lambda: session):
        _l_(437451)

        _c_(437444, _n_(437443, "print", lambda: print), "found in sesstion")
        _l_(437445)
        aux = _c_(437449, _n_(437446, "redirect", lambda: redirect), _c_(437448, _n_(437447, "url_for", lambda: url_for), "index_route"))
        _l_(437450)
        return aux

    if _c_(437454, _a_(437453, _n_(437452, "form", lambda: form), "validate_on_submit")):
        _l_(437528)

        _c_(437456, _n_(437455, "print", lambda: print), "FORM VALID")
        _l_(437457)
        feadback = _c_(437463, _n_(437458, "val_login", lambda: val_login), _a_(437460, _n_(437459, "form", lambda: form), "username"), _a_(437462, _n_(437461, "form", lambda: form), "password"))
        _l_(437464)
        _c_(437467, _n_(437465, "print", lambda: print), _n_(437466, "feadback", lambda: feadback))
        _l_(437468)
        if _n_(437469, "feadback", lambda: feadback)[0] == 1:
            _l_(437527)

            _c_(437471, _n_(437470, "print", lambda: print), "got through if")
            _l_(437472)
            agent = _a_(437475, _a_(437474, _n_(437473, "request", lambda: request), "user_agent"), "string")
            _l_(437476)
            time = _c_(437478, _n_(437477, "get_time", lambda: get_time))
            _l_(437479)
            newHistory = _c_(437486, _n_(437480, "LoginHistory", lambda: LoginHistory), usr_id=_c_(437483, _n_(437481, "int", lambda: int), _n_(437482, "feadback", lambda: feadback)[1]), time=_n_(437484, "time", lambda: time), device_type=_n_(437485, "agent", lambda: agent))
            _l_(437487)
            _c_(437492, _a_(437490, _a_(437489, _n_(437488, "db", lambda: db), "session"), "add"), _n_(437491, "newHistory", lambda: newHistory))
            _l_(437493)
            _c_(437497, _a_(437496, _a_(437495, _n_(437494, "db", lambda: db), "session"), "commit"))
            _l_(437498)
            _n_(437499, "session", lambda: session)["logged_in"] = True
            _l_(437500)
            _c_(437503, _n_(437501, "print", lambda: print), _n_(437502, "session", lambda: session)["logged_in"])
            _l_(437504)
            _n_(437505, "session", lambda: session)["username"] = _n_(437506, "feadback", lambda: feadback)[3]
            _l_(437507)
            _n_(437508, "session", lambda: session)["id"] = _n_(437509, "feadback", lambda: feadback)[1]
            _l_(437510)
            if _n_(437511, "feadback", lambda: feadback)[2]:
                _l_(437514)

                _n_(437512, "session", lambda: session)["admin"] = True
                _l_(437513)
            aux = _c_(437518, _n_(437515, "redirect", lambda: redirect), _c_(437517, _n_(437516, "url_for", lambda: url_for), "index_route"))
            _l_(437519)

            return aux
        else:
            _c_(437521, _n_(437520, "print", lambda: print), "error")
            _l_(437522)
            aux = _c_(437525, _n_(437523, "render_template", lambda: render_template), "login.html", form=_n_(437524, "form", lambda: form), error="true")
            _l_(437526)
            return aux
    _c_(437530, _n_(437529, "print", lambda: print), "at render")
    _l_(437531)
    aux = _c_(437534, _n_(437532, "render_template", lambda: render_template), "login.html", form=_n_(437533, "form", lambda: form))
    _l_(437535)
    return aux