# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import Main
    _l_(580805)

except ImportError:
    pass
try:
    import smtplib
    _l_(580807)

except ImportError:
    pass
try:
    import time
    _l_(580809)

except ImportError:
    pass
try:
    from email.message import EmailMessage
    _l_(580811)

except ImportError:
    pass


# send function
def send_email():
    _l_(580964)

    try:
        _l_(580963)

        msg = _c_(580813, _n_(580812, "EmailMessage", lambda: EmailMessage))
        _l_(580814)

        emailText = _c_(580818, _a_(580817, _a_(580816, _n_(580815, "Main", lambda: Main), "email_str"), "get"))
        _l_(580819)
        passwordText = _c_(580823, _a_(580822, _a_(580821, _n_(580820, "Main", lambda: Main), "password_str"), "get"))
        _l_(580824)
        receiverText = _c_(580828, _a_(580827, _a_(580826, _n_(580825, "Main", lambda: Main), "receiver_str"), "get"))
        _l_(580829)
        subjectText = _c_(580833, _a_(580832, _a_(580831, _n_(580830, "Main", lambda: Main), "subject_str"), "get"))
        _l_(580834)
        bodyText = _c_(580838, _a_(580837, _a_(580836, _n_(580835, "Main", lambda: Main), "bodyEntry"), "get"), "1.0", "end-1c")
        _l_(580839)

        _n_(580840, "msg", lambda: msg)['Subject'] = _n_(580841, "subjectText", lambda: subjectText)
        _l_(580842)
        _n_(580843, "msg", lambda: msg)['From'] = _n_(580844, "emailText", lambda: emailText)
        _l_(580845)
        _n_(580846, "msg", lambda: msg)['To'] = _n_(580847, "receiverText", lambda: receiverText)
        _l_(580848)
        _c_(580852, _a_(580850, _n_(580849, "msg", lambda: msg), "set_content"), _n_(580851, "bodyText", lambda: bodyText))
        _l_(580853)

        if _n_(580854, "emailText", lambda: emailText) == "" or _n_(580855, "passwordText", lambda: passwordText) == "" or _n_(580856, "receiverText", lambda: receiverText) == "" or _n_(580857, "subjectText", lambda: subjectText) == "" or _n_(580858, "bodyText", lambda: bodyText) == "":
            _l_(580942)

            _c_(580862, _a_(580861, _a_(580860, _n_(580859, "Main", lambda: Main), "notif"), "config"), text="All fields are required!", fg="red")
            _l_(580863)

            _c_(580867, _a_(580866, _a_(580865, _n_(580864, "Main", lambda: Main), "root"), "update"))
            _l_(580868)
            _c_(580871, _a_(580870, _n_(580869, "time", lambda: time), "sleep"), 2.5)
            _l_(580872)

            _c_(580876, _a_(580875, _a_(580874, _n_(580873, "Main", lambda: Main), "notif"), "config"), text="")
            _l_(580877)
            aux = ""
            _l_(580878)
            return aux
        else:
            server = _c_(580881, _a_(580880, _n_(580879, "smtplib", lambda: smtplib), "SMTP"), 'smtp.gmail.com', 587)
            _l_(580882)
            _c_(580885, _a_(580884, _n_(580883, "server", lambda: server), "starttls"))
            _l_(580886)
            _c_(580891, _a_(580888, _n_(580887, "server", lambda: server), "login"), _n_(580889, "emailText", lambda: emailText), _n_(580890, "passwordText", lambda: passwordText))
            _l_(580892)
            _c_(580896, _a_(580894, _n_(580893, "server", lambda: server), "send_message"), _n_(580895, "msg", lambda: msg))
            _l_(580897)

            _c_(580901, _a_(580900, _a_(580899, _n_(580898, "Main", lambda: Main), "emailEntry"), "delete"), 0, 'end')
            _l_(580902)
            _c_(580906, _a_(580905, _a_(580904, _n_(580903, "Main", lambda: Main), "passwordEntry"), "delete"), 0, 'end')
            _l_(580907)
            _c_(580911, _a_(580910, _a_(580909, _n_(580908, "Main", lambda: Main), "receiverEntry"), "delete"), 0, 'end')
            _l_(580912)
            _c_(580916, _a_(580915, _a_(580914, _n_(580913, "Main", lambda: Main), "subjectEntry"), "delete"), 0, 'end')
            _l_(580917)
            _c_(580921, _a_(580920, _a_(580919, _n_(580918, "Main", lambda: Main), "bodyEntry"), "delete"), "1.0", "end-1c")
            _l_(580922)

            _c_(580926, _a_(580925, _a_(580924, _n_(580923, "Main", lambda: Main), "notif"), "config"), text="Email Sent!", fg="green")
            _l_(580927)

            _c_(580931, _a_(580930, _a_(580929, _n_(580928, "Main", lambda: Main), "root"), "update"))
            _l_(580932)
            _c_(580935, _a_(580934, _n_(580933, "time", lambda: time), "sleep"), 2.5)
            _l_(580936)

            _c_(580940, _a_(580939, _a_(580938, _n_(580937, "Main", lambda: Main), "notif"), "config"), text="")
            _l_(580941)
    except:
        _l_(580962)

        _c_(580946, _a_(580945, _a_(580944, _n_(580943, "Main", lambda: Main), "notif"), "config"), text="There was a error please try again", fg="red")
        _l_(580947)

        _c_(580951, _a_(580950, _a_(580949, _n_(580948, "Main", lambda: Main), "root"), "update"))
        _l_(580952)
        _c_(580955, _a_(580954, _n_(580953, "time", lambda: time), "sleep"), 2.5)
        _l_(580956)

        _c_(580960, _a_(580959, _a_(580958, _n_(580957, "Main", lambda: Main), "notif"), "config"), text="")
        _l_(580961)