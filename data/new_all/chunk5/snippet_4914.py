# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40579983/attributeerror-outlook-application-logon
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(690848)

except ImportError:
    pass

def main():
    _l_(690890)


    session = _c_(690852, _a_(690851, _a_(690850, _a_(690849, win32com, "client"), "dynamic"), "Dispatch"), "Outlook.Application")
    _l_(690853)
    _c_(690856, _a_(690855, _n_(690854, "session", lambda: session), "Logon"), 'Outlook') 
    _l_(690857) 
    inbox = _a_(690859, _n_(690858, "session", lambda: session), "Inbox")
    _l_(690860)
    message = _c_(690864, _a_(690863, _a_(690862, _n_(690861, "inbox", lambda: inbox), "Messages"), "GetLast"))
    _l_(690865)
    attachments = _a_(690867, _n_(690866, "message", lambda: message), "Attachments")
    _l_(690868)
    for i in _c_(690872, _n_(690869, "range", lambda: range), _a_(690871, _n_(690870, "attachments", lambda: attachments), "Count")):
        _l_(690885)

        attachment = _c_(690876, _a_(690874, _n_(690873, "attachments", lambda: attachments), "Item"), _n_(690875, "i", lambda: i) + 1)
        _l_(690877)
        filename = 'C:\EMAILS\tempfile_%i' % _n_(690878, "i", lambda: i)
        _l_(690879)
        _c_(690883, _a_(690881, _n_(690880, "attachment", lambda: attachment), "WriteToFile"), _n_(690882, "filename", lambda: filename))
        _l_(690884)
    _c_(690888, _a_(690887, _n_(690886, "session", lambda: session), "Logoff"))
    _l_(690889)

if _n_(690891, "__name__", lambda: __name__) == '__main__':
    _l_(690895)

    _c_(690893, _n_(690892, "main", lambda: main))
    _l_(690894)