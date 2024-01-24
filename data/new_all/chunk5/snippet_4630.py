# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53951162/flask-login-typeerror-object-supporting-the-buffer-api-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(659036, _a_(659035, _n_(659034, "app", lambda: app), "route"), '/register', methods=['POST', 'GET'])
def register():
    _l_(659083)

    form = _c_(659038, _n_(659037, "RegisterForm", lambda: RegisterForm))
    _l_(659039)

    if _c_(659042, _a_(659041, _n_(659040, "form", lambda: form), "validate_on_submit")):
        _l_(659078)

        hashed_password = _c_(659047, _n_(659043, "generate_password_hash", lambda: generate_password_hash), _a_(659046, _a_(659045, _n_(659044, "form", lambda: form), "password"), "data"), method='sha256')
        _l_(659048)
        new_user = _c_(659057, _n_(659049, "User", lambda: User), username=_a_(659052, _a_(659051, _n_(659050, "form", lambda: form), "username"), "data"), password=_n_(659053, "hashed_password", lambda: hashed_password), email=_a_(659056, _a_(659055, _n_(659054, "form", lambda: form), "email"), "data"))
        _l_(659058)
        _c_(659061, _a_(659060, _n_(659059, "db", lambda: db), "create_all"))
        _l_(659062)
        _c_(659067, _a_(659065, _a_(659064, _n_(659063, "db", lambda: db), "session"), "add"), _n_(659066, "new_user", lambda: new_user))
        _l_(659068)
        _c_(659072, _a_(659071, _a_(659070, _n_(659069, "db", lambda: db), "session"), "commit"))
        _l_(659073)
        aux = _c_(659076, _n_(659074, "render_template", lambda: render_template), 'register_ok.html', form=_n_(659075, "form", lambda: form))
        _l_(659077)
        return aux
    aux = _c_(659081, _n_(659079, "render_template", lambda: render_template), 'register.html', form=_n_(659080, "form", lambda: form))
    _l_(659082)
    return aux