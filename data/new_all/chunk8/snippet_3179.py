# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22268627/typeerror-when-developing-tkinter-notepad-like-application-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(626175)

except ImportError:
    pass
top=_c_(626177, _n_(626176, "Tk", lambda: Tk))
_l_(626178)
_c_(626181, _a_(626180, _n_(626179, "top", lambda: top), "title"), 'Mypad')
_l_(626182)
def save(self,s):
    _l_(626202)

    _n_(626183, "self", lambda: self).s=_c_(626186, _a_(626185, _n_(626184, "filedialog", lambda: filedialog), "asksaveasfilename"), defaultextension='.txt')
    _l_(626187)
    c=_c_(626191, _n_(626188, "open", lambda: open), _a_(626190, _n_(626189, "self", lambda: self), "s"),'w')
    _l_(626192)
    w=_c_(626200, _a_(626194, _n_(626193, "c", lambda: c), "write"), _c_(626199, _n_(626195, "str", lambda: str), _c_(626198, _a_(626197, _n_(626196, "e", lambda: e), "get"), '1.0','end')))
    _l_(626201)
def close():
    _l_(626207)

    _c_(626205, _a_(626204, _n_(626203, "top", lambda: top), "destroy"))
    _l_(626206)
menubar=_c_(626210, _n_(626208, "Menu", lambda: Menu), _n_(626209, "top", lambda: top))
_l_(626211)
file=_c_(626214, _n_(626212, "Menu", lambda: Menu), _n_(626213, "menubar", lambda: menubar),tearoff=0)
_l_(626215)
vet=_c_(626219, _a_(626217, _n_(626216, "file", lambda: file), "add_command"), label='Save',command=_n_(626218, "save", lambda: save))
_l_(626220)
_c_(626223, _a_(626222, _n_(626221, "file", lambda: file), "add_separator"))
_l_(626224)
_c_(626228, _a_(626226, _n_(626225, "file", lambda: file), "add_command"), label='Exit',command=_n_(626227, "close", lambda: close))
_l_(626229)
_c_(626233, _a_(626231, _n_(626230, "menubar", lambda: menubar), "add_cascade"), label='File',menu=_n_(626232, "file", lambda: file))
_l_(626234)
e=_c_(626236, _n_(626235, "Text", lambda: Text))
_l_(626237)
_c_(626240, _a_(626239, _n_(626238, "e", lambda: e), "pack"), ipady=30)
_l_(626241)
_c_(626245, _a_(626243, _n_(626242, "top", lambda: top), "config"), menu=_n_(626244, "menubar", lambda: menubar))
_l_(626246)
_c_(626249, _a_(626248, _n_(626247, "top", lambda: top), "mainloop"))
_l_(626250)