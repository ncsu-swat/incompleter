# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38075488/how-to-fix-attributeerror-with-imagetk-and-tkinter-in-python3-4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(465336)

except ImportError:
    pass
try:
    import sys
    _l_(465338)

except ImportError:
    pass
try:
    from timeit import default_timer as timer
    _l_(465340)

except ImportError:
    pass
try:
    import time
    _l_(465342)

except ImportError:
    pass
try:
    from PIL import ImageTk, Image
    _l_(465344)

except ImportError:
    pass



tot_time=0
_l_(465345)
del_time=0
_l_(465346)
imgpath=r'logo.jpg'
_l_(465347)

def NewTab():
    _l_(465384)

    start=_c_(465349, _n_(465348, "timer", lambda: timer))
    _l_(465350)
    _c_(465354, _a_(465352, _n_(465351, "time", lambda: time), "sleep"), _n_(465353, "del_time", lambda: del_time)) #user defined delay time
    _l_(465355) #user defined delay time
    _c_(465358, _a_(465357, _n_(465356, "window", lambda: window), "withdraw"))
    _l_(465359)
    _c_(465362, _a_(465361, _n_(465360, "win2", lambda: win2), "deiconify"))
    _l_(465363)
    end=_c_(465365, _n_(465364, "timer", lambda: timer))
    _l_(465366)
    tot_time=_n_(465367, "end", lambda: end)-_n_(465368, "start", lambda: start)
    _l_(465369)

    _c_(465382, _a_(465371, _n_(465370, "labW2", lambda: labW2), "configure"), text=('That took %s miliseconds or %s seconds'%(_c_(465376, _n_(465372, "str", lambda: str), _c_(465375, _n_(465373, "round", lambda: round), _n_(465374, "tot_time", lambda: tot_time)*1000,5)),_c_(465381, _n_(465377, "str", lambda: str), _c_(465380, _n_(465378, "round", lambda: round), _n_(465379, "tot_time", lambda: tot_time),5)))))
    _l_(465383)

def close():
    _l_(465389)

    _c_(465387, _a_(465386, _n_(465385, "sys", lambda: sys), "exit"))
    _l_(465388)

def NTButt():
    _l_(465398)

    _c_(465392, _a_(465391, _n_(465390, "win2", lambda: win2), "withdraw"))
    _l_(465393)
    _c_(465396, _a_(465395, _n_(465394, "window", lambda: window), "deiconify"))
    _l_(465397)


win2=_c_(465401, _a_(465400, _n_(465399, "tk", lambda: tk), "Tk"))
_l_(465402)
_c_(465405, _a_(465404, _n_(465403, "win2", lambda: win2), "geometry"), '1100x900')
_l_(465406)
_c_(465409, _a_(465408, _n_(465407, "win2", lambda: win2), "title"), 'Button Click')
_l_(465410)
labW2=_c_(465414, _a_(465412, _n_(465411, "tk", lambda: tk), "Label"), _n_(465413, "win2", lambda: win2), text='ERROR: Time could not be calculated')
_l_(465415)
butW2=_c_(465420, _a_(465417, _n_(465416, "tk", lambda: tk), "Button"), _n_(465418, "win2", lambda: win2), text='Go back', bg='White', command=_n_(465419, "NTButt", lambda: NTButt))
_l_(465421)
btn2W2=_c_(465426, _a_(465423, _n_(465422, "tk", lambda: tk), "Button"), _n_(465424, "win2", lambda: win2), text='Leave', bg='Red', command=_n_(465425, "close", lambda: close))
_l_(465427)
_c_(465430, _a_(465429, _n_(465428, "labW2", lambda: labW2), "pack"))
_l_(465431)
_c_(465434, _a_(465433, _n_(465432, "butW2", lambda: butW2), "pack"))
_l_(465435)
_c_(465438, _a_(465437, _n_(465436, "btn2W2", lambda: btn2W2), "pack"))
_l_(465439)
_c_(465442, _a_(465441, _n_(465440, "win2", lambda: win2), "withdraw"))
_l_(465443)



window=_c_(465446, _a_(465445, _n_(465444, "tk", lambda: tk), "Tk"))
_l_(465447)
_c_(465450, _a_(465449, _n_(465448, "window", lambda: window), "geometry"), '1100x900')
_l_(465451)
_c_(465454, _a_(465453, _n_(465452, "window", lambda: window), "title"), 'Hello World')
_l_(465455)
lab1= _c_(465459, _a_(465457, _n_(465456, "tk", lambda: tk), "Label"), _n_(465458, "window", lambda: window), text='Input the desired delay time')
_l_(465460)
ent=_c_(465464, _a_(465462, _n_(465461, "tk", lambda: tk), "Entry"), _n_(465463, "window", lambda: window))
_l_(465465)
btn=_c_(465470, _a_(465467, _n_(465466, "tk", lambda: tk), "Button"), _n_(465468, "window", lambda: window), text='Go to new window', bg='Blue', command=_n_(465469, "NewTab", lambda: NewTab))
_l_(465471)
btn2=_c_(465476, _a_(465473, _n_(465472, "tk", lambda: tk), "Button"), _n_(465474, "window", lambda: window), text='Leave', bg='Red', command=_n_(465475, "close", lambda: close))
_l_(465477)
###############################################
imgset=_c_(465484, _a_(465479, _n_(465478, "ImageTk", lambda: ImageTk), "PhotoImage"), _c_(465483, _a_(465481, _n_(465480, "Image", lambda: Image), "open"), _n_(465482, "imgpath", lambda: imgpath)))
_l_(465485)
photo = _c_(465489, _a_(465487, _n_(465486, "ImageTk", lambda: ImageTk), "PhotoImage"), _n_(465488, "imgset", lambda: imgset)) 
_l_(465490) 
labimg = _c_(465495, _a_(465492, _n_(465491, "tk", lambda: tk), "Label"), _n_(465493, "window", lambda: window), image=_n_(465494, "photo", lambda: photo))
_l_(465496)
_n_(465497, "labimg", lambda: labimg).image = _n_(465498, "photo", lambda: photo) 
_l_(465499) 
_c_(465502, _a_(465501, _n_(465500, "labimg", lambda: labimg), "pack"))
_l_(465503)
###############################################
_c_(465506, _a_(465505, _n_(465504, "lab1", lambda: lab1), "pack"))
_l_(465507)
_c_(465510, _a_(465509, _n_(465508, "ent", lambda: ent), "pack"))
_l_(465511)
_c_(465514, _a_(465513, _n_(465512, "btn", lambda: btn), "pack"))
_l_(465515)
_c_(465518, _a_(465517, _n_(465516, "btn2", lambda: btn2), "pack"))
_l_(465519)

_c_(465522, _a_(465521, _n_(465520, "window", lambda: window), "mainloop"))
_l_(465523)