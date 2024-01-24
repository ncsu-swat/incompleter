# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65853626/odoo-uncaught-typeerror-cannot-read-property-string-of-undefined-settings-vie
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TicketSettings(_a_(529663, _n_(529662, "models", lambda: models), "TransientModel")):
    _l_(529731)

    _inherit = 'res.config.settings'
    _l_(529664)

    template_id = _c_(529666, _a_(529665, fields, "Many2one"), 'mail.template', string='Mail template')
    _l_(529667)
    hours = _c_(529669, _a_(529668, fields, "Integer"), 'hours')
    _l_(529670)

    def set_values(self):
        _l_(529695)

        _c_(529675, _a_(529674, _n_(529671, "super", lambda: super)(_n_(529672, "TicketSettings", lambda: TicketSettings), _n_(529673, "self", lambda: self)), "set_values"))
        _l_(529676)
        settings = _c_(529680, _a_(529679, _a_(529678, _n_(529677, "self", lambda: self), "env")['ir.config_parameter'], "sudo"))
        _l_(529681)
        _c_(529687, _a_(529683, _n_(529682, "settings", lambda: settings), "set_param"), 'base.template_id', _a_(529686, _a_(529685, _n_(529684, "self", lambda: self), "template_id"), "id"))
        _l_(529688)
        _c_(529693, _a_(529690, _n_(529689, "settings", lambda: settings), "set_param"), 'base.hours', _a_(529692, _n_(529691, "self", lambda: self), "hours"))
        _l_(529694)

    @_a_(529696, api, "model")
    def get_values(self):
        _l_(529730)

        res = _c_(529701, _a_(529700, _n_(529697, "super", lambda: super)(_n_(529698, "TicketSettings", lambda: TicketSettings), _n_(529699, "self", lambda: self)), "get_values"))
        _l_(529702)
        settings = _c_(529706, _a_(529705, _a_(529704, _n_(529703, "self", lambda: self), "env")['ir.config_parameter'], "sudo"))
        _l_(529707)
        template_id = _c_(529710, _a_(529709, _n_(529708, "settings", lambda: settings), "get_param"), 'base.template_id')
        _l_(529711)
        hours = _c_(529714, _a_(529713, _n_(529712, "settings", lambda: settings), "get_param"), 'base.hours')
        _l_(529715)
        _c_(529726, _a_(529717, _n_(529716, "res", lambda: res), "update"), template_id = _c_(529720, _n_(529718, "literal_eval", lambda: literal_eval), _n_(529719, "template_id", lambda: template_id)) if _n_(529721, "template_id", lambda: template_id) else None,
            hours = _c_(529724, _n_(529722, "literal_eval", lambda: literal_eval), _n_(529723, "hours", lambda: hours)) if _n_(529725, "hours", lambda: hours) else None)
        _l_(529727)
        aux = _n_(529728, "res", lambda: res)
        _l_(529729)
        return aux