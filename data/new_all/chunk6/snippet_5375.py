# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60950088/typeerror-sequence-item-0-expected-str-instance-tuple-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import smtplib
    _l_(364070)

except ImportError:
    pass
try:
    from email.mime.multipart import MIMEMultipart
    _l_(364072)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(364074)

except ImportError:
    pass


MY_ADDRESS = _c_(364076, _n_(364075, "input", lambda: input), 'your email: ')
_l_(364077)

PASSWORD = _c_(364079, _n_(364078, "input", lambda: input), 'your password: ')
_l_(364080)

emailadd = _c_(364082, _n_(364081, "input", lambda: input), 'text file email addresses: ')
_l_(364083)

subject = _c_(364085, _n_(364084, "input", lambda: input), 'text file containing subject  ')
_l_(364086)

body = _c_(364088, _n_(364087, "input", lambda: input), 'text file containing body: ')
_l_(364089)


def getcontacts(filename):
    _l_(364104)

    emails = []
    _l_(364090)
    with _c_(364093, _n_(364091, "open", lambda: open), _n_(364092, "filename", lambda: filename), mode='r', encoding='utf-8') as contacts_file:
        _l_(364101)

        for a_contact in _n_(364094, "contacts_file", lambda: contacts_file):
            _l_(364100)

            _c_(364098, _a_(364096, _n_(364095, "emails", lambda: emails), "append"), _n_(364097, "a_contact", lambda: a_contact))
            _l_(364099)
    aux = _n_(364102, "emails", lambda: emails)
    _l_(364103)
    return aux


def readtemplate(filename):
    _l_(364113)

    with _c_(364107, _n_(364105, "open", lambda: open), _n_(364106, "filename", lambda: filename), 'r', encoding='utf-8') as template_file:
        _l_(364112)

        aux = _c_(364110, _a_(364109, _n_(364108, "template_file", lambda: template_file), "read"))
        _l_(364111)
        return aux


def main():
    _l_(364185)

    global contents, msg
    _l_(364114)
    emails = _c_(364117, _n_(364115, "getcontacts", lambda: getcontacts), _n_(364116, "emailadd", lambda: emailadd))
    _l_(364118)
    message_template = _c_(364121, _n_(364119, "readtemplate", lambda: readtemplate), _n_(364120, "body", lambda: body))
    _l_(364122)


    s = _c_(364125, _a_(364124, _n_(364123, "smtplib", lambda: smtplib), "SMTP"), host='smtp.gmail.com', port=587)
    _l_(364126)
    _c_(364129, _a_(364128, _n_(364127, "s", lambda: s), "starttls"))
    _l_(364130)
    _c_(364135, _a_(364132, _n_(364131, "s", lambda: s), "login"), _n_(364133, "MY_ADDRESS", lambda: MY_ADDRESS), _n_(364134, "PASSWORD", lambda: PASSWORD))
    _l_(364136)


    for email in _c_(364139, _n_(364137, "zip", lambda: zip), _n_(364138, "emails", lambda: emails)):
        _l_(364180)

        msg = _c_(364141, _n_(364140, "MIMEMultipart", lambda: MIMEMultipart))
        _l_(364142)

        f = _c_(364145, _n_(364143, "open", lambda: open), _n_(364144, "subject", lambda: subject), 'r')
        _l_(364146)
        if _a_(364148, _n_(364147, "f", lambda: f), "mode") == 'r':
            _l_(364153)

            contents = _c_(364151, _a_(364150, _n_(364149, "f", lambda: f), "read"))
            _l_(364152)
        _c_(364156, _a_(364155, _n_(364154, "f", lambda: f), "close"))
        _l_(364157)

        _n_(364158, "msg", lambda: msg)['From'] = _n_(364159, "MY_ADDRESS", lambda: MY_ADDRESS)
        _l_(364160)
        _n_(364161, "msg", lambda: msg)['To'] = _n_(364162, "email", lambda: email)
        _l_(364163)
        _n_(364164, "msg", lambda: msg)['Subject'] = _n_(364165, "contents", lambda: contents)
        _l_(364166)

        _c_(364172, _a_(364168, _n_(364167, "msg", lambda: msg), "attach"), _c_(364171, _n_(364169, "MIMEText", lambda: MIMEText), _n_(364170, "message_template", lambda: message_template), 'plain'))
        _l_(364173)

        _c_(364177, _a_(364175, _n_(364174, "s", lambda: s), "send_message"), _n_(364176, "msg", lambda: msg))
        _l_(364178)
        del msg
        _l_(364179)

    _c_(364183, _a_(364182, _n_(364181, "s", lambda: s), "quit"))
    _l_(364184)


if _n_(364186, "__name__", lambda: __name__) == '__main__':
    _l_(364190)

    _c_(364188, _n_(364187, "main", lambda: main))
    _l_(364189)