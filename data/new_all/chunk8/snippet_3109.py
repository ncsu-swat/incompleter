# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45231518/tkinter-listbox-error-attributeerror-int-object-has-no-attribute-tk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(642367)

except ImportError:
    pass

def ListWindow():
    _l_(642407)

    Listwindow = _c_(642369, _n_(642368, "Tk", lambda: Tk))           
    _l_(642370)           
    _c_(642373, _a_(642372, _n_(642371, "Listwindow", lambda: Listwindow), "title"), "Welcome")
    _l_(642374)
    _c_(642377, _a_(642376, _n_(642375, "Listwindow", lambda: Listwindow), "geometry"), "400x130")
    _l_(642378)

    lbl_welcome = _c_(642381, _n_(642379, "Label", lambda: Label), _n_(642380, "Listwindow", lambda: Listwindow),text="Welcome to A list box!")
    _l_(642382)
    _c_(642385, _a_(642384, _n_(642383, "lbl_welcome", lambda: lbl_welcome), "grid"), row=0,column=0,columnspan=10)
    _l_(642386)

    myList = _c_(642389, _n_(642387, "Listbox", lambda: Listbox), _n_(642388, "Listwindow", lambda: Listwindow))
    _l_(642390)
    _c_(642393, _a_(642392, _n_(642391, "myList", lambda: myList), "grid"), row=1,column=0,columnspan=10)
    _l_(642394)

    WidgetNames = ['Button', 'Canvas']
    _l_(642395)
    for widget in _n_(642396, "WidgetNames", lambda: WidgetNames):
        _l_(642402)

        _c_(642400, _a_(642398, _n_(642397, "Listbox", lambda: Listbox), "insert"), 0, _n_(642399, "widget", lambda: widget))
        _l_(642401)
    _c_(642405, _a_(642404, _n_(642403, "myList", lambda: myList), "grid"), row=0,column=0,columnspan=10)
    _l_(642406)

def main():
    _l_(642411)

    _c_(642409, _n_(642408, "ListWindow", lambda: ListWindow))
    _l_(642410)

if _n_(642412, "__name__", lambda: __name__) == "__main__":
    _l_(642416)

    _c_(642414, _n_(642413, "main", lambda: main))
    _l_(642415)