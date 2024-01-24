# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65945389/why-am-i-receiving-this-nameerror-when-attempting-to-add-an-outlooks-email-atta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(620255)

except ImportError:
    pass
try:
    import datetime as date
    _l_(620257)

except ImportError:
    pass

# Input
f = _c_(620259, _n_(620258, "open", lambda: open), "testfile.txt", "w+")
_l_(620260)


outlook = _c_(620265, _a_(620264, _c_(620263, _a_(620262, _a_(620261, win32com, "client"), "Dispatch"), "Outlook.Application"), "GetNamespace"), "MAPI")
_l_(620266)
folder = _c_(620270, _a_(620269, _a_(620268, _n_(620267, "outlook", lambda: outlook), "Folders"), "Item"), "TestFolder")
_l_(620271)
inbox = _c_(620275, _a_(620274, _a_(620273, _n_(620272, "folder", lambda: folder), "Folders"), "Item"), "Inbox")
_l_(620276)
msg = _a_(620278, _n_(620277, "inbox", lambda: inbox), "Items")
_l_(620279)

# Process
list = []
_l_(620280)

for x in _n_(620281, "msg", lambda: msg):
    _l_(620310)

    senderEmail = _a_(620283, _n_(620282, "x", lambda: x), "SenderEmailAddress")
    _l_(620284)
    sender = _a_(620286, _n_(620285, "x", lambda: x), "SenderName")
    _l_(620287)
    subject = _a_(620289, _n_(620288, "x", lambda: x), "Subject")
    _l_(620290)
    if _a_(620292, _n_(620291, "x", lambda: x), "Attachments"):
        _l_(620299)

        for f in _a_(620294, _n_(620293, "x", lambda: x), "Attachments"):
            _l_(620298)

            attachment = _a_(620296, _n_(620295, "f", lambda: f), "FileName")
            _l_(620297)
    sum = [_n_(620300, "subject", lambda: subject), _n_(620301, "sender", lambda: sender), _n_(620302, "senderEmail", lambda: senderEmail), _n_(620303, "attachment", lambda: attachment)]
    _l_(620304)
    _c_(620308, _a_(620306, _n_(620305, "list", lambda: list), "extend"), _n_(620307, "sum", lambda: sum))
    _l_(620309)