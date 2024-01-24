# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(673392, _a_(673391, _n_(673390, "app", lambda: app), "route"), '/login', methods=['POST', 'GET'])
def login():
    _l_(673438)

    form = _c_(673394, _n_(673393, "LoginForm", lambda: LoginForm))
    _l_(673395)

    if _c_(673398, _a_(673397, _n_(673396, "form", lambda: form), "validate_on_submit")):
        _l_(673433)

        user = _c_(673407, _a_(673406, _c_(673405, _a_(673401, _a_(673400, _n_(673399, "User", lambda: User), "query"), "filter_by"), username=_a_(673404, _a_(673403, _n_(673402, "form", lambda: form), "username"), "data")), "first"))
        _l_(673408)
        if _n_(673409, "user", lambda: user):
            _l_(673432)

            if _c_(673415, _n_(673410, "check_password_hash", lambda: check_password_hash), _a_(673412, _n_(673411, "user", lambda: user), "password"), _a_(673414, _n_(673413, "form", lambda: form), "password")):
                _l_(673428)

                _c_(673421, _n_(673416, "login_user", lambda: login_user), _n_(673417, "user", lambda: user), remember=_a_(673420, _a_(673419, _n_(673418, "form", lambda: form), "remember"), "data"))
                _l_(673422)
                aux = _c_(673426, _n_(673423, "redirect", lambda: redirect), _c_(673425, _n_(673424, "url_for", lambda: url_for), 'dashboard'))
                _l_(673427)
                return aux
            aux = _c_(673430, _n_(673429, "render_template", lambda: render_template), 'err_login.html')
            _l_(673431)
            return aux
    aux = _c_(673436, _n_(673434, "render_template", lambda: render_template), 'login.html', form=_n_(673435, "form", lambda: form))
    _l_(673437)
    return aux