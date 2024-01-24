# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60392844/webscraping-typeerror-sendmail-missing-1-required-positional-argument-msg
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(475388)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(475390)

except ImportError:
    pass
try:
    import smtplib
    _l_(475392)

except ImportError:
    pass
try:
    import time
    _l_(475394)

except ImportError:
    pass


URL = 'https://www.amazon.co.uk/Garmin-Forerunner-735XT-Multisport-Running-Black-Grey/dp/B01DWIY39A/ref=sr_1_3?keywords=garmin&qid=1582615813&sr=8-3'
_l_(475395)

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
_l_(475396)


def check_price():
    _l_(475444)

    page = _c_(475401, _a_(475398, _n_(475397, "requests", lambda: requests), "get"), _n_(475399, "URL", lambda: URL), headers=_n_(475400, "headers", lambda: headers))
    _l_(475402)

    soup = _c_(475406, _n_(475403, "BeautifulSoup", lambda: BeautifulSoup), _a_(475405, _n_(475404, "page", lambda: page), "content"), 'html.parser')
    _l_(475407)

    title = _c_(475412, _a_(475411, _c_(475410, _a_(475409, _n_(475408, "soup", lambda: soup), "find"), id ="productTitle"), "get_text"))
    _l_(475413)
    price = _c_(475418, _a_(475417, _c_(475416, _a_(475415, _n_(475414, "soup", lambda: soup), "find"), id="priceblock_dealprice"), "get_text"))
    _l_(475419)
    converted_price = _c_(475422, _n_(475420, "float", lambda: float), _n_(475421, "price", lambda: price)[1:6])
    _l_(475423)

    if(_n_(475424, "converted_price", lambda: converted_price) < 160.00):
        _l_(475428)

        _c_(475426, _n_(475425, "send_mail", lambda: send_mail))
        _l_(475427)

    _c_(475431, _n_(475429, "print", lambda: print), _n_(475430, "converted_price", lambda: converted_price))
    _l_(475432)
    _c_(475437, _n_(475433, "print", lambda: print), _c_(475436, _a_(475435, _n_(475434, "title", lambda: title), "strip")))
    _l_(475438)

    if(_n_(475439, "converted_price", lambda: converted_price) > 160.00):
        _l_(475443)

        _c_(475441, _n_(475440, "send_mail", lambda: send_mail))
        _l_(475442)

def send_mail():
    _l_(475482)

    server = _c_(475447, _a_(475446, _n_(475445, "smtplib", lambda: smtplib), "SMTP"), 'smtp.gmail.com', 587)
    _l_(475448)
    _c_(475451, _a_(475450, _n_(475449, "server", lambda: server), "ehlo"))
    _l_(475452)
    _c_(475455, _a_(475454, _n_(475453, "server", lambda: server), "starttls"))
    _l_(475456)
    _c_(475459, _a_(475458, _n_(475457, "server", lambda: server), "ehlo"))
    _l_(475460)

    _c_(475463, _a_(475462, _n_(475461, "server", lambda: server), "login"), 'address', 'mAJnkzjfTqw8xJe')
    _l_(475464)

    subject = 'Price decreased!'
    _l_(475465)
    body = 'Now it is time to buy: https://www.amazon.co.uk/Garmin-Forerunner-735XT-Multisport-Running-Black-Grey/dp/B01DWIY39A/ref=sr_1_3?keywords=garmin&qid=1582615813&sr=8-3'
    _l_(475466)

    msg = f"Subject: {_n_(475467, 'subject', lambda: subject)}\n\n{_n_(475468, 'body', lambda: body)}"
    _l_(475469)

    _c_(475473, _a_(475471, _n_(475470, "server", lambda: server), "sendmail"), 'address@gmail.com',
        _n_(475472, "msg", lambda: msg) 
    )
    _l_(475474)
    _c_(475476, _n_(475475, "print", lambda: print), 'E-mail has been sent!')
    _l_(475477)
    _c_(475480, _a_(475479, _n_(475478, "server", lambda: server), "quit"))
    _l_(475481)

while(True):
    _l_(475490)

    _c_(475484, _n_(475483, "check_price", lambda: check_price))
    _l_(475485)
    _c_(475488, _a_(475487, _n_(475486, "time", lambda: time), "sleep"), 28800)
    _l_(475489)