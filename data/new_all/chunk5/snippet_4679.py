# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51704416/none-type-error-in-gui-window-execution-of-farenheit-to-deg-celcius-converter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(702108)

except ImportError:
    pass
my_window = _c_(702110, _n_(702109, "Tk", lambda: Tk))
_l_(702111)
def converter():
    _l_(702125)

    F = _c_(702116, _n_(702112, "float", lambda: float), _c_(702115, _a_(702114, _n_(702113, "entry_input", lambda: entry_input), "get")))
    _l_(702117)
    T = (_n_(702118, "F", lambda: F)-32)*5/9
    _l_(702119)
    _n_(702120, "display_Temp", lambda: display_Temp)["text"] = _c_(702123, _n_(702121, "str", lambda: str), _n_(702122, "T", lambda: T)) 
    _l_(702124) 
_c_(702130, _a_(702129, _c_(702128, _n_(702126, "Label", lambda: Label), _n_(702127, "my_window", lambda: my_window),text="Enter Temperature in Farenheit = "), "grid"), row=0,column=0)
_l_(702131)
display_Temp = _c_(702136, _a_(702135, _c_(702134, _n_(702132, "Label", lambda: Label), _n_(702133, "my_window", lambda: my_window)), "grid"), row=1,column=1)
_l_(702137)
entry_input = _c_(702142, _a_(702141, _c_(702140, _n_(702138, "Entry", lambda: Entry), _n_(702139, "my_window", lambda: my_window)), "grid"), row=0,column=1)
_l_(702143)
button = _c_(702149, _a_(702148, _c_(702147, _n_(702144, "Button", lambda: Button), _n_(702145, "my_window", lambda: my_window),text="Convert to Deg Celcius",command = _n_(702146, "converter", lambda: converter),bd=8,relief="raised"), "grid"), row=1,column=0)
_l_(702150)
_c_(702153, _a_(702152, _n_(702151, "my_window", lambda: my_window), "mainloop"))
_l_(702154)