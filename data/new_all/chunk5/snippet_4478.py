# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56903546/how-to-resolve-error-typeerror-strptime-argument-1-must-be-str-not-bool
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AttendanceModificationRequest(_a_(653388, _n_(653387, "models", lambda: models), "Model")):
    _l_(653507)


    _name = 'attendance.modification.request'
    _l_(653389)
    _description = 'Attendance modification Request'
    _l_(653390)
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _l_(653391)

    def _get_employee_id(self):
        _l_(653403)

        employee_rec = _c_(653398, _a_(653394, _a_(653393, _n_(653392, "self", lambda: self), "env")['hr.employee'], "search"), [('user_id', '=',
                _a_(653397, _a_(653396, _n_(653395, "self", lambda: self), "env"), "uid"))], limit=1)
        _l_(653399)
        aux = _a_(653401, _n_(653400, "employee_rec", lambda: employee_rec), "id")
        _l_(653402)
        return aux

    employee_id = _c_(653405, _a_(653404, fields, "Many2one"), 'hr.employee', 'Employee',
                                  readonly=True,
                                  default=_get_employee_id,
                                  required=True)
    _l_(653406)
    user_id = _c_(653411, _a_(653407, fields, "Many2one"), 'res.users',
        string='User',
        track_visibility='onchange',
        readonly=True,
        states={'draft': [('readonly', False)]},
        default=lambda self: _a_(653410, _a_(653409, _n_(653408, "self", lambda: self), "env"), "user"),
        )
    _l_(653412)
    state = _c_(653414, _a_(653413, fields, "Selection"), [('draft', 'Pending'), ('waiting',
                             'Waiting for approval'), ('approved',
                             'Approved'), ('cancel', 'Cancelled')],
                             readonly=True,
                             help='Gives the state of the attendance request modification .'
                             , default='draft')
    _l_(653415)
    modification_date = _c_(653417, _a_(653416, fields, "Date"), 'Date')
    _l_(653418)
    time_check_in_1 = _c_(653420, _a_(653419, fields, "Datetime"), 'Check in')
    _l_(653421)
    time_check_out_1 = _c_(653423, _a_(653422, fields, "Datetime"), 'Check out')
    _l_(653424)
    note = _c_(653426, _a_(653425, fields, "Text"), 'Note')
    _l_(653427)
    attendance_id = _c_(653429, _a_(653428, fields, "Many2one"), 'hr.attendance', string='Attendance'
                                    )
    _l_(653430)

    @_a_(653431, api, "multi")
    def modification_approval(self):
        _l_(653506)

        attend_signin_ids = _c_(653438, _a_(653434, _a_(653433, _n_(653432, "self", lambda: self), "env")['hr.attendance'
                ], "search"), [('employee_id', '=', _a_(653437, _a_(653436, _n_(653435, "self", lambda: self), "employee_id"), "id"))])
        _l_(653439)
        check_in_date = \
            _c_(653448, _a_(653447, _c_(653446, _a_(653442, _a_(653441, _n_(653440, "datetime", lambda: datetime), "datetime"), "strptime"), _a_(653444, _n_(653443, "self", lambda: self), "time_check_in_1"),
                _n_(653445, "DEFAULT_SERVER_DATETIME_FORMAT", lambda: DEFAULT_SERVER_DATETIME_FORMAT)), "date"))
        _l_(653449)
        check_out_date = \
            _c_(653458, _a_(653457, _c_(653456, _a_(653452, _a_(653451, _n_(653450, "datetime", lambda: datetime), "datetime"), "strptime"), _a_(653454, _n_(653453, "self", lambda: self), "time_check_out_1"),
                _n_(653455, "DEFAULT_SERVER_DATETIME_FORMAT", lambda: DEFAULT_SERVER_DATETIME_FORMAT)), "date"))
        _l_(653459)
        for record in _n_(653460, "self", lambda: self):
            _l_(653501)

            attendance_check_in_date = \
                _c_(653470, _a_(653469, _c_(653468, _a_(653463, _a_(653462, _n_(653461, "datetime", lambda: datetime), "datetime"), "strptime"), _a_(653466, _a_(653465, _n_(653464, "record", lambda: record), "attendance_id"), "check_in"),
                    _n_(653467, "DEFAULT_SERVER_DATETIME_FORMAT", lambda: DEFAULT_SERVER_DATETIME_FORMAT)), "date"))
            _l_(653471)
            attendance_check_out_date = \
                _c_(653481, _a_(653480, _c_(653479, _a_(653474, _a_(653473, _n_(653472, "datetime", lambda: datetime), "datetime"), "strptime"), _a_(653477, _a_(653476, _n_(653475, "record", lambda: record), "attendance_id"), "check_out"),
                    _n_(653478, "DEFAULT_SERVER_DATETIME_FORMAT", lambda: DEFAULT_SERVER_DATETIME_FORMAT)), "date"))
            _l_(653482)
            if _a_(653485, _a_(653484, _n_(653483, "record", lambda: record), "attendance_id"), "employee_id") == _a_(653487, _n_(653486, "self", lambda: self), "employee_id") \
                and _n_(653488, "check_in_date", lambda: check_in_date) == _n_(653489, "attendance_check_in_date", lambda: attendance_check_in_date):
                _l_(653500)

                _a_(653491, _n_(653490, "record", lambda: record), "attendance_id").check_in = _a_(653493, _n_(653492, "self", lambda: self), "time_check_in_1")
                _l_(653494)
                _a_(653496, _n_(653495, "record", lambda: record), "attendance_id").check_out = _a_(653498, _n_(653497, "self", lambda: self), "time_check_out_1")
                _l_(653499)
        aux = _c_(653504, _a_(653503, _n_(653502, "self", lambda: self), "write"), {'state': 'approved'})
        _l_(653505)
        return aux