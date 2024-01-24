# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65881511/odoo-12-getting-typeerror-on-while-trying-to-access-models-record-from-record
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import odoo.http as http
    _l_(547643)

except ImportError:
    pass
try:
    from odoo import SUPERUSER_ID
    _l_(547645)

except ImportError:
    pass
try:
    from odoo import registry as registry_get
    _l_(547647)

except ImportError:
    pass
try:
    from odoo.api import Environment
    _l_(547649)

except ImportError:
    pass
try:
    import json
    _l_(547651)

except ImportError:
    pass


class Controller(_a_(547653, _n_(547652, "http", lambda: http), "Controller")):
    _l_(547678)


    @_c_(547656, _a_(547655, _n_(547654, "http", lambda: http), "route"), '/test', type='http', auth='public', website=False)
    def handler(self):
        _l_(547677)

        registry = _c_(547658, _n_(547657, "registry_get", lambda: registry_get), 'ceres')
        _l_(547659)
        with _c_(547662, _a_(547661, _n_(547660, "registry", lambda: registry), "cursor")) as cr:
            _l_(547674)

            env = _c_(547666, _n_(547663, "Environment", lambda: Environment), _n_(547664, "cr", lambda: cr), _n_(547665, "SUPERUSER_ID", lambda: SUPERUSER_ID), {})
            _l_(547667)
            attendee = _c_(547672, _a_(547671, _c_(547670, _a_(547669, _n_(547668, "env", lambda: env)['product.template'], "sudo")), "search"), [])
            _l_(547673)
        aux = _n_(547675, "attendee", lambda: attendee) 
        _l_(547676) 
        return aux 