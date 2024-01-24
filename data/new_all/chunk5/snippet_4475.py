# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def register_user():
    _l_(685885)


    global username
    _l_(685845)
    global password
    _l_(685846)
    global username_entry
    _l_(685847)
    global password_entry
    _l_(685848)

#Username e password
    username_info = _c_(685851, _a_(685850, _n_(685849, "username", lambda: username), "get"))
    _l_(685852)
    password_info = _c_(685855, _a_(685854, _n_(685853, "password", lambda: password), "get"))
    _l_(685856)

#aprire file in write mode
    file = _c_(685859, _n_(685857, "open", lambda: open), _n_(685858, "username_info", lambda: username_info), "w")
    _l_(685860)

#scrittura info nel file
    _c_(685864, _a_(685862, _n_(685861, "file", lambda: file), "write"), _n_(685863, "username_info", lambda: username_info) + "\n")
    _l_(685865)
    _c_(685869, _a_(685867, _n_(685866, "file", lambda: file), "write"), _n_(685868, "password_info", lambda: password_info))
    _l_(685870)
    _c_(685873, _a_(685872, _n_(685871, "file", lambda: file), "close"))
    _l_(685874)

    _c_(685878, _a_(685876, _n_(685875, "username_entry", lambda: username_entry), "delete"), 0, _n_(685877, "END", lambda: END))
    _l_(685879)
    _c_(685883, _a_(685881, _n_(685880, "password_entry", lambda: password_entry), "delete"), 0, _n_(685882, "END", lambda: END))
    _l_(685884)

_a_(685889, _c_(685888, _n_(685886, "Label", lambda: Label), _n_(685887, "register_screen", lambda: register_screen), text="Registrazione avvenuta con successo", fg="green", font=("Lemon/Milk", 11)), "pack")
_l_(685890)
_a_(685894, _c_(685893, _n_(685891, "Button", lambda: Button), text="Login", height="2", width="30", command = _n_(685892, "login", lambda: login)), "pack")
_l_(685895)