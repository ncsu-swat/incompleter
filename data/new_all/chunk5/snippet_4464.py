# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(690656)

except ImportError:
    pass
try:
    import runpy
    _l_(690658)

except ImportError:
    pass

file_globals = _c_(690661, _a_(690660, _n_(690659, "runpy", lambda: runpy), "run_path"), "Register_user().py")
_l_(690662)
file_globals = _c_(690665, _a_(690664, _n_(690663, "runpy", lambda: runpy), "run_path"), "register().py")
_l_(690666)


def main_account_screen():
    _l_(690685)


    global main_screen
    _l_(690667)
    _c_(690672, _a_(690671, _c_(690670, _n_(690668, "Button", lambda: Button), text="Register", height="2", width="30", command=_n_(690669, "register", lambda: register)), "pack"))
    _l_(690673)
    main_screen = _c_(690675, _n_(690674, "Tk", lambda: Tk)) #Crea finetra gui
    _l_(690676) #Crea finetra gui
    _c_(690679, _a_(690678, _n_(690677, "main_screen", lambda: main_screen), "geometry"), "300x250")
    _l_(690680)
    _c_(690683, _a_(690682, _n_(690681, "main_screen", lambda: main_screen), "title"), "Login") #Titolo gui
    _l_(690684) #Titolo gui


#Form
_c_(690689, _a_(690688, _c_(690687, _n_(690686, "Label", lambda: Label), text="Login o Registrati", bg="blue", width="300", height="2", font=("Lemon/Milk", 13)), "pack"))
_l_(690690)
_c_(690694, _a_(690693, _c_(690692, _n_(690691, "Label", lambda: Label), text=""), "pack"))
_l_(690695)

#Login Button
_c_(690699, _a_(690698, _c_(690697, _n_(690696, "Button", lambda: Button), text="Login", height="2", width="30"), "pack"))
_l_(690700)
_c_(690704, _a_(690703, _c_(690702, _n_(690701, "Label", lambda: Label), text=""), "pack"))
_l_(690705)

#Register Button
_c_(690709, _a_(690708, _c_(690707, _n_(690706, "Button", lambda: Button), text="Registrati", height="2", width="30"), "pack"))
_l_(690710)

_c_(690713, _a_(690712, _n_(690711, "main_screen", lambda: main_screen), "mainloop")) #Starta la GUI
_l_(690714) #Starta la GUI

_c_(690716, _n_(690715, "main_account_screen", lambda: main_account_screen)) #Chiama la funzione
_l_(690717) #Chiama la funzione