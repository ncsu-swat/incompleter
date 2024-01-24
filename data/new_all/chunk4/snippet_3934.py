# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65194399/how-to-fix-attributeerror-partially-initialized-module-sendemail-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import Main
    _l_(628533)

except ImportError:
    pass
try:
    import smtplib
    _l_(628535)

except ImportError:
    pass
try:
    import time
    _l_(628537)

except ImportError:
    pass
try:
    from email.message import EmailMessage
    _l_(628539)

except ImportError:
    pass


# send function
def send_email():
    _l_(628692)

    try:
        _l_(628691)

        msg = _c_(628541, _n_(628540, "EmailMessage", lambda: EmailMessage))
        _l_(628542)

        emailText = _c_(628546, _a_(628545, _a_(628544, _n_(628543, "Main", lambda: Main), "email_str"), "get"))
        _l_(628547)
        passwordText = _c_(628551, _a_(628550, _a_(628549, _n_(628548, "Main", lambda: Main), "password_str"), "get"))
        _l_(628552)
        receiverText = _c_(628556, _a_(628555, _a_(628554, _n_(628553, "Main", lambda: Main), "receiver_str"), "get"))
        _l_(628557)
        subjectText = _c_(628561, _a_(628560, _a_(628559, _n_(628558, "Main", lambda: Main), "subject_str"), "get"))
        _l_(628562)
        bodyText = _c_(628566, _a_(628565, _a_(628564, _n_(628563, "Main", lambda: Main), "bodyEntry"), "get"), "1.0", "end-1c")
        _l_(628567)

        _n_(628568, "msg", lambda: msg)['Subject'] = _n_(628569, "subjectText", lambda: subjectText)
        _l_(628570)
        _n_(628571, "msg", lambda: msg)['From'] = _n_(628572, "emailText", lambda: emailText)
        _l_(628573)
        _n_(628574, "msg", lambda: msg)['To'] = _n_(628575, "receiverText", lambda: receiverText)
        _l_(628576)
        _c_(628580, _a_(628578, _n_(628577, "msg", lambda: msg), "set_content"), _n_(628579, "bodyText", lambda: bodyText))
        _l_(628581)

        if _n_(628582, "emailText", lambda: emailText) == "" or _n_(628583, "passwordText", lambda: passwordText) == "" or _n_(628584, "receiverText", lambda: receiverText) == "" or _n_(628585, "subjectText", lambda: subjectText) == "" or _n_(628586, "bodyText", lambda: bodyText) == "":
            _l_(628670)

            _c_(628590, _a_(628589, _a_(628588, _n_(628587, "Main", lambda: Main), "notif"), "config"), text="All fields are required!", fg="red")
            _l_(628591)

            _c_(628595, _a_(628594, _a_(628593, _n_(628592, "Main", lambda: Main), "root"), "update"))
            _l_(628596)
            _c_(628599, _a_(628598, _n_(628597, "time", lambda: time), "sleep"), 2.5)
            _l_(628600)

            _c_(628604, _a_(628603, _a_(628602, _n_(628601, "Main", lambda: Main), "notif"), "config"), text="")
            _l_(628605)
            aux = ""
            _l_(628606)
            return aux
        else:
            server = _c_(628609, _a_(628608, _n_(628607, "smtplib", lambda: smtplib), "SMTP"), 'smtp.gmail.com', 587)
            _l_(628610)
            _c_(628613, _a_(628612, _n_(628611, "server", lambda: server), "starttls"))
            _l_(628614)
            _c_(628619, _a_(628616, _n_(628615, "server", lambda: server), "login"), _n_(628617, "emailText", lambda: emailText), _n_(628618, "passwordText", lambda: passwordText))
            _l_(628620)
            _c_(628624, _a_(628622, _n_(628621, "server", lambda: server), "send_message"), _n_(628623, "msg", lambda: msg))
            _l_(628625)

            _c_(628629, _a_(628628, _a_(628627, _n_(628626, "Main", lambda: Main), "emailEntry"), "delete"), 0, 'end')
            _l_(628630)
            _c_(628634, _a_(628633, _a_(628632, _n_(628631, "Main", lambda: Main), "passwordEntry"), "delete"), 0, 'end')
            _l_(628635)
            _c_(628639, _a_(628638, _a_(628637, _n_(628636, "Main", lambda: Main), "receiverEntry"), "delete"), 0, 'end')
            _l_(628640)
            _c_(628644, _a_(628643, _a_(628642, _n_(628641, "Main", lambda: Main), "subjectEntry"), "delete"), 0, 'end')
            _l_(628645)
            _c_(628649, _a_(628648, _a_(628647, _n_(628646, "Main", lambda: Main), "bodyEntry"), "delete"), "1.0", "end-1c")
            _l_(628650)

            _c_(628654, _a_(628653, _a_(628652, _n_(628651, "Main", lambda: Main), "notif"), "config"), text="Email Sent!", fg="green")
            _l_(628655)

            _c_(628659, _a_(628658, _a_(628657, _n_(628656, "Main", lambda: Main), "root"), "update"))
            _l_(628660)
            _c_(628663, _a_(628662, _n_(628661, "time", lambda: time), "sleep"), 2.5)
            _l_(628664)

            _c_(628668, _a_(628667, _a_(628666, _n_(628665, "Main", lambda: Main), "notif"), "config"), text="")
            _l_(628669)
    except:
        _l_(628690)

        _c_(628674, _a_(628673, _a_(628672, _n_(628671, "Main", lambda: Main), "notif"), "config"), text="There was a error please try again", fg="red")
        _l_(628675)

        _c_(628679, _a_(628678, _a_(628677, _n_(628676, "Main", lambda: Main), "root"), "update"))
        _l_(628680)
        _c_(628683, _a_(628682, _n_(628681, "time", lambda: time), "sleep"), 2.5)
        _l_(628684)

        _c_(628688, _a_(628687, _a_(628686, _n_(628685, "Main", lambda: Main), "notif"), "config"), text="")
        _l_(628689)