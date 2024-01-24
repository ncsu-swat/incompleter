# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def register_user():
    _l_(686148)


    global username
    _l_(686108)
    global password
    _l_(686109)
    global username_entry
    _l_(686110)
    global password_entry
    _l_(686111)

#Username e password
    username_info = _c_(686114, _a_(686113, _n_(686112, "username", lambda: username), "get"))
    _l_(686115)
    password_info = _c_(686118, _a_(686117, _n_(686116, "password", lambda: password), "get"))
    _l_(686119)

#aprire file in write mode
    file = _c_(686122, _n_(686120, "open", lambda: open), _n_(686121, "username_info", lambda: username_info), "w")
    _l_(686123)

#scrittura info nel file
    _c_(686127, _a_(686125, _n_(686124, "file", lambda: file), "write"), _n_(686126, "username_info", lambda: username_info) + "\n")
    _l_(686128)
    _c_(686132, _a_(686130, _n_(686129, "file", lambda: file), "write"), _n_(686131, "password_info", lambda: password_info))
    _l_(686133)
    _c_(686136, _a_(686135, _n_(686134, "file", lambda: file), "close"))
    _l_(686137)

    _c_(686141, _a_(686139, _n_(686138, "username_entry", lambda: username_entry), "delete"), 0, _n_(686140, "END", lambda: END))
    _l_(686142)
    _c_(686146, _a_(686144, _n_(686143, "password_entry", lambda: password_entry), "delete"), 0, _n_(686145, "END", lambda: END))
    _l_(686147)

_a_(686152, _c_(686151, _n_(686149, "Label", lambda: Label), _n_(686150, "register_screen", lambda: register_screen), text="Registrazione avvenuta con successo", fg="green", font=("Lemon/Milk", 11)), "pack")
_l_(686153)
_a_(686157, _c_(686156, _n_(686154, "Button", lambda: Button), text="Login", height="2", width="30", command = _n_(686155, "login", lambda: login)), "pack")
_l_(686158)