# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63063811/typeerror-utf8-is-an-invalid-keyword-argument-for-compat32-smtplib-email-erro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(380410)

except ImportError:
    pass
try:
    from string import Template
    _l_(380412)

except ImportError:
    pass
try:
    import smtplib
    _l_(380414)

except ImportError:
    pass
try:
    import random
    _l_(380416)

except ImportError:
    pass
try:
    import time
    _l_(380418)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(380420)

except ImportError:
    pass
try:
    from email.mime.multipart import MIMEMultipart
    _l_(380422)

except ImportError:
    pass




template_file = r'C:\Users\91880\Desktop\template.txt'
_l_(380423)
filename = r'C:\Users\91880\Downloads\2307.csv'
_l_(380424)


#  reads the file and returns the names, emails in a list
def get_contacts(file):
    _l_(380451)

    names_list = []
    _l_(380425)
    emails_list = []
    _l_(380426)
    with _c_(380429, _n_(380427, "open", lambda: open), _n_(380428, "file", lambda: file), 'r') as mail_data:
        _l_(380447)

        data = _c_(380433, _a_(380431, _n_(380430, "csv", lambda: csv), "reader"), _n_(380432, "mail_data", lambda: mail_data))
        _l_(380434)
        for details in _n_(380435, "data", lambda: data):
            _l_(380446)

            _c_(380439, _a_(380437, _n_(380436, "names_list", lambda: names_list), "append"), _n_(380438, "details", lambda: details)[0])
            _l_(380440)
            _c_(380444, _a_(380442, _n_(380441, "emails_list", lambda: emails_list), "append"), _n_(380443, "details", lambda: details)[1])
            _l_(380445)
    aux = _n_(380448, "names_list", lambda: names_list), _n_(380449, "emails_list", lambda: emails_list)
    _l_(380450)
    return aux


# reads the template from a text file and returns
def get_template(file):
    _l_(380464)

    with _c_(380454, _n_(380452, "open", lambda: open), _n_(380453, "file", lambda: file), 'r') as template_info:
        _l_(380459)

        template_data = _c_(380457, _a_(380456, _n_(380455, "template_info", lambda: template_info), "read"))
        _l_(380458)
    aux = _c_(380462, _n_(380460, "Template", lambda: Template), _n_(380461, "template_data", lambda: template_data))
    _l_(380463)
    return aux


def main():
    _l_(380554)

    email_user = 'myemail@mail.com'
    _l_(380465)
    password = 'mypassword'
    _l_(380466)

    subs = ['Hi', 'Hello']
    _l_(380467)

    names, emails = _c_(380470, _n_(380468, "get_contacts", lambda: get_contacts), _n_(380469, "filename", lambda: filename))
    _l_(380471)
    template = _c_(380474, _n_(380472, "get_template", lambda: get_template), _n_(380473, "template_file", lambda: template_file))
    _l_(380475)

    with _c_(380478, _a_(380477, _n_(380476, "smtplib", lambda: smtplib), "SMTP"), 'smtp.office365.com', '587') as smtp:
        _l_(380553)

        _c_(380481, _a_(380480, _n_(380479, "smtp", lambda: smtp), "ehlo"))
        _l_(380482)
        _c_(380485, _a_(380484, _n_(380483, "smtp", lambda: smtp), "starttls"))
        _l_(380486)
        _c_(380489, _a_(380488, _n_(380487, "smtp", lambda: smtp), "ehlo"))
        _l_(380490)
        _c_(380495, _a_(380492, _n_(380491, "smtp", lambda: smtp), "login"), _n_(380493, "email_user", lambda: email_user), _n_(380494, "password", lambda: password))
        _l_(380496)
        for name, email in _c_(380500, _n_(380497, "zip", lambda: zip), _n_(380498, "names", lambda: names), _n_(380499, "emails", lambda: emails)):
            _l_(380552)

            subject = _c_(380504, _a_(380502, _n_(380501, "random", lambda: random), "choice"), _n_(380503, "subs", lambda: subs))
            _l_(380505)
            number = _c_(380508, _a_(380507, _n_(380506, "random", lambda: random), "randint"), 10, 30)
            _l_(380509)
            msg = _c_(380511, _n_(380510, "MIMEMultipart", lambda: MIMEMultipart))
            _l_(380512)
            message = _c_(380518, _a_(380514, _n_(380513, "template", lambda: template), "substitute"), name=_c_(380517, _a_(380516, _n_(380515, "name", lambda: name), "title")))
            _l_(380519)
            _n_(380520, "msg", lambda: msg)['From'] = _n_(380521, "email_user", lambda: email_user)
            _l_(380522)
            _n_(380523, "msg", lambda: msg)['To'] = _n_(380524, "email", lambda: email)
            _l_(380525)
            _n_(380526, "msg", lambda: msg)['Subject'] = _n_(380527, "subject", lambda: subject)
            _l_(380528)
            _c_(380534, _a_(380530, _n_(380529, "msg", lambda: msg), "attach"), _c_(380533, _n_(380531, "MIMEText", lambda: MIMEText), _n_(380532, "message", lambda: message), 'html'))
            _l_(380535)
            _c_(380539, _a_(380537, _n_(380536, "smtp", lambda: smtp), "send_message"), _n_(380538, "msg", lambda: msg))
            _l_(380540)
            _c_(380544, _n_(380541, "print", lambda: print), f'sent email to {_n_(380542, "name", lambda: name)} at {_n_(380543, "email", lambda: email)}')
            _l_(380545)
            del msg
            _l_(380546)
            _c_(380550, _a_(380548, _n_(380547, 'time', lambda: time), 'sleep'), _n_(380549, 'number', lambda: number))
            _l_(380551)


if _n_(380555, '__name__', lambda: __name__) == '__main__':
    _l_(380559)

    _c_(380557, _n_(380556, 'main', lambda: main))
    _l_(380558)