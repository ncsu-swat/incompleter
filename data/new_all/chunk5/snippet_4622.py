# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(687392, _a_(687391, _n_(687390, "app", lambda: app), "route"), '/register', methods=['POST', 'GET'])
def register():
    _l_(687439)

    form = _c_(687394, _n_(687393, "RegisterForm", lambda: RegisterForm))
    _l_(687395)

    if _c_(687398, _a_(687397, _n_(687396, "form", lambda: form), "validate_on_submit")):
        _l_(687434)

        hashed_password = _c_(687403, _n_(687399, "generate_password_hash", lambda: generate_password_hash), _a_(687402, _a_(687401, _n_(687400, "form", lambda: form), "password"), "data"), method='sha256')
        _l_(687404)
        new_user = _c_(687413, _n_(687405, "User", lambda: User), username=_a_(687408, _a_(687407, _n_(687406, "form", lambda: form), "username"), "data"), password=_n_(687409, "hashed_password", lambda: hashed_password), email=_a_(687412, _a_(687411, _n_(687410, "form", lambda: form), "email"), "data"))
        _l_(687414)
        _c_(687417, _a_(687416, _n_(687415, "db", lambda: db), "create_all"))
        _l_(687418)
        _c_(687423, _a_(687421, _a_(687420, _n_(687419, "db", lambda: db), "session"), "add"), _n_(687422, "new_user", lambda: new_user))
        _l_(687424)
        _c_(687428, _a_(687427, _a_(687426, _n_(687425, "db", lambda: db), "session"), "commit"))
        _l_(687429)
        aux = _c_(687432, _n_(687430, "render_template", lambda: render_template), 'register_ok.html', form=_n_(687431, "form", lambda: form))
        _l_(687433)
        return aux
    aux = _c_(687437, _n_(687435, "render_template", lambda: render_template), 'register.html', form=_n_(687436, "form", lambda: form))
    _l_(687438)
    return aux