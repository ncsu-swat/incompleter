# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63555043/attributeerror-unknown-cc-while-trying-to-parse-emails-in-ms-outlook-2010-wi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client as client
    _l_(573319)

except ImportError:
    pass

outlook=_c_(573322, _a_(573321, _n_(573320, "client", lambda: client), "Dispatch"), 'Outlook.Application')
_l_(573323)

namespace=_c_(573326, _a_(573325, _n_(573324, "outlook", lambda: outlook), "GetNameSpace"), "MAPI")
_l_(573327)

Der=_a_(573329, _n_(573328, "namespace", lambda: namespace), "Folders")['Drive']
_l_(573330)

Dinbox=_a_(573332, _n_(573331, "Der", lambda: Der), "Folders")['Inbox']
_l_(573333)

for message in _a_(573335, _n_(573334, "Dinbox", lambda: Dinbox), "Items"):
    _l_(573346)

    if _a_(573337, _n_(573336, "message", lambda: message), "Categories") =="":
        _l_(573345)

        if "xyz" in _a_(573339, _n_(573338, "message", lambda: message), "CC") or "xyz" in _a_(573341, _n_(573340, "message", lambda: message), "To") :
            _l_(573344)

            _n_(573342, "message", lambda: message).Categories="xyz"
            _l_(573343)