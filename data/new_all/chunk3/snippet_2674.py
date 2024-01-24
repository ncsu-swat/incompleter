# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67120601/attributeerror-demo1-object-has-no-attribute-textbox
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(538360)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(538362)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(538364)

except ImportError:
    pass


def fun1(self,name):
    _l_(538371)

    result="check"
    _l_(538365)
    _c_(538369, _a_(538367, _n_(538366, "Demo2", lambda: Demo2), "data"), _n_(538368, "result", lambda: result))
    _l_(538370)
def cal(master):
    _l_(538376)

    master = _c_(538374, _n_(538372, "Demo2", lambda: Demo2), _n_(538373, "master", lambda: master))
    _l_(538375)

class Demo1:
    _l_(538406)

    
    def __init__(self, master):
        _l_(538405)

        _n_(538377, "self", lambda: self).master = _n_(538378, "master", lambda: master)
        _l_(538379)

        button=_c_(538387, _a_(538381, _n_(538380, "tk", lambda: tk), "Button"), _a_(538383, _n_(538382, "self", lambda: self), "master"), text="check",anchor="w",command=lambda :_c_(538386, _n_(538384, "fun1", lambda: fun1), _n_(538385, "self", lambda: self),"abc") )
        _l_(538388)
        _c_(538391, _a_(538390, _n_(538389, "button", lambda: button), "grid"), row=0,column=1)
        _l_(538392)
        _c_(538403, _a_(538394, _n_(538393, "button", lambda: button), "config"), command=lambda button=_n_(538395, "button", lambda: button): [_c_(538399, _n_(538396, "cal", lambda: cal), _a_(538398, _n_(538397, "self", lambda: self), "master")),_c_(538402, _n_(538400, "fun1", lambda: fun1), _n_(538401, "self", lambda: self),"abc")])
        _l_(538404)
class Demo2:
    _l_(538430)

    def __init__(self, master):
        _l_(538422)

        _n_(538407, "self", lambda: self).master = _n_(538408, "master", lambda: master)
        _l_(538409)

        _n_(538410, "self", lambda: self).textbox=_c_(538415, _a_(538412, _n_(538411, "tk", lambda: tk), "Text"), _a_(538414, _n_(538413, "self", lambda: self), "master"),font=('Calibri',12))
        _l_(538416)
        _c_(538420, _a_(538419, _a_(538418, _n_(538417, "self", lambda: self), "textbox"), "grid"), row=0,column=1)
        _l_(538421)

    def data(self,data):
        _l_(538429)

        _c_(538427, _a_(538425, _a_(538424, _n_(538423, "self", lambda: self), "textbox"), "insert"), 'end',_n_(538426, "data", lambda: data))
        _l_(538428)
def main():
    _l_(538443)

    root = _c_(538433, _a_(538432, _n_(538431, "tk", lambda: tk), "Tk"))
    _l_(538434)
    app = _c_(538437, _n_(538435, "Demo1", lambda: Demo1), _n_(538436, "root", lambda: root))
    _l_(538438)
    _c_(538441, _a_(538440, _n_(538439, "root", lambda: root), "mainloop"))
    _l_(538442)


if _n_(538444, "__name__", lambda: __name__) == '__main__':
    _l_(538448)

    _c_(538446, _n_(538445, "main", lambda: main))        
    _l_(538447)        