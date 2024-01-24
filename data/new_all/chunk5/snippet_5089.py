# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70787649/python3-9-i-am-trying-to-write-an-exception-but-get-this-errortypeerror-catch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Error(_n_(656816, "BaseException", lambda: BaseException)):
    _l_(656818)

    """something"""
    pass
    _l_(656817)

class MailMessage(_n_(656819, "Error", lambda: Error)):
    _l_(656823)

    def __init__(self):
        _l_(656822)

        _n_(656820, "self", lambda: self).connection = None
        _l_(656821)
c = _c_(656825, _n_(656824, "MailMessage", lambda: MailMessage))
_l_(656826)
_c_(656829, _a_(656828, _n_(656827, "c", lambda: c), "set_recs_for_mail_box")) #just for connection
_l_(656830) #just for connection
command_to_db = "SELECT *"
_l_(656831)
try:
    _l_(656843)

    recs = _c_(656837, _a_(656833, _n_(656832, "c", lambda: c), "execute_query"), _a_(656835, _n_(656834, "c", lambda: c), "connection"), _n_(656836, "command_to_db", lambda: command_to_db))
    _l_(656838)
except _c_(656840, _n_(656839, "Error", lambda: Error)):
    _l_(656842)

    pass
    _l_(656841)