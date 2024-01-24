# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71457635/typeerror-init-takes-from-1-to-2-positional-arguments-but-3-were-given-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class StartPage(_a_(455468, _n_(455467, "ttk", lambda: ttk), "Frame")):
    _l_(455517)

    def __init__(self, parent, controller):
        _l_(455483)

        _n_(455469, "self", lambda: self).controller = _n_(455470, "controller", lambda: controller)
        _l_(455471)
        _c_(455477, _a_(455474, _a_(455473, _n_(455472, "ttk", lambda: ttk), "Frame"), "__init__"), _n_(455475, "self", lambda: self), _n_(455476, "parent", lambda: parent))
        _l_(455478)
        _c_(455481, _a_(455480, _n_(455479, "self", lambda: self), "startMenu"))
        _l_(455482)

    def startMenu(self):
        _l_(455516)

        heading = _c_(455486, _n_(455484, "Label", lambda: Label), _n_(455485, "self", lambda: self), text="My App", font=('Arial', 30))
        _l_(455487)
        _c_(455490, _a_(455489, _n_(455488, "heading", lambda: heading), "grid"), column=0, row=0)
        _l_(455491)

        start_button = _c_(455499, _n_(455492, "Button", lambda: Button), _n_(455493, "self", lambda: self), text="Start", font='Arial 16', width=8, command=lambda: _c_(455498, _a_(455496, _a_(455495, _n_(455494, "self", lambda: self), "controller"), "show_frame"), _n_(455497, "LoginPage", lambda: LoginPage)))
        _l_(455500)
        _c_(455503, _a_(455502, _n_(455501, "start_button", lambda: start_button), "grid"), column=0, row=1)
        _l_(455504)

        exit_button = _c_(455510, _n_(455505, "Button", lambda: Button), _n_(455506, "self", lambda: self), text="Exit", font='Arial 16', width=8, command=_a_(455509, _a_(455508, _n_(455507, "self", lambda: self), "controller"), "destroy"))
        _l_(455511)
        _c_(455514, _a_(455513, _n_(455512, "exit_button", lambda: exit_button), "grid"), column=1, row=1)
        _l_(455515)