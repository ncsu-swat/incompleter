# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70787649/python3-9-i-am-trying-to-write-an-exception-but-get-this-errortypeerror-catch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MailMessage(_n_(684343, "BaseException", lambda: BaseException)):
    _l_(684347)

    def __init__(self):
        _l_(684346)

        _n_(684344, "self", lambda: self).connection = None
        _l_(684345)
c = _c_(684349, _n_(684348, "MailMessage", lambda: MailMessage))
_l_(684350)
_c_(684353, _a_(684352, _n_(684351, "c", lambda: c), "set_recs_for_mail_box")) #just for connection
_l_(684354) #just for connection
command_to_db = "SELECT *"
_l_(684355)
try:
    _l_(684367)

    recs = _c_(684361, _a_(684357, _n_(684356, "c", lambda: c), "execute_query"), _a_(684359, _n_(684358, "c", lambda: c), "connection"), _n_(684360, "command_to_db", lambda: command_to_db))
    _l_(684362)
except _c_(684364, _n_(684363, "SyntaxError", lambda: SyntaxError)):
    _l_(684366)

    pass
    _l_(684365)