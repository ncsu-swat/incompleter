# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61533489/nameerror-name-username-is-not-defined-in-python-with-tkinter-gui
#26/4/2020 28/4/2020 30/4/2020

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sign_in_clicked():
    _l_(359632)

    username = _c_(359616, _a_(359615, _n_(359614, "username_entry", lambda: username_entry), "get"))
    _l_(359617)
    password = _c_(359620, _a_(359619, _n_(359618, "password_entry", lambda: password_entry), "get"))
    _l_(359621)
    _c_(359625, _a_(359623, _n_(359622, "username_entry", lambda: username_entry), "delete"), 0, _n_(359624, "END", lambda: END))
    _l_(359626)
    _c_(359630, _a_(359628, _n_(359627, "password_entry", lambda: password_entry), "delete"), 0, _n_(359629, "END", lambda: END))
    _l_(359631)
try:
    from tkinter import *
    _l_(359634)

except ImportError:
    pass

sign_in = _c_(359636, _n_(359635, "Tk", lambda: Tk))
_l_(359637)
_c_(359640, _a_(359639, _n_(359638, "sign_in", lambda: sign_in), "title"), "Sign in")
_l_(359641)

sign_in_label = _c_(359647, _a_(359645, _c_(359644, _n_(359642, "Label", lambda: Label), _n_(359643, "sign_in", lambda: sign_in),text="Please Sign In!"), "grid"), row=0, column=0, columnspan=2, sticky=_n_(359646, "W", lambda: W))
_l_(359648)
username_label = _c_(359654, _a_(359652, _c_(359651, _n_(359649, "Label", lambda: Label), _n_(359650, "sign_in", lambda: sign_in),text="Username:"), "grid"), row=1, column=0, sticky=_n_(359653, "W", lambda: W))
_l_(359655)
password_label = _c_(359661, _a_(359659, _c_(359658, _n_(359656, "Label", lambda: Label), _n_(359657, "sign_in", lambda: sign_in),text="password:"), "grid"), row=2, column=0, sticky=_n_(359660, "W", lambda: W))
_l_(359662)

username_entry = _c_(359665, _n_(359663, "Entry", lambda: Entry), _n_(359664, "sign_in", lambda: sign_in), width=20, bg="gray70")
_l_(359666)
_c_(359670, _a_(359668, _n_(359667, "username_entry", lambda: username_entry), "grid"), row=1, column=1, sticky=_n_(359669, "W", lambda: W))
_l_(359671)
password_entry = _c_(359674, _n_(359672, "Entry", lambda: Entry), _n_(359673, "sign_in", lambda: sign_in), width=20, bg="gray70")
_l_(359675)
_c_(359679, _a_(359677, _n_(359676, "password_entry", lambda: password_entry), "grid"), row=2, column=1, sticky=_n_(359678, "W", lambda: W))
_l_(359680)

sign_in_button = _c_(359687, _a_(359685, _c_(359684, _n_(359681, "Button", lambda: Button), _n_(359682, "sign_in", lambda: sign_in), text="Sign In", width=25, command=_n_(359683, "sign_in_clicked", lambda: sign_in_clicked)), "grid"), row=3, column=0, columnspan=2, sticky=_n_(359686, "W", lambda: W))
_l_(359688)

output_text = _c_(359692, _n_(359689, "Text", lambda: Text), _n_(359690, "sign_in", lambda: sign_in), width=23, height=6, wrap=_n_(359691, "WORD", lambda: WORD), background="DarkOrchid1")
_l_(359693)
_c_(359697, _a_(359695, _n_(359694, "output_text", lambda: output_text), "grid"), row=6, column=0, columnspan=2, sticky=_n_(359696, "W", lambda: W))
_l_(359698)

if _n_(359699, "username", lambda: username)=="1" and _n_(359700, "password", lambda: password)=="2":
    _l_(359706)

    _c_(359704, _a_(359702, _n_(359701, "output_text", lambda: output_text), "insert"), _n_(359703, "END", lambda: END), "hi")
    _l_(359705)

_c_(359709, _a_(359708, _n_(359707, "sign_in", lambda: sign_in), "mainloop"))
_l_(359710)