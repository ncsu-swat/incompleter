# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37783437/nameerror-which-isnt-name-error-python
#!/usr/bin/python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(610077)

except ImportError:
    pass
try:
    import smtplib
    _l_(610079)

except ImportError:
    pass
with _c_(610081, _n_(610080, "open", lambda: open), "/linux/sendmail",'r') as nas_file:
    _l_(610086)

    success=_c_(610084, _a_(610083, _n_(610082, "nas_file", lambda: nas_file), "read"))
    _l_(610085)

_c_(610089, _n_(610087, "print", lambda: print), _n_(610088, "success", lambda: success))
_l_(610090)
def send_mail(msg):
    _l_(610121)

    fromaddr = 'XXXXX'
    _l_(610091)
    toaddrs  = 'XXXXX'
    _l_(610092)


    # Credentials (if needed)
    username = 'XXXXX'
    _l_(610093)
    password = 'XXXXX'
    _l_(610094)

    # The actual mail send
    server = _c_(610097, _a_(610096, _n_(610095, "smtplib", lambda: smtplib), "SMTP"), 'smtp.gmail.com:587')
    _l_(610098)
    _c_(610101, _a_(610100, _n_(610099, "server", lambda: server), "starttls"))
    _l_(610102)
    _c_(610107, _a_(610104, _n_(610103, "server", lambda: server), "login"), _n_(610105, "username", lambda: username),_n_(610106, "password", lambda: password))
    _l_(610108)
    _c_(610114, _a_(610110, _n_(610109, "server", lambda: server), "sendmail"), _n_(610111, "fromaddr", lambda: fromaddr), _n_(610112, "toaddrs", lambda: toaddrs), _n_(610113, "msg", lambda: msg))
    _l_(610115)
    _c_(610118, _a_(610117, _n_(610116, "server", lambda: server), "quit"))
    _l_(610119)
    aux = ""
    _l_(610120)
    return aux
if True:
    _l_(610126)

    _c_(610124, _n_(610122, "send_mail", lambda: send_mail), _n_(610123, "success", lambda: success))
    _l_(610125)