# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51704416/none-type-error-in-gui-window-execution-of-farenheit-to-deg-celcius-converter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(678171)

except ImportError:
    pass
my_window = _c_(678173, _n_(678172, "Tk", lambda: Tk))
_l_(678174)
def converter():
    _l_(678188)

    F = _c_(678179, _n_(678175, "float", lambda: float), _c_(678178, _a_(678177, _n_(678176, "entry_input", lambda: entry_input), "get")))
    _l_(678180)
    T = (_n_(678181, "F", lambda: F)-32)*5/9
    _l_(678182)
    _n_(678183, "display_Temp", lambda: display_Temp)["text"] = _c_(678186, _n_(678184, "str", lambda: str), _n_(678185, "T", lambda: T)) 
    _l_(678187) 
_c_(678193, _a_(678192, _c_(678191, _n_(678189, "Label", lambda: Label), _n_(678190, "my_window", lambda: my_window),text="Enter Temperature in Farenheit = "), "grid"), row=0,column=0)
_l_(678194)
display_Temp = _c_(678199, _a_(678198, _c_(678197, _n_(678195, "Label", lambda: Label), _n_(678196, "my_window", lambda: my_window)), "grid"), row=1,column=1)
_l_(678200)
entry_input = _c_(678205, _a_(678204, _c_(678203, _n_(678201, "Entry", lambda: Entry), _n_(678202, "my_window", lambda: my_window)), "grid"), row=0,column=1)
_l_(678206)
button = _c_(678212, _a_(678211, _c_(678210, _n_(678207, "Button", lambda: Button), _n_(678208, "my_window", lambda: my_window),text="Convert to Deg Celcius",command = _n_(678209, "converter", lambda: converter),bd=8,relief="raised"), "grid"), row=1,column=0)
_l_(678213)
_c_(678216, _a_(678215, _n_(678214, "my_window", lambda: my_window), "mainloop"))
_l_(678217)