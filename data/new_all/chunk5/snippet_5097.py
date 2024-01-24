# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70787649/python3-9-i-am-trying-to-write-an-exception-but-get-this-errortypeerror-catch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MailMessage(_n_(668167, "BaseException", lambda: BaseException)):
    _l_(668171)

    def __init__(self):
        _l_(668170)

        _n_(668168, "self", lambda: self).connection = None
        _l_(668169)
c = _c_(668173, _n_(668172, "MailMessage", lambda: MailMessage))
_l_(668174)
_c_(668177, _a_(668176, _n_(668175, "c", lambda: c), "set_recs_for_mail_box")) #just for connection
_l_(668178) #just for connection
command_to_db = "SELECT *"
_l_(668179)
try:
    _l_(668191)

    recs = _c_(668185, _a_(668181, _n_(668180, "c", lambda: c), "execute_query"), _a_(668183, _n_(668182, "c", lambda: c), "connection"), _n_(668184, "command_to_db", lambda: command_to_db))
    _l_(668186)
except _c_(668188, _n_(668187, "SyntaxError", lambda: SyntaxError)):
    _l_(668190)

    pass
    _l_(668189)