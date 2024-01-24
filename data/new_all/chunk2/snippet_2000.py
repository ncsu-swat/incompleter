# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71184884/attributeerror-str-object-has-no-attribute-get-odoo14
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from odoo import fields, models, api
    _l_(428187)

except ImportError:
    pass

class  CreateExam(_a_(428189, _n_(428188, "models", lambda: models), "TransientModel")):
    _l_(428209)

    _name = 'exam.wizards'
    _l_(428190)
    _description = 'Create exams'
    _l_(428191)

    std_wiz = _c_(428194, _a_(428193, _n_(428192, "fields", lambda: fields), "Many2one"), comodel_name='std.record',
        string='Student',
        required=False)
    _l_(428195)
    std_subject = _c_(428198, _a_(428197, _n_(428196, "fields", lambda: fields), "Many2one"), 'std.subject',string="Subject")
    _l_(428199)
    std_marks=_c_(428202, _a_(428201, _n_(428200, "fields", lambda: fields), "Float"), string="Marks")
    _l_(428203)

    def save_btn(self):
        _l_(428208)

        _c_(428205, _n_(428204, "print", lambda: print), "saved")
        _l_(428206)
        aux = True
        _l_(428207)
        return aux