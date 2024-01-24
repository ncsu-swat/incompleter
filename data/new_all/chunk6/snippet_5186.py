# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65181993/attributeerror-event-object-has-no-attribute-show-frame-in-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(351404)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(351406)

except ImportError:
    pass
   
class tkinterApp(_n_(351407, "Tk", lambda: Tk)):
    _l_(351477)

      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):
        _l_(351451)

          
        # __init__ function for class Tk 
        _c_(351413, _a_(351409, _n_(351408, "Tk", lambda: Tk), "__init__"), _n_(351410, "self", lambda: self), *_n_(351411, "args", lambda: args), **_n_(351412, "kwargs", lambda: kwargs)) 
        _l_(351414) 
          
        # creating a container 
        container = _c_(351417, _n_(351415, "Frame", lambda: Frame), _n_(351416, "self", lambda: self))   
        _l_(351418)   
        _c_(351421, _a_(351420, _n_(351419, "container", lambda: container), "pack"), side = "top", fill = "both", expand = True)  
        _l_(351422)  
   
        # initializing frames to an empty array 
        _n_(351423, "self", lambda: self).frames = {}
        _l_(351424)
        
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (_n_(351425, "StartPage", lambda: StartPage), _n_(351426, "Page1", lambda: Page1)):
            _l_(351441)

   
            frame = _c_(351430, _n_(351427, "F", lambda: F), _n_(351428, "container", lambda: container), _n_(351429, "self", lambda: self)) 
            _l_(351431) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            _a_(351433, _n_(351432, "self", lambda: self), "frames")[_n_(351434, "F", lambda: F)] = _n_(351435, "frame", lambda: frame)  
            _l_(351436)  
   
            _c_(351439, _a_(351438, _n_(351437, "frame", lambda: frame), "grid"), row = 0, column = 0, sticky ="nsew")
            _l_(351440)
        _c_(351444, _a_(351443, _n_(351442, "self", lambda: self), "update"))
        _l_(351445)
        _c_(351449, _a_(351447, _n_(351446, "self", lambda: self), "show_frame"), _n_(351448, "StartPage", lambda: StartPage))
        _l_(351450)
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont):
        _l_(351476)

        if _n_(351452, "cont", lambda: cont) not in _a_(351454, _n_(351453, "self", lambda: self), "frames"):
            _l_(351463)

            _a_(351456, _n_(351455, "self", lambda: self), "frames")[_n_(351457, "cont", lambda: cont)] = _c_(351461, _n_(351458, "cont", lambda: cont), _n_(351459, "container", lambda: container), _n_(351460, "self", lambda: self))
            _l_(351462)
        frame = _a_(351465, _n_(351464, "self", lambda: self), "frames")[_n_(351466, "cont", lambda: cont)]
        _l_(351467)
        _c_(351470, _a_(351469, _n_(351468, "frame", lambda: frame), "tkraise"))
        _l_(351471)
        _c_(351474, _a_(351473, _n_(351472, "frame", lambda: frame), "event_generate"), "<<ShowFrame>>")
        _l_(351475)
   
# first window frame startpage 
   
class StartPage(_n_(351478, "Frame", lambda: Frame)):
    _l_(351545)

    def __init__(self, parent, controller):
        _l_(351491)

        _c_(351483, _a_(351480, _n_(351479, "Frame", lambda: Frame), "__init__"), _n_(351481, "self", lambda: self), _n_(351482, "parent", lambda: parent))
        _l_(351484)
        _c_(351489, _a_(351486, _n_(351485, "self", lambda: self), "bind"), "<<ShowFrame>>", _a_(351488, _n_(351487, "self", lambda: self), "myStartPage"))
        _l_(351490)

    def printcehck(self,event):
        _l_(351495)

        _c_(351493, _n_(351492, "print", lambda: print), "hack")
        _l_(351494)

    def myStartPage(self,controller):
        _l_(351544)

        _c_(351499, _a_(351498, _n_(351496, "super", lambda: super)(_n_(351497, "StartPage", lambda: StartPage)), "__init__"))
        _l_(351500)
        _c_(351503, _n_(351501, "print", lambda: print), _n_(351502, "controller", lambda: controller))
        _l_(351504)
        canvas = _c_(351507, _n_(351505, "Canvas", lambda: Canvas), _n_(351506, "self", lambda: self),width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        _l_(351508)
        _c_(351511, _a_(351510, _n_(351509, "canvas", lambda: canvas), "pack"))
        _l_(351512)

        _n_(351513, "self", lambda: self).background = _c_(351515, _n_(351514, "PhotoImage", lambda: PhotoImage), file="background.png")
        _l_(351516)
        _c_(351521, _a_(351518, _n_(351517, "canvas", lambda: canvas), "create_image"), 300,300,image=_a_(351520, _n_(351519, "self", lambda: self), "background"), tags="B")
        _l_(351522)

        _n_(351523, "self", lambda: self).character1 = _c_(351525, _n_(351524, "PhotoImage", lambda: PhotoImage), file="bg-e-butd.png")
        _l_(351526)
        obj1 = _c_(351532, _a_(351528, _n_(351527, "canvas", lambda: canvas), "create_image"), 50,50,image=_a_(351530, _n_(351529, "self", lambda: self), "character1"), anchor=_n_(351531, "NW", lambda: NW))
        _l_(351533)
        _c_(351542, _a_(351535, _n_(351534, "canvas", lambda: canvas), "tag_bind"), _n_(351536, "obj1", lambda: obj1), '<1>', lambda event=None : _c_(351541, _a_(351538, _n_(351537, "controller", lambda: controller), "show_frame"), _n_(351539, "self", lambda: self),_n_(351540, "Page1", lambda: Page1))) #error occurs here.
        _l_(351543) #error occurs here.
# second window frame page1  
class Page1(_n_(351546, "Frame", lambda: Frame)):
    _l_(351586)

      
    def __init__(self, parent, controller):
        _l_(351585)

          
        _c_(351551, _a_(351548, _n_(351547, "Frame", lambda: Frame), "__init__"), _n_(351549, "self", lambda: self), _n_(351550, "parent", lambda: parent))
        _l_(351552)

        canvas = _c_(351555, _n_(351553, "Canvas", lambda: Canvas), _n_(351554, "self", lambda: self),width=300, height=300, bd=0, highlightthickness=0, relief='ridge')
        _l_(351556)
        _c_(351559, _a_(351558, _n_(351557, "canvas", lambda: canvas), "pack"))
        _l_(351560)

        _n_(351561, "self", lambda: self).background = _c_(351563, _n_(351562, "PhotoImage", lambda: PhotoImage), file="background.png")
        _l_(351564)
        _c_(351569, _a_(351566, _n_(351565, "canvas", lambda: canvas), "create_image"), 300,300,image=_a_(351568, _n_(351567, "self", lambda: self), "background"), tags="B")
        _l_(351570)

        _n_(351571, "self", lambda: self).character1 = _c_(351573, _n_(351572, "PhotoImage", lambda: PhotoImage), file="bg-e-butd.png")
        _l_(351574)
        _c_(351583, _a_(351576, _n_(351575, "self", lambda: self), "after"), 1000, lambda: _c_(351582, _a_(351578, _n_(351577, "canvas", lambda: canvas), "create_image"), 50,50,image=_a_(351580, _n_(351579, "self", lambda: self), "character1"), anchor=_n_(351581, "NW", lambda: NW)))
        _l_(351584)

   
# Driver Code 
app = _c_(351588, _n_(351587, "tkinterApp", lambda: tkinterApp))
_l_(351589)
_c_(351592, _a_(351591, _n_(351590, "app", lambda: app), "title"), "Title")
_l_(351593)
_c_(351596, _a_(351595, _n_(351594, "app", lambda: app), "mainloop")) 
_l_(351597) 