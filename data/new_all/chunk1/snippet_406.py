# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71804258/flask-app-nameerror-name-markup-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request, render_template, flash
    _l_(401223)

except ImportError:
    pass
try:
    from flask_mail import Mail, Message
    _l_(401225)

except ImportError:
    pass
try:
    from flask_cors import CORS, cross_origin
    _l_(401227)

except ImportError:
    pass
try:
    from flask_recaptcha import ReCaptcha
    _l_(401229)

except ImportError:
    pass
try:
    import requests
    _l_(401231)

except ImportError:
    pass
try:
    import json
    _l_(401233)

except ImportError:
    pass
try:
    import os
    _l_(401235)

except ImportError:
    pass

app = _c_(401238, _n_(401236, "Flask", lambda: Flask), _n_(401237, "__name__", lambda: __name__), static_folder='static', static_url_path='')
_l_(401239)
recaptcha = _c_(401242, _n_(401240, "ReCaptcha", lambda: ReCaptcha), app=_n_(401241, "app", lambda: app))
_l_(401243)

_a_(401245, _n_(401244, "app", lambda: app), "config")['RECAPTCHA_ENABLED'] = True
_l_(401246)
_a_(401248, _n_(401247, "app", lambda: app), "config")['RECAPTCHA_PUBLIC_KEY'] = '***********************'
_l_(401249)
_a_(401251, _n_(401250, "app", lambda: app), "config")['RECAPTCHA_PRIVATE_KEY'] = '****************************'
_l_(401252)

@_c_(401255, _a_(401254, _n_(401253, "app", lambda: app), "route"), '/', methods=['GET'])
def index():
    _l_(401259)

    aux = _c_(401257, _n_(401256, "render_template", lambda: render_template), "//index.html")
    _l_(401258)
    return aux

@_c_(401262, _a_(401261, _n_(401260, "app", lambda: app), "route"), '/contact-us', methods=['GET'])
@_c_(401265, _a_(401264, _n_(401263, "app", lambda: app), "route"), '/contact', methods=['GET', 'POST'])
def contact():
    _l_(401315)

    if _a_(401267, _n_(401266, "request", lambda: request), "method") == 'POST':
        _l_(401311)

        r = _c_(401272, _a_(401269, _n_(401268, "requests", lambda: requests), "post"), 'https://www.google.com/recaptcha/api/siteverify',
                          data={'secret': '***********',
                                'response': _a_(401271, _n_(401270, "request", lambda: request), "form")['g-recaptcha-response']})
        _l_(401273)
        google_response = _c_(401278, _a_(401275, _n_(401274, "json", lambda: json), "loads"), _a_(401277, _n_(401276, "r", lambda: r), "text"))
        _l_(401279)

        if _n_(401280, "google_response", lambda: google_response)['success']:
            _l_(401310)

            contact_form = {'name': _a_(401282, _n_(401281, "request", lambda: request), "form")['name'],
                            'email': _a_(401284, _n_(401283, "request", lambda: request), "form")['email'],
                            'message': _a_(401286, _n_(401285, "request", lambda: request), "form")['message']}
            _l_(401287)
            msg = _c_(401291, _n_(401288, "Message", lambda: Message), subject='Contact from website',
                          sender=_n_(401289, "contact_form", lambda: contact_form)['email'],
                          recipients=['*************'],
                          body=_n_(401290, "contact_form", lambda: contact_form)['message'])
            _l_(401292)
            _c_(401296, _a_(401294, _n_(401293, "mail", lambda: mail), "send"), _n_(401295, "msg", lambda: msg))
            _l_(401297)
            _c_(401299, _n_(401298, "flash", lambda: flash), 'Success, we will respond within at least 24 hours.')
            _l_(401300)
            aux = _c_(401302, _n_(401301, "render_template", lambda: render_template), 'contact.html')
            _l_(401303)
            return aux

        else:
            _c_(401305, _n_(401304, "flash", lambda: flash), 'failed to submit, please retry or contact us at ************')
            _l_(401306)
            aux = _c_(401308, _n_(401307, "render_template", lambda: render_template), 'contact.html')
            _l_(401309)
            return aux
    aux = _c_(401313, _n_(401312, "render_template", lambda: render_template), 'contact.html')
    _l_(401314)

    return aux

if _n_(401316, "__name__", lambda: __name__) == '__main__':
    _l_(401321)

    _c_(401319, _a_(401318, _n_(401317, "app", lambda: app), "run"))
    _l_(401320)