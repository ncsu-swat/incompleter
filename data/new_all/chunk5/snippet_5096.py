# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70787649/python3-9-i-am-trying-to-write-an-exception-but-get-this-errortypeerror-catch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Error(_n_(663330, "BaseException", lambda: BaseException)):
    _l_(663332)

    """something"""
    pass
    _l_(663331)

class MailMessage(_n_(663333, "Error", lambda: Error)):
    _l_(663337)

    def __init__(self):
        _l_(663336)

        _n_(663334, "self", lambda: self).connection = None
        _l_(663335)
c = _c_(663339, _n_(663338, "MailMessage", lambda: MailMessage))
_l_(663340)
_c_(663343, _a_(663342, _n_(663341, "c", lambda: c), "set_recs_for_mail_box")) #just for connection
_l_(663344) #just for connection
command_to_db = "SELECT *"
_l_(663345)
try:
    _l_(663357)

    recs = _c_(663351, _a_(663347, _n_(663346, "c", lambda: c), "execute_query"), _a_(663349, _n_(663348, "c", lambda: c), "connection"), _n_(663350, "command_to_db", lambda: command_to_db))
    _l_(663352)
except _c_(663354, _n_(663353, "Error", lambda: Error)):
    _l_(663356)

    pass
    _l_(663355)