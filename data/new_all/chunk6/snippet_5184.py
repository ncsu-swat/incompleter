# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65181993/attributeerror-event-object-has-no-attribute-show-frame-in-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(364399)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(364401)

except ImportError:
    pass
   
class tkinterApp(_n_(364402, "Tk", lambda: Tk)):
    _l_(364472)

      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):
        _l_(364446)

          
        # __init__ function for class Tk 
        _c_(364408, _a_(364404, _n_(364403, "Tk", lambda: Tk), "__init__"), _n_(364405, "self", lambda: self), *_n_(364406, "args", lambda: args), **_n_(364407, "kwargs", lambda: kwargs)) 
        _l_(364409) 
          
        # creating a container 
        container = _c_(364412, _n_(364410, "Frame", lambda: Frame), _n_(364411, "self", lambda: self))   
        _l_(364413)   
        _c_(364416, _a_(364415, _n_(364414, "container", lambda: container), "pack"), side = "top", fill = "both", expand = True)  
        _l_(364417)  
   
        # initializing frames to an empty array 
        _n_(364418, "self", lambda: self).frames = {}
        _l_(364419)
        
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (_n_(364420, "StartPage", lambda: StartPage), _n_(364421, "Page1", lambda: Page1)):
            _l_(364436)

   
            frame = _c_(364425, _n_(364422, "F", lambda: F), _n_(364423, "container", lambda: container), _n_(364424, "self", lambda: self)) 
            _l_(364426) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            _a_(364428, _n_(364427, "self", lambda: self), "frames")[_n_(364429, "F", lambda: F)] = _n_(364430, "frame", lambda: frame)  
            _l_(364431)  
   
            _c_(364434, _a_(364433, _n_(364432, "frame", lambda: frame), "grid"), row = 0, column = 0, sticky ="nsew")
            _l_(364435)
        _c_(364439, _a_(364438, _n_(364437, "self", lambda: self), "update"))
        _l_(364440)
        _c_(364444, _a_(364442, _n_(364441, "self", lambda: self), "show_frame"), _n_(364443, "StartPage", lambda: StartPage))
        _l_(364445)
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont):
        _l_(364471)

        if _n_(364447, "cont", lambda: cont) not in _a_(364449, _n_(364448, "self", lambda: self), "frames"):
            _l_(364458)

            _a_(364451, _n_(364450, "self", lambda: self), "frames")[_n_(364452, "cont", lambda: cont)] = _c_(364456, _n_(364453, "cont", lambda: cont), _n_(364454, "container", lambda: container), _n_(364455, "self", lambda: self))
            _l_(364457)
        frame = _a_(364460, _n_(364459, "self", lambda: self), "frames")[_n_(364461, "cont", lambda: cont)]
        _l_(364462)
        _c_(364465, _a_(364464, _n_(364463, "frame", lambda: frame), "tkraise"))
        _l_(364466)
        _c_(364469, _a_(364468, _n_(364467, "frame", lambda: frame), "event_generate"), "<<ShowFrame>>")
        _l_(364470)
   
# first window frame startpage 
   
class StartPage(_n_(364473, "Frame", lambda: Frame)):
    _l_(364540)

    def __init__(self, parent, controller):
        _l_(364486)

        _c_(364478, _a_(364475, _n_(364474, "Frame", lambda: Frame), "__init__"), _n_(364476, "self", lambda: self), _n_(364477, "parent", lambda: parent))
        _l_(364479)
        _c_(364484, _a_(364481, _n_(364480, "self", lambda: self), "bind"), "<<ShowFrame>>", _a_(364483, _n_(364482, "self", lambda: self), "myStartPage"))
        _l_(364485)

    def printcehck(self,event):
        _l_(364490)

        _c_(364488, _n_(364487, "print", lambda: print), "hack")
        _l_(364489)

    def myStartPage(self,controller):
        _l_(364539)

        _c_(364494, _a_(364493, _n_(364491, "super", lambda: super)(_n_(364492, "StartPage", lambda: StartPage)), "__init__"))
        _l_(364495)
        _c_(364498, _n_(364496, "print", lambda: print), _n_(364497, "controller", lambda: controller))
        _l_(364499)
        canvas = _c_(364502, _n_(364500, "Canvas", lambda: Canvas), _n_(364501, "self", lambda: self),width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        _l_(364503)
        _c_(364506, _a_(364505, _n_(364504, "canvas", lambda: canvas), "pack"))
        _l_(364507)

        _n_(364508, "self", lambda: self).background = _c_(364510, _n_(364509, "PhotoImage", lambda: PhotoImage), file="background.png")
        _l_(364511)
        _c_(364516, _a_(364513, _n_(364512, "canvas", lambda: canvas), "create_image"), 300,300,image=_a_(364515, _n_(364514, "self", lambda: self), "background"), tags="B")
        _l_(364517)

        _n_(364518, "self", lambda: self).character1 = _c_(364520, _n_(364519, "PhotoImage", lambda: PhotoImage), file="bg-e-butd.png")
        _l_(364521)
        obj1 = _c_(364527, _a_(364523, _n_(364522, "canvas", lambda: canvas), "create_image"), 50,50,image=_a_(364525, _n_(364524, "self", lambda: self), "character1"), anchor=_n_(364526, "NW", lambda: NW))
        _l_(364528)
        _c_(364537, _a_(364530, _n_(364529, "canvas", lambda: canvas), "tag_bind"), _n_(364531, "obj1", lambda: obj1), '<1>', lambda event=None : _c_(364536, _a_(364533, _n_(364532, "controller", lambda: controller), "show_frame"), _n_(364534, "self", lambda: self),_n_(364535, "Page1", lambda: Page1))) #error occurs here.
        _l_(364538) #error occurs here.
# second window frame page1  
class Page1(_n_(364541, "Frame", lambda: Frame)):
    _l_(364581)

      
    def __init__(self, parent, controller):
        _l_(364580)

          
        _c_(364546, _a_(364543, _n_(364542, "Frame", lambda: Frame), "__init__"), _n_(364544, "self", lambda: self), _n_(364545, "parent", lambda: parent))
        _l_(364547)

        canvas = _c_(364550, _n_(364548, "Canvas", lambda: Canvas), _n_(364549, "self", lambda: self),width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        _l_(364551)
        _c_(364554, _a_(364553, _n_(364552, "canvas", lambda: canvas), "pack"))
        _l_(364555)

        _n_(364556, "self", lambda: self).background = _c_(364558, _n_(364557, "PhotoImage", lambda: PhotoImage), file="background.png")
        _l_(364559)
        _c_(364564, _a_(364561, _n_(364560, "canvas", lambda: canvas), "create_image"), 300,300,image=_a_(364563, _n_(364562, "self", lambda: self), "background"), tags="B")
        _l_(364565)

        _n_(364566, "self", lambda: self).character1 = _c_(364568, _n_(364567, "PhotoImage", lambda: PhotoImage), file="bg-e-butd.png")
        _l_(364569)
        _c_(364578, _a_(364571, _n_(364570, "self", lambda: self), "after"), 1000, lambda: _c_(364577, _a_(364573, _n_(364572, "canvas", lambda: canvas), "create_image"), 50,50,image=_a_(364575, _n_(364574, "self", lambda: self), "character1"), anchor=_n_(364576, "NW", lambda: NW)))
        _l_(364579)

   
# Driver Code 
app = _c_(364583, _n_(364582, "tkinterApp", lambda: tkinterApp))
_l_(364584)
_c_(364587, _a_(364586, _n_(364585, "app", lambda: app), "title"), "Title")
_l_(364588)
_c_(364591, _a_(364590, _n_(364589, "app", lambda: app), "mainloop")) 
_l_(364592) 