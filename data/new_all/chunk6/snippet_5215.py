# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59291245/flask-login-attributeerror-int-object-has-no-attribute-is-authenticated
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(364390, _a_(364389, _n_(364388, "app", lambda: app), "route"), '/device_detail', methods=['GET', 'POST'])
@_n_(364391, "login_required", lambda: login_required)
def device_detail_operation():
    _l_(364397)

    error = None
    _l_(364392)
    aux = _c_(364395, _n_(364393, "render_template", lambda: render_template), 'device_detail.html', error=_n_(364394, "error", lambda: error))
    _l_(364396)
    return aux