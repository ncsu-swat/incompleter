# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55813036/how-to-solve-the-error-typeerror-a-bytes-like-object-is-required-not-str-wi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from threading import Thread
    _l_(570736)

except ImportError:
    pass
try:
    from flask_mail import Message
    _l_(570738)

except ImportError:
    pass
try:
    from app import app, mail
    _l_(570740)

except ImportError:
    pass

def send_async_email(app, msg):
    _l_(570750)

    with _c_(570743, _a_(570742, _n_(570741, "app", lambda: app), "app_context")):
        _l_(570749)

        _c_(570747, _a_(570745, _n_(570744, "mail", lambda: mail), "send"), _n_(570746, "msg", lambda: msg))
        _l_(570748)

def send_email(subject, sender, recipients, text_body):
    _l_(570779)

    msg = _c_(570755, _n_(570751, "Message", lambda: Message), _n_(570752, "subject", lambda: subject), sender=_n_(570753, "sender", lambda: sender), recipients=_n_(570754, "recipients", lambda: recipients))
    _l_(570756)
    _n_(570757, "msg", lambda: msg).body = _n_(570758, "text_body", lambda: text_body)
    _l_(570759)
    with _c_(570762, _a_(570761, _n_(570760, "app", lambda: app), "open_resource"), "../logs/chaos.log") as fp:
        _l_(570770)

        _c_(570768, _a_(570764, _n_(570763, "msg", lambda: msg), "attach"), b'../logs/chaos.log', _c_(570767, _a_(570766, _n_(570765, "fp", lambda: fp), "read")))
        _l_(570769)
    _c_(570777, _a_(570776, _c_(570775, _n_(570771, "Thread", lambda: Thread), target=_n_(570772, "send_async_email", lambda: send_async_email), args=(_n_(570773, "app", lambda: app), _n_(570774, "msg", lambda: msg))), "start"))
    _l_(570778)