# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71359706/flask-login-attributeerror-str-object-has-no-attribute-is-active
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(634115, _a_(634114, _n_(634113, "admin", lambda: admin), "route"), '/', methods=['GET'])
def index():
    _l_(634123)

    form = _c_(634117, _n_(634116, "admin_login", lambda: admin_login))
    _l_(634118)
    aux = _c_(634121, _n_(634119, "render_template", lambda: render_template), 'login.html', form=_n_(634120, "form", lambda: form))
    _l_(634122)
    return aux

@_c_(634126, _a_(634125, _n_(634124, "admin", lambda: admin), "route"), '/', methods=['POST'])
def index_post():
    _l_(634169)

    form = _c_(634128, _n_(634127, "admin_login", lambda: admin_login))
    _l_(634129)
    user = _a_(634132, _a_(634131, _n_(634130, "form", lambda: form), "name"), "data")
    _l_(634133)
    password = _a_(634136, _a_(634135, _n_(634134, "form", lambda: form), "password"), "data")
    _l_(634137)
    remember = _a_(634140, _a_(634139, _n_(634138, "form", lambda: form), "remember"), "data")
    _l_(634141)
    user_check = _c_(634148, _a_(634147, _c_(634146, _a_(634144, _a_(634143, _n_(634142, "Admin", lambda: Admin), "query"), "filter_by"), username=_n_(634145, "user", lambda: user)), "first"))
    _l_(634149)
    if _n_(634150, "user_check", lambda: user_check):
        _l_(634168)

        password_check = _c_(634155, _n_(634151, "check_password_hash", lambda: check_password_hash), _a_(634153, _n_(634152, "user_check", lambda: user_check), "password"), _n_(634154, "password", lambda: password))
        _l_(634156)
        if _n_(634157, "password_check", lambda: password_check):
            _l_(634167)

            _c_(634160, _n_(634158, "login_user", lambda: login_user), _n_(634159, "user", lambda: user))
            _l_(634161)
            aux = _c_(634165, _n_(634162, "redirect", lambda: redirect), _c_(634164, _n_(634163, "url_for", lambda: url_for), 'admin.search'))
            _l_(634166)
            return aux