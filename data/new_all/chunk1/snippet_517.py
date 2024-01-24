# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60106043/odoo-12-attributeerror-int-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
student_id = _c_(401034, _a_(401030, _n_(401029, "fields", lambda: fields), "Many2one"), 'res.users', 'Etudiant', readonly=True, required=True, default=lambda self: _c_(401033, _a_(401032, _n_(401031, "self", lambda: self), "choice_student"))  )
_l_(401035)

@_c_(401038, _a_(401037, _n_(401036, "api", lambda: api), "onchange"), 'projet_terminer_id')
def choice_student(self):
    _l_(401047)

    aux = _a_(401045, _c_(401044, _a_(401043, _c_(401042, _a_(401041, _a_(401040, _n_(401039, "self", lambda: self), "env")['res.users'], "sudo")), "search"), [ ('id','=', 45)]), "id")
    _l_(401046)
    return aux