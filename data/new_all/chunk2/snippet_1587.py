# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74582002/attribute-error-when-working-with-self-and-with
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(473069, "self", lambda: self).doc = _c_(473071, _n_(473070, "Document", lambda: Document))
_l_(473072)
_a_(473074, _n_(473073, "self", lambda: self), "doc").documentclass = _c_(473076, _n_(473075, "Command", lambda: Command), 'documentclass',
    options=['12pt'],
    arguments=['article']
    )
_l_(473077)
# Set up preamble (cannot share code)
_n_(473078, "self", lambda: self).overview_table = _c_(473084, _a_(473081, _a_(473080, _n_(473079, "self", lambda: self), "doc"), "create"), _c_(473083, _n_(473082, "LongTable", lambda: LongTable), "| l | l | l |")) 
_l_(473085) 