# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73538666/print-a-placeholder-in-bold-within-a-sentence-using-tags-attributeerror-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(370345)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(370347)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(370349)

except ImportError:
    pass

root = _c_(370352, _a_(370351, _n_(370350, "tk", lambda: tk), "Tk"))
_l_(370353)
_c_(370356, _a_(370355, _n_(370354, "root", lambda: root), "geometry"), "300x200")
_l_(370357)

combobox=_c_(370361, _a_(370359, _n_(370358, "ttk", lambda: ttk), "Combobox"), _n_(370360, "root", lambda: root), width = 16)
_l_(370362)
_c_(370365, _a_(370364, _n_(370363, "combobox", lambda: combobox), "place"), x=15, y=10)
_l_(370366)
_n_(370367, "combobox", lambda: combobox)['value'] = ["City", "Other"]
_l_(370368)


textbox = _c_(370372, _a_(370370, _n_(370369, "tk", lambda: tk), "Text"), _n_(370371, "root", lambda: root),width=20,height=4)
_l_(370373)
_c_(370376, _a_(370375, _n_(370374, "textbox", lambda: textbox), "place"), x=15, y=50)
_l_(370377)

def function1():
    _l_(370409)

    if _c_(370380, _a_(370379, _n_(370378, "combobox", lambda: combobox), "get")) == "City":
        _l_(370390)

        city = "London" #city = diz[sel_city]["City"]
        _l_(370381) #city = diz[sel_city]["City"]
        city_start = _c_(370384, _a_(370383, _n_(370382, "city", lambda: city), "upper"))
        _l_(370385)
        _c_(370388, _a_(370387, _n_(370386, "city_start", lambda: city_start), "tag_config"), font=("Verdana", 14, 'bold'))
        _l_(370389)


    def function2():
        _l_(370405)

        text =  f"{_n_(370391, 'city_start', lambda: city_start)} Phrase1, Phrase2, Phrase3"
        _l_(370392)
                
        _c_(370396, _a_(370394, _n_(370393, "textbox", lambda: textbox), "delete"), 1.0,_n_(370395, "END", lambda: END))     
        _l_(370397)     
        _c_(370403, _a_(370399, _n_(370398, "textbox", lambda: textbox), "insert"), _a_(370401, _n_(370400, "tk", lambda: tk), "END"), _n_(370402, "text", lambda: text)) #.format(allenat_random=allenat_random, variable_random=variable_random))
        _l_(370404) #.format(allenat_random=allenat_random, variable_random=variable_random))

    _c_(370407, _n_(370406, "function2", lambda: function2))
    _l_(370408)


Button = _c_(370413, _n_(370410, "Button", lambda: Button), _n_(370411, "root", lambda: root), text="Print", command=_n_(370412, "function1", lambda: function1))
_l_(370414)
_c_(370417, _a_(370416, _n_(370415, "Button", lambda: Button), "pack"))
_l_(370418)
_c_(370421, _a_(370420, _n_(370419, "Button", lambda: Button), "place"), x=15, y=130)
_l_(370422)
 
_c_(370425, _a_(370424, _n_(370423, "root", lambda: root), "mainloop"))
_l_(370426)