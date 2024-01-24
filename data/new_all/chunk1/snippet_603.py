# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20152258/typeerror-can-only-concatenate-tuple-not-str-to-tuple-in-python
#-*- coding: cp857 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(394727)

except ImportError:
    pass

###########################################################

root=_c_(394729, _n_(394728, "Tk", lambda: Tk))
_l_(394730)

_c_(394733, _a_(394732, _n_(394731, "root", lambda: root), "title"), "MY FILM ARCHIVE")
_l_(394734)

_c_(394737, _a_(394736, _n_(394735, "root", lambda: root), "resizable"), False, False)
_l_(394738)

########################################################### 


def add():
    _l_(394758)

    db = _c_(394740, _n_(394739, "open", lambda: open), r"C:\Users\PC\Desktop\db.txt", "a+")
    _l_(394741)
    enter=_c_(394743, _n_(394742, "input", lambda: input), "Enter your's film: "),
    _l_(394744)
    _c_(394748, _a_(394746, _n_(394745, "db", lambda: db), "write"), _n_(394747, "enter", lambda: enter) + "\n")
    _l_(394749)
    _c_(394752, _a_(394751, _n_(394750, "db", lambda: db), "close"))
    _l_(394753)
    _c_(394756, _a_(394755, _n_(394754, "db", lambda: db), "flush"))    
    _l_(394757)    

button=_c_(394761, _n_(394759, "Button", lambda: Button), text="Add Film!",command=_n_(394760, "add", lambda: add), font=("Flux",15, "bold"))
_l_(394762)
_c_(394765, _a_(394764, _n_(394763, "button", lambda: button), "pack"), expand="yes", anchor="center")
_l_(394766)

_c_(394768, _n_(394767, "mainloop", lambda: mainloop))
_l_(394769)