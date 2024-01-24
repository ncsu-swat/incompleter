# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57134375/attributeerror-users-arduino-object-has-no-attribute-progressbar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(536087)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(536089)

except ImportError:
    pass
try:
    import time
    _l_(536091)

except ImportError:
    pass

class users_Arduino:
    _l_(536211)


    def __init__(self,window):
        _l_(536124)

        _n_(536092, "self", lambda: self).wind = _n_(536093, "window", lambda: window)
        _l_(536094)
        _c_(536098, _a_(536097, _a_(536096, _n_(536095, "self", lambda: self), "wind"), "title"), "System F2T - Cadastro Arduino")
        _l_(536099)

        menubar = _c_(536102, _n_(536100, "Menu", lambda: Menu), _n_(536101, "window", lambda: window))
        _l_(536103)
        arduino = _c_(536106, _n_(536104, "Menu", lambda: Menu), _n_(536105, "menubar", lambda: menubar),tearoff=0)
        _l_(536107)
        _c_(536111, _a_(536109, _n_(536108, "menubar", lambda: menubar), "add_cascade"), label = "Arduino",menu=_n_(536110, "arduino", lambda: arduino))
        _l_(536112)
        _c_(536117, _a_(536114, _n_(536113, "arduino", lambda: arduino), "add_command"), label = "Conectar/Inserir dados-BD", command=_a_(536116, _n_(536115, "self", lambda: self), "getSerialData"))
        _l_(536118)
        _c_(536122, _a_(536120, _n_(536119, "window", lambda: window), "config"), menu = _n_(536121, "menubar", lambda: menubar))
        _l_(536123)

    def bar():
        _l_(536177)

        _n_(536125, "progress", lambda: progress)['value'] = 20
        _l_(536126)
        _c_(536129, _a_(536128, _n_(536127, "root", lambda: root), "update_idletasks")) 
        _l_(536130) 
        _c_(536133, _a_(536132, _n_(536131, "time", lambda: time), "sleep"), 1) 
        _l_(536134) 

        _n_(536135, "progress", lambda: progress)['value'] = 40
        _l_(536136)
        _c_(536139, _a_(536138, _n_(536137, "root", lambda: root), "update_idletasks")) 
        _l_(536140) 
        _c_(536143, _a_(536142, _n_(536141, "time", lambda: time), "sleep"), 1) 
        _l_(536144) 

        _n_(536145, "progress", lambda: progress)['value'] = 50
        _l_(536146)
        _c_(536149, _a_(536148, _n_(536147, "root", lambda: root), "update_idletasks")) 
        _l_(536150) 
        _c_(536153, _a_(536152, _n_(536151, "time", lambda: time), "sleep"), 1) 
        _l_(536154) 

        _n_(536155, "progress", lambda: progress)['value'] = 60
        _l_(536156)
        _c_(536159, _a_(536158, _n_(536157, "root", lambda: root), "update_idletasks")) 
        _l_(536160) 
        _c_(536163, _a_(536162, _n_(536161, "time", lambda: time), "sleep"), 1) 
        _l_(536164) 

        _n_(536165, "progress", lambda: progress)['value'] = 80
        _l_(536166)
        _c_(536169, _a_(536168, _n_(536167, "root", lambda: root), "update_idletasks")) 
        _l_(536170) 
        _c_(536173, _a_(536172, _n_(536171, "time", lambda: time), "sleep"), 1) 
        _l_(536174) 
        _n_(536175, "progress", lambda: progress)['value'] = 100   
        _l_(536176)   

    def getSerialData(self):
        _l_(536210)

        _n_(536178, "self", lambda: self).progresso = _c_(536180, _n_(536179, "Toplevel", lambda: Toplevel))
        _l_(536181)
        _c_(536185, _a_(536184, _a_(536183, _n_(536182, "self", lambda: self), "progresso"), "title"), "System F2T - Progress")
        _l_(536186)
        _c_(536190, _a_(536189, _a_(536188, _n_(536187, "self", lambda: self), "progresso"), "geometry"), "290x200")
        _l_(536191)
        #self.progresso["bg"] = "#000"
        progress = _c_(536199, _a_(536198, _c_(536197, _a_(536193, _n_(536192, "self", lambda: self), "Progressbar"), _a_(536195, _n_(536194, "self", lambda: self), "progresso"),orient = _n_(536196, "HORIZONTAL", lambda: HORIZONTAL), length = 100, mode = 'determinate'), "pack"), pady = 10) 
        _l_(536200) 
        _c_(536208, _a_(536207, _c_(536206, _n_(536201, "Button", lambda: Button), _a_(536203, _n_(536202, "self", lambda: self), "progresso"), text = 'Start', command = _a_(536205, _n_(536204, "self", lambda: self), "bar")), "pack"), pady = 10) 
        _l_(536209) 

if _n_(536212, "__name__", lambda: __name__) == '__main__':
    _l_(536226)

    window = _c_(536214, _n_(536213, "Tk", lambda: Tk))
    _l_(536215)
    _n_(536216, "window", lambda: window)['bg'] = "#000"
    _l_(536217)
    _c_(536220, _n_(536218, "users_Arduino", lambda: users_Arduino), _n_(536219, "window", lambda: window))
    _l_(536221)
    _c_(536224, _a_(536223, _n_(536222, "window", lambda: window), "mainloop"))
    _l_(536225)