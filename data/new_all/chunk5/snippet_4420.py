# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58016854/attributeerror-unknown-senton-error-in-python-outlook
# -*- coding: latin-1 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(678971)

except ImportError:
    pass
try:
    import os
    _l_(678973)

except ImportError:
    pass
try:
    import datetime
    _l_(678975)

except ImportError:
    pass

today = _c_(678979, _a_(678978, _a_(678977, _n_(678976, "datetime", lambda: datetime), "date"), "today"))
_l_(678980)
path = _c_(678983, _a_(678982, _n_(678981, "os", lambda: os), "path"), "D:\my_path")
_l_(678984)

outlook = _c_(678989, _a_(678988, _c_(678987, _a_(678986, _a_(678985, win32com, "client"), "Dispatch"), "Outlook.Application"), "GetNamespace"), "MAPI") #Opens Microsoft Outlook
_l_(678990) #Opens Microsoft Outlook
inbox = _c_(678993, _a_(678992, _n_(678991, "outlook", lambda: outlook), "GetDefaultFolder"), 6) #N4 Invocie folder
_l_(678994) #N4 Invocie folder
messages = _a_(678996, _n_(678995, "inbox", lambda: inbox), "Items")  #Get first email
_l_(678997)  #Get first email


def saveattachemnts(subject = "Title Maíl - *"):
    _l_(679042)

    for message in _n_(678998, "messages", lambda: messages):
        _l_(679041)

        if _a_(679000, _n_(678999, "message", lambda: message), "Subject") == _n_(679001, "subject", lambda: subject) and _a_(679003, _n_(679002, "message", lambda: message), "Unread") or _c_(679007, _a_(679006, _a_(679005, _n_(679004, "message", lambda: message), "Senton"), "date")) == _n_(679008, "today", lambda: today):
            _l_(679040)

            attachments = _a_(679010, _n_(679009, "message", lambda: message), "Attachments")
            _l_(679011)
            attachment = _c_(679014, _a_(679013, _n_(679012, "attachments", lambda: attachments), "Item"), 1)
            _l_(679015)
            for attachment in _a_(679017, _n_(679016, "message", lambda: message), "Attachments"):
                _l_(679039)

                _c_(679028, _a_(679019, _n_(679018, "attachment", lambda: attachment), "SaveAsFile"), _c_(679027, _a_(679022, _a_(679021, _n_(679020, "os", lambda: os), "path"), "join"), _n_(679023, "path", lambda: path), _c_(679026, _n_(679024, "str", lambda: str), _n_(679025, "attachment", lambda: attachment))))
                _l_(679029)
                if _a_(679031, _n_(679030, "message", lambda: message), "Subject") == _n_(679032, "subject", lambda: subject) and _a_(679034, _n_(679033, "message", lambda: message), "Unread"):
                    _l_(679037)

                    _n_(679035, "message", lambda: message).Unread = False
                    _l_(679036)
                break
                _l_(679038)

_c_(679044, _n_(679043, "saveattachemnts", lambda: saveattachemnts))
_l_(679045)
_c_(679048, _a_(679047, _n_(679046, "os", lambda: os), "system"), "this_python.py")
_l_(679049)