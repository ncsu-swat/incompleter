# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65853626/odoo-uncaught-typeerror-cannot-read-property-string-of-undefined-settings-vie
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TicketSettings(_a_(524515, _n_(524514, "models", lambda: models), "TransientModel")):
    _l_(524583)

    _inherit = 'res.config.settings'
    _l_(524516)

    template_id = _c_(524518, _a_(524517, fields, "Many2one"), 'mail.template', string='Mail template')
    _l_(524519)
    days = _c_(524521, _a_(524520, fields, "Integer"), 'Days')
    _l_(524522)

    def set_values(self):
        _l_(524547)

        _c_(524527, _a_(524526, _n_(524523, "super", lambda: super)(_n_(524524, "TicketSettings", lambda: TicketSettings), _n_(524525, "self", lambda: self)), "set_values"))
        _l_(524528)
        settings = _c_(524532, _a_(524531, _a_(524530, _n_(524529, "self", lambda: self), "env")['ir.config_parameter'], "sudo"))
        _l_(524533)
        _c_(524539, _a_(524535, _n_(524534, "settings", lambda: settings), "set_param"), 'base.template_id', _a_(524538, _a_(524537, _n_(524536, "self", lambda: self), "template_id"), "id"))
        _l_(524540)
        _c_(524545, _a_(524542, _n_(524541, "settings", lambda: settings), "set_param"), 'base.days', _a_(524544, _n_(524543, "self", lambda: self), "days"))
        _l_(524546)

    @_a_(524548, api, "model")
    def get_values(self):
        _l_(524582)

        res = _c_(524553, _a_(524552, _n_(524549, "super", lambda: super)(_n_(524550, "TicketSettings", lambda: TicketSettings), _n_(524551, "self", lambda: self)), "get_values"))
        _l_(524554)
        settings = _c_(524558, _a_(524557, _a_(524556, _n_(524555, "self", lambda: self), "env")['ir.config_parameter'], "sudo"))
        _l_(524559)
        template_id = _c_(524562, _a_(524561, _n_(524560, "settings", lambda: settings), "get_param"), 'base.template_id')
        _l_(524563)
        days = _c_(524566, _a_(524565, _n_(524564, "settings", lambda: settings), "get_param"), 'base.days')
        _l_(524567)
        _c_(524578, _a_(524569, _n_(524568, "res", lambda: res), "update"), template_id = _c_(524572, _n_(524570, "literal_eval", lambda: literal_eval), _n_(524571, "template_id", lambda: template_id)) if _n_(524573, "template_id", lambda: template_id) else None,
            hours = _c_(524576, _n_(524574, "literal_eval", lambda: literal_eval), _n_(524575, "days", lambda: days)) if _n_(524577, "days", lambda: days) else None)
        _l_(524579)
        aux = _n_(524580, "res", lambda: res)
        _l_(524581)
        return aux