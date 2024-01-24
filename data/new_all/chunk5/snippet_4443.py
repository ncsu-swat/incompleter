# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57734727/typeerror-argument-of-type-mail-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(658757, _a_(658756, _n_(658755, "app", lambda: app), "route"), '/email', methods=['GET', 'POST'])
def send_mail():
    _l_(658789)

    getting = _c_(658761, _a_(658760, _a_(658759, _n_(658758, "request", lambda: request), "form"), "get"), 'mail')
    _l_(658762)
    token = _c_(658766, _a_(658764, _n_(658763, "s", lambda: s), "dumps"), _n_(658765, "getting", lambda: getting), salt='email-confirm')
    _l_(658767)

    msg = _c_(658770, _n_(658768, "Message", lambda: Message), 'Confirm Email', sender='vatsalayvk1434@gmail.com', recipients=[_n_(658769, "mail", lambda: mail)])
    _l_(658771)

    link = _c_(658774, _n_(658772, "url_for", lambda: url_for), 'confirm_mail', token=_n_(658773, "token", lambda: token), _externel=True)
    _l_(658775)
    _n_(658776, "msg", lambda: msg).body = f'Your Link is {_n_(658777, "link", lambda: link)}'
    _l_(658778)

    _c_(658782, _a_(658780, _n_(658779, 'mail', lambda: mail), 'send'), _n_(658781, 'msg', lambda: msg))
    _l_(658783)
    aux = _c_(658787, _n_(658784, 'render_template', lambda: render_template), 'confirm.html', getting=_n_(658785, 'getting', lambda: getting), token=_n_(658786, 'token', lambda: token))
    _l_(658788)
    return aux