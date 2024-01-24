# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32908969/typeerror-str-does-not-support-the-buffer-interface-when-using-flask-sendmail
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask.ext.sendmail import Message
    _l_(677128)

except ImportError:
    pass
try:
    from flask.ext.sendmail import Mail
    _l_(677130)

except ImportError:
    pass

mail = _c_(677132, _n_(677131, "Mail", lambda: Mail))
_l_(677133)
_c_(677137, _a_(677135, _n_(677134, "mail", lambda: mail), "init_app"), _n_(677136, "app", lambda: app))
_l_(677138)
msg = _c_(677146, _n_(677139, "Message", lambda: Message), _c_(677141, _a_(677140, "Hello", "encode"), 'utf-8'), sender=_c_(677143, _a_(677142, "xxx@xxx.com", "encode"), 'utf-8'), recipients=_c_(677145, _a_(677144, "xxx@xxx.com", "encode"), 'utf-8'))
_l_(677147)
_n_(677148, "msg", lambda: msg).body = "testing"
_l_(677149)
_n_(677150, "msg", lambda: msg).html = "testing"
_l_(677151)
_c_(677155, _a_(677153, _n_(677152, "mail", lambda: mail), "send"), _n_(677154, "msg", lambda: msg))
_l_(677156)