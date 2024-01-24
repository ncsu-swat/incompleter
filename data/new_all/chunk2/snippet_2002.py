# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71016869/attributeerror-ir-ui-menu-object-has-no-attribute-report-action-when-genera
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from odoo import models, fields
    _l_(472646)

except ImportError:
    pass

class hotelreport(_a_(472648, _n_(472647, "models", lambda: models), "TransientModel")):
    _l_(472680)

    _name = 'hotel.report.wizard'
    _l_(472649)

    employee = _c_(472652, _a_(472651, _n_(472650, "fields", lambda: fields), "Many2one"), 'res.users', string="Employee")
    _l_(472653)
    from_date = _c_(472656, _a_(472655, _n_(472654, "fields", lambda: fields), "Date"), string="Starting Date")
    _l_(472657)
    to_date = _c_(472660, _a_(472659, _n_(472658, "fields", lambda: fields), "Date"), string="Ending Date")
    _l_(472661)

    def action_print_report(self):
        _l_(472679)

        data = {
            'start_date': _a_(472663, _n_(472662, "self", lambda: self), "from_date"),
            'end_date': _a_(472665, _n_(472664, "self", lambda: self), "to_date"),
            'employee': _a_(472668, _a_(472667, _n_(472666, "self", lambda: self), "employee"), "id")
        }
        _l_(472669)
        aux = _c_(472677, _a_(472674, _c_(472673, _a_(472672, _a_(472671, _n_(472670, "self", lambda: self), "env"), "ref"), 'hotel_promo.print_report'), "report_action"), _n_(472675, "self", lambda: self), data=_n_(472676, "data", lambda: data))
        _l_(472678)
        return aux