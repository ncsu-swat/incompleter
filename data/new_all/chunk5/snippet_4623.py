# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(691678, _a_(691677, _n_(691676, "app", lambda: app), "route"), '/login', methods=['POST', 'GET'])
def login():
    _l_(691724)

    form = _c_(691680, _n_(691679, "LoginForm", lambda: LoginForm))
    _l_(691681)

    if _c_(691684, _a_(691683, _n_(691682, "form", lambda: form), "validate_on_submit")):
        _l_(691719)

        user = _c_(691693, _a_(691692, _c_(691691, _a_(691687, _a_(691686, _n_(691685, "User", lambda: User), "query"), "filter_by"), username=_a_(691690, _a_(691689, _n_(691688, "form", lambda: form), "username"), "data")), "first"))
        _l_(691694)
        if _n_(691695, "user", lambda: user):
            _l_(691718)

            if _c_(691701, _n_(691696, "check_password_hash", lambda: check_password_hash), _a_(691698, _n_(691697, "user", lambda: user), "password"), _a_(691700, _n_(691699, "form", lambda: form), "password")):
                _l_(691714)

                _c_(691707, _n_(691702, "login_user", lambda: login_user), _n_(691703, "user", lambda: user), remember=_a_(691706, _a_(691705, _n_(691704, "form", lambda: form), "remember"), "data"))
                _l_(691708)
                aux = _c_(691712, _n_(691709, "redirect", lambda: redirect), _c_(691711, _n_(691710, "url_for", lambda: url_for), 'dashboard'))
                _l_(691713)
                return aux
            aux = _c_(691716, _n_(691715, "render_template", lambda: render_template), 'err_login.html')
            _l_(691717)
            return aux
    aux = _c_(691722, _n_(691720, "render_template", lambda: render_template), 'login.html', form=_n_(691721, "form", lambda: form))
    _l_(691723)
    return aux