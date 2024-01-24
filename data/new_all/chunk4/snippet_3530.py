# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72754431/python-list-attribute-error-without-a-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
receiver_email = _c_(627440, _a_(627439, _c_(627438, _n_(627435, "open", lambda: open), _a_(627437, _n_(627436, "subscribers", lambda: subscribers), "txt"), 'r'), "readlines"))
_l_(627441)
for i in _n_(627442, "receiver_email", lambda: receiver_email):
    _l_(627474)

    current_mail = _c_(627445, _a_(627444, _n_(627443, "i", lambda: i), "removesuffix"), "\n")
    _l_(627446)
    _c_(627451, _n_(627447, "print", lambda: print), _c_(627450, _n_(627448, "type", lambda: type), _n_(627449, "current_mail", lambda: current_mail)))
    _l_(627452)
    _c_(627457, _n_(627453, "print", lambda: print), _c_(627456, _n_(627454, "type", lambda: type), _n_(627455, "smtp_data", lambda: smtp_data)[2]))
    _l_(627458)
    _c_(627463, _n_(627459, "print", lambda: print), _c_(627462, _n_(627460, "type", lambda: type), _n_(627461, "message", lambda: message)))
    _l_(627464)
    _c_(627472, _a_(627466, _n_(627465, "smtp", lambda: smtp), "sendmail"), _n_(627467, "smtp_data", lambda: smtp_data)[2], _n_(627468, "current_mail", lambda: current_mail), _c_(627471, _a_(627470, _n_(627469, "message", lambda: message), "as_string")))
    _l_(627473)