# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38854169/typeerror-schreiben-methode-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(632065)

except ImportError:
    pass

class Versenden(_n_(632066, "object", lambda: object)):
    _l_(632071)

    def testen(self):
        _l_(632070)

        _c_(632068, _n_(632067, "print", lambda: print), "Funktioniert")
        _l_(632069)


class Schreiben(_n_(632072, "object", lambda: object)):
    _l_(632149)



    def __init__(self, sender, smtpserver, smtppasswort):
        _l_(632086)

        _n_(632073, "self", lambda: self).Absender = _n_(632074, "sender", lambda: sender)
        _l_(632075)
        _n_(632076, "self", lambda: self).Smtpserver = _n_(632077, "smtpserver", lambda: smtpserver)
        _l_(632078)
        _n_(632079, "self", lambda: self).Smtppasswort = _n_(632080, "smtppasswort", lambda: smtppasswort)
        _l_(632081)
        _c_(632084, _a_(632083, _n_(632082, "Schreiben", lambda: Schreiben), "schreiben_methode"))
        _l_(632085)

    def schreiben_methode(self):
        _l_(632148)

        root1 = _c_(632088, _n_(632087, "Tk", lambda: Tk))
        _l_(632089)
        versenden = _c_(632091, _n_(632090, "Versenden", lambda: Versenden))
        _l_(632092)
        labelEmpfaenger = _c_(632095, _n_(632093, "Label", lambda: Label), _n_(632094, "root1", lambda: root1), text="Empfaenger:")
        _l_(632096)
        labelBetreff = _c_(632099, _n_(632097, "Label", lambda: Label), _n_(632098, "root1", lambda: root1), text="Betreff:")
        _l_(632100)
        empfaenger = _c_(632103, _n_(632101, "Entry", lambda: Entry), _n_(632102, "root1", lambda: root1))
        _l_(632104)
        betreff = _c_(632107, _n_(632105, "Entry", lambda: Entry), _n_(632106, "root1", lambda: root1))
        _l_(632108)
        inhalt = _c_(632111, _n_(632109, "Text", lambda: Text), _n_(632110, "root1", lambda: root1), height=10, width=50)
        _l_(632112)
        buttonSenden = _c_(632118, _n_(632113, "Button", lambda: Button), _n_(632114, "root1", lambda: root1), text="senden", command=lambda: _c_(632117, _a_(632116, _n_(632115, "versenden", lambda: versenden), "testen")))
        _l_(632119)

        _c_(632122, _a_(632121, _n_(632120, "labelEmpfaenger", lambda: labelEmpfaenger), "grid"), row=0, column=0)
        _l_(632123)
        _c_(632126, _a_(632125, _n_(632124, "empfaenger", lambda: empfaenger), "grid"), row=0, column=1)
        _l_(632127)
        _c_(632130, _a_(632129, _n_(632128, "labelBetreff", lambda: labelBetreff), "grid"), row=1, column=0)
        _l_(632131)
        _c_(632134, _a_(632133, _n_(632132, "betreff", lambda: betreff), "grid"), row=1, column=1)
        _l_(632135)
        _c_(632138, _a_(632137, _n_(632136, "inhalt", lambda: inhalt), "grid"), row=2, columnspan=2)
        _l_(632139)
        _c_(632142, _a_(632141, _n_(632140, "buttonSenden", lambda: buttonSenden), "grid"), row=3, columnspan=2)
        _l_(632143)

        _c_(632146, _a_(632145, _n_(632144, "root1", lambda: root1), "mainloop"))
        _l_(632147)

root = _c_(632151, _n_(632150, "Tk", lambda: Tk))
_l_(632152)
schreiben = _c_(632154, _n_(632153, "Schreiben", lambda: Schreiben), "a", "a", "a")
_l_(632155)

labelEmail = _c_(632158, _n_(632156, "Label", lambda: Label), _n_(632157, "root", lambda: root), text="Ihre Email-Addresse")
_l_(632159)
labelPasswort = _c_(632162, _n_(632160, "Label", lambda: Label), _n_(632161, "root", lambda: root), text="Ihr Passwort")
_l_(632163)
labelServer = _c_(632166, _n_(632164, "Label", lambda: Label), _n_(632165, "root", lambda: root), text="SMTP-Server")
_l_(632167)


email = _c_(632170, _n_(632168, "Entry", lambda: Entry), _n_(632169, "root", lambda: root))
_l_(632171)
passwort = _c_(632174, _n_(632172, "Entry", lambda: Entry), _n_(632173, "root", lambda: root))
_l_(632175)
server = _c_(632178, _n_(632176, "Entry", lambda: Entry), _n_(632177, "root", lambda: root))
_l_(632179)

buttonWeiter = _c_(632188, _n_(632180, "Button", lambda: Button), _n_(632181, "root", lambda: root), text="Weiter", command=lambda: _c_(632187, _a_(632183, _n_(632182, "schreiben", lambda: schreiben), "schreiben_methode"), _n_(632184, "email", lambda: email), _n_(632185, "server", lambda: server), _n_(632186, "passwort", lambda: passwort)))
_l_(632189)


_c_(632192, _a_(632191, _n_(632190, "labelEmail", lambda: labelEmail), "grid"), row=0)
_l_(632193)
_c_(632196, _a_(632195, _n_(632194, "labelPasswort", lambda: labelPasswort), "grid"), row=1)
_l_(632197)
_c_(632200, _a_(632199, _n_(632198, "email", lambda: email), "grid"), row=0, column=1)
_l_(632201)
_c_(632204, _a_(632203, _n_(632202, "passwort", lambda: passwort), "grid"), row=1, column=1)
_l_(632205)
_c_(632208, _a_(632207, _n_(632206, "labelServer", lambda: labelServer), "grid"), row=2)
_l_(632209)
_c_(632212, _a_(632211, _n_(632210, "server", lambda: server), "grid"), row=2, column=1)
_l_(632213)
_c_(632216, _a_(632215, _n_(632214, "buttonWeiter", lambda: buttonWeiter), "grid"), row=3, columnspan=2)
_l_(632217)

_c_(632220, _a_(632219, _n_(632218, "root", lambda: root), "mainloop"))
_l_(632221)