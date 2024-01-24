# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73538666/print-a-placeholder-in-bold-within-a-sentence-using-tags-attributeerror-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(360506)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(360508)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(360510)

except ImportError:
    pass

root = _c_(360513, _a_(360512, _n_(360511, "tk", lambda: tk), "Tk"))
_l_(360514)
_c_(360517, _a_(360516, _n_(360515, "root", lambda: root), "geometry"), "300x200")
_l_(360518)

combobox=_c_(360522, _a_(360520, _n_(360519, "ttk", lambda: ttk), "Combobox"), _n_(360521, "root", lambda: root), width = 16)
_l_(360523)
_c_(360526, _a_(360525, _n_(360524, "combobox", lambda: combobox), "place"), x=15, y=10)
_l_(360527)
_n_(360528, "combobox", lambda: combobox)['value'] = ["City", "Other"]
_l_(360529)


textbox = _c_(360533, _a_(360531, _n_(360530, "tk", lambda: tk), "Text"), _n_(360532, "root", lambda: root),width=20,height=4)
_l_(360534)
_c_(360537, _a_(360536, _n_(360535, "textbox", lambda: textbox), "place"), x=15, y=50)
_l_(360538)

def function1():
    _l_(360570)

    if _c_(360541, _a_(360540, _n_(360539, "combobox", lambda: combobox), "get")) == "City":
        _l_(360551)

        city = "London" #city = diz[sel_city]["City"]
        _l_(360542) #city = diz[sel_city]["City"]
        city_start = _c_(360545, _a_(360544, _n_(360543, "city", lambda: city), "upper"))
        _l_(360546)
        _c_(360549, _a_(360548, _n_(360547, "city_start", lambda: city_start), "tag_config"), font=("Verdana", 14, 'bold'))
        _l_(360550)


    def function2():
        _l_(360566)

        text =  f"{_n_(360552, 'city_start', lambda: city_start)} Phrase1, Phrase2, Phrase3"
        _l_(360553)
                
        _c_(360557, _a_(360555, _n_(360554, "textbox", lambda: textbox), "delete"), 1.0,_n_(360556, "END", lambda: END))     
        _l_(360558)     
        _c_(360564, _a_(360560, _n_(360559, "textbox", lambda: textbox), "insert"), _a_(360562, _n_(360561, "tk", lambda: tk), "END"), _n_(360563, "text", lambda: text)) #.format(allenat_random=allenat_random, variable_random=variable_random))
        _l_(360565) #.format(allenat_random=allenat_random, variable_random=variable_random))

    _c_(360568, _n_(360567, "function2", lambda: function2))
    _l_(360569)


Button = _c_(360574, _n_(360571, "Button", lambda: Button), _n_(360572, "root", lambda: root), text="Print", command=_n_(360573, "function1", lambda: function1))
_l_(360575)
_c_(360578, _a_(360577, _n_(360576, "Button", lambda: Button), "pack"))
_l_(360579)
_c_(360582, _a_(360581, _n_(360580, "Button", lambda: Button), "place"), x=15, y=130)
_l_(360583)
 
_c_(360586, _a_(360585, _n_(360584, "root", lambda: root), "mainloop"))
_l_(360587)