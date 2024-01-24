# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56242706/flask-bcrypt-check-password-method-always-return-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(541109, _a_(541108, _n_(541107, "app", lambda: app), "route"), '/login' , methods=['POST', 'GET'])
def login():
    _l_(541167)

    form = _c_(541111, _n_(541110, "login_form", lambda: login_form))# imported from forms.py file as a class
    _l_(541112)# imported from forms.py file as a class
    email = _a_(541115, _a_(541114, _n_(541113, "form", lambda: form), "email"), "data")
    _l_(541116)
    if _c_(541119, _a_(541118, _n_(541117, "form", lambda: form), "validate_on_submit")):
        _l_(541162)

        _c_(541123, _a_(541121, _n_(541120, "cur", lambda: cur), "execute"), "SELECT email FROM users WHERE email =%s", [_n_(541122, "email", lambda: email)])
        _l_(541124)
        user_email = _c_(541127, _a_(541126, _n_(541125, "cur", lambda: cur), "fetchone"))
        _l_(541128)
        _c_(541132, _a_(541130, _n_(541129, "cur", lambda: cur), "execute"), "SELECT password FROM users WHERE email =%s",[_n_(541131, "email", lambda: email)])
        _l_(541133)
        hashed_password = _c_(541136, _a_(541135, _n_(541134, "cur", lambda: cur), "fetchone"))
        _l_(541137)
        if _n_(541138, "user_email", lambda: user_email) and _c_(541145, _a_(541140, _n_(541139, "bcrypt", lambda: bcrypt), "check_password_hash"), _n_(541141, "hashed_password", lambda: hashed_password),_a_(541144, _a_(541143, _n_(541142, "form", lambda: form), "password"), "data")) :
            _l_(541161)

            _c_(541151, _n_(541146, "login_user", lambda: login_user), _n_(541147, "user_email", lambda: user_email),remember=_a_(541150, _a_(541149, _n_(541148, "form", lambda: form), "remember"), "data"))
            _l_(541152)
            aux = _c_(541156, _n_(541153, "redirect", lambda: redirect), _c_(541155, _n_(541154, "url_for", lambda: url_for), 'home'))
            _l_(541157)
            return aux
        else :
            _c_(541159, _n_(541158, "flash", lambda: flash), 'Unable to log in , please check your email and password', 'danger')
            _l_(541160)
    aux = _c_(541165, _n_(541163, "render_template", lambda: render_template), 'login.html' , title='login' , form= _n_(541164, "form", lambda: form))
    _l_(541166)

    return aux