# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56955112/nameerror-name-label-is-not-definednameerror-name-label-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(689890)

except ImportError:
    pass
try:
    import runpy
    _l_(689892)

except ImportError:
    pass

file_globals = _c_(689895, _a_(689894, _n_(689893, "runpy", lambda: runpy), "run_path"), "Register_user().py")
_l_(689896)
file_globals = _c_(689899, _a_(689898, _n_(689897, "runpy", lambda: runpy), "run_path"), "register().py")
_l_(689900)


def main_account_screen():
    _l_(689919)


    global main_screen
    _l_(689901)
    _c_(689906, _a_(689905, _c_(689904, _n_(689902, "Button", lambda: Button), text="Register", height="2", width="30", command=_n_(689903, "register", lambda: register)), "pack"))
    _l_(689907)
    main_screen = _c_(689909, _n_(689908, "Tk", lambda: Tk)) #Crea finetra gui
    _l_(689910) #Crea finetra gui
    _c_(689913, _a_(689912, _n_(689911, "main_screen", lambda: main_screen), "geometry"), "300x250")
    _l_(689914)
    _c_(689917, _a_(689916, _n_(689915, "main_screen", lambda: main_screen), "title"), "Login") #Titolo gui
    _l_(689918) #Titolo gui


#Form
_c_(689923, _a_(689922, _c_(689921, _n_(689920, "Label", lambda: Label), text="Login o Registrati", bg="blue", width="300", height="2", font=("Lemon/Milk", 13)), "pack"))
_l_(689924)
_c_(689928, _a_(689927, _c_(689926, _n_(689925, "Label", lambda: Label), text=""), "pack"))
_l_(689929)

#Login Button
_c_(689933, _a_(689932, _c_(689931, _n_(689930, "Button", lambda: Button), text="Login", height="2", width="30"), "pack"))
_l_(689934)
_c_(689938, _a_(689937, _c_(689936, _n_(689935, "Label", lambda: Label), text=""), "pack"))
_l_(689939)

#Register Button
_c_(689943, _a_(689942, _c_(689941, _n_(689940, "Button", lambda: Button), text="Registrati", height="2", width="30"), "pack"))
_l_(689944)

_c_(689947, _a_(689946, _n_(689945, "main_screen", lambda: main_screen), "mainloop")) #Starta la GUI
_l_(689948) #Starta la GUI

_c_(689950, _n_(689949, "main_account_screen", lambda: main_account_screen)) #Chiama la funzione
_l_(689951) #Chiama la funzione