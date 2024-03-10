# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58016854/attributeerror-unknown-senton-error-in-python-outlook
# -*- coding: latin-1 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(668845)

except ImportError:
    pass
try:
    import os
    _l_(668847)

except ImportError:
    pass
try:
    import datetime
    _l_(668849)

except ImportError:
    pass

today = _c_(668853, _a_(668852, _a_(668851, _n_(668850, "datetime", lambda: datetime), "date"), "today"))
_l_(668854)
path = _c_(668857, _a_(668856, _n_(668855, "os", lambda: os), "path"), "D:\my_path")
_l_(668858)

outlook = _c_(668863, _a_(668862, _c_(668861, _a_(668860, _a_(668859, win32com, "client"), "Dispatch"), "Outlook.Application"), "GetNamespace"), "MAPI") #Opens Microsoft Outlook
_l_(668864) #Opens Microsoft Outlook
inbox = _c_(668867, _a_(668866, _n_(668865, "outlook", lambda: outlook), "GetDefaultFolder"), 6) #N4 Invocie folder
_l_(668868) #N4 Invocie folder
messages = _a_(668870, _n_(668869, "inbox", lambda: inbox), "Items")  #Get first email
_l_(668871)  #Get first email


def saveattachemnts(subject = "Title Maíl - *"):
    _l_(668916)

    for message in _n_(668872, "messages", lambda: messages):
        _l_(668915)

        if _a_(668874, _n_(668873, "message", lambda: message), "Subject") == _n_(668875, "subject", lambda: subject) and _a_(668877, _n_(668876, "message", lambda: message), "Unread") or _c_(668881, _a_(668880, _a_(668879, _n_(668878, "message", lambda: message), "Senton"), "date")) == _n_(668882, "today", lambda: today):
            _l_(668914)

            attachments = _a_(668884, _n_(668883, "message", lambda: message), "Attachments")
            _l_(668885)
            attachment = _c_(668888, _a_(668887, _n_(668886, "attachments", lambda: attachments), "Item"), 1)
            _l_(668889)
            for attachment in _a_(668891, _n_(668890, "message", lambda: message), "Attachments"):
                _l_(668913)

                _c_(668902, _a_(668893, _n_(668892, "attachment", lambda: attachment), "SaveAsFile"), _c_(668901, _a_(668896, _a_(668895, _n_(668894, "os", lambda: os), "path"), "join"), _n_(668897, "path", lambda: path), _c_(668900, _n_(668898, "str", lambda: str), _n_(668899, "attachment", lambda: attachment))))
                _l_(668903)
                if _a_(668905, _n_(668904, "message", lambda: message), "Subject") == _n_(668906, "subject", lambda: subject) and _a_(668908, _n_(668907, "message", lambda: message), "Unread"):
                    _l_(668911)

                    _n_(668909, "message", lambda: message).Unread = False
                    _l_(668910)
                break
                _l_(668912)

_c_(668918, _n_(668917, "saveattachemnts", lambda: saveattachemnts))
_l_(668919)
_c_(668922, _a_(668921, _n_(668920, "os", lambda: os), "system"), "this_python.py")
_l_(668923)