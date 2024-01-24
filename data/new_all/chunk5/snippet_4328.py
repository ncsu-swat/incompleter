# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59564096/typeerror-in-gui-tkinter-ask-stablelvl-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tkinter as tk
    _l_(677634)

except ImportError:
    pass
try:
    import tkinter.messagebox
    _l_(677636)

except ImportError:
    pass
try:
    from PIL import Image, ImageTk
    _l_(677638)

except ImportError:
    pass
try:
    from tkinter.filedialog import askopenfile
    _l_(677640)

except ImportError:
    pass

root3 = _c_(677643, _a_(677642, _n_(677641, "tk", lambda: tk), "Tk"))
_l_(677644)
_c_(677647, _a_(677646, _n_(677645, "root3", lambda: root3), "geometry"), '200x300') 
_l_(677648) 
info2=_c_(677652, _a_(677650, _n_(677649, "tk", lambda: tk), "Label"), _n_(677651, "root3", lambda: root3),text='Enter index of last head value before initiation slug test',anchor='e')
_l_(677653)
_c_(677656, _a_(677655, _n_(677654, "info2", lambda: info2), "pack"))
_l_(677657)

#Parameter
par = ('Index of stable level')
_l_(677658)
def ask_stableLvl(enter):
    _l_(677670)

    global stableLvl
    _l_(677659)
    stableLvl =  _c_(677664, _n_(677660, "float", lambda: float), _c_(677663, _a_(677662, _n_(677661, "enter", lambda: enter)['Index of stable level'], "get"))) 
    _l_(677665) 
    _c_(677668, _n_(677666, "print", lambda: print), _n_(677667, "stableLvl", lambda: stableLvl))
    _l_(677669)
#stableLvl = int(input('Enter index of last head value before initiation slug test: '))
def fill(stableLvl):
    _l_(677718)

    dic = {}
    _l_(677671)
    row2 = _c_(677675, _a_(677673, _n_(677672, "tk", lambda: tk), "Frame"), _n_(677674, "root3", lambda: root3))
    _l_(677676)
    lab2 = _c_(677681, _a_(677678, _n_(677677, "tk", lambda: tk), "Label"), _n_(677679, "row2", lambda: row2), width=15, text=_n_(677680, "stableLvl", lambda: stableLvl), anchor='w')
    _l_(677682)
    ent2 = _c_(677686, _a_(677684, _n_(677683, "tk", lambda: tk), "Entry"), _n_(677685, "row2", lambda: row2))      
    _l_(677687)      
    _c_(677694, _a_(677689, _n_(677688, "row2", lambda: row2), "pack"), side=_a_(677691, _n_(677690, "tk", lambda: tk), "TOP"),fill=_a_(677693, _n_(677692, "tk", lambda: tk), "X"),padx=2,pady=2)
    _l_(677695)
    _c_(677700, _a_(677697, _n_(677696, "lab2", lambda: lab2), "pack"), side=_a_(677699, _n_(677698, "tk", lambda: tk), "LEFT"))
    _l_(677701)
    _c_(677710, _a_(677703, _n_(677702, "ent2", lambda: ent2), "pack"), side=_a_(677705, _n_(677704, "tk", lambda: tk), "RIGHT"), expand=_a_(677707, _n_(677706, "tk", lambda: tk), "YES"),fill=_a_(677709, _n_(677708, "tk", lambda: tk), "X"))
    _l_(677711)
    _n_(677712, "dic", lambda: dic)[_n_(677713, "stableLvl", lambda: stableLvl)] = _n_(677714, "ent2", lambda: ent2)
    _l_(677715)
    aux = _n_(677716, "dic", lambda: dic)
    _l_(677717)
    return aux
#
if _n_(677719, "__name__", lambda: __name__) == '__main__':
    _l_(677724)

    ent2 = _c_(677722, _n_(677720, "fill", lambda: fill), _n_(677721, "stableLvl", lambda: stableLvl))
    _l_(677723)
save_button = _c_(677728, _a_(677726, _n_(677725, "tk", lambda: tk), "Button"), _n_(677727, "root3", lambda: root3))
_l_(677729)
_c_(677734, _a_(677731, _n_(677730, "save_button", lambda: save_button), "configure"), text='Save', command=_c_(677733, _n_(677732, "ask_stableLvl", lambda: ask_stableLvl)))
_l_(677735)
_c_(677738, _a_(677737, _n_(677736, "save_button", lambda: save_button), "pack"))
_l_(677739)
_c_(677742, _a_(677741, _n_(677740, "root3", lambda: root3), "mainloop"))
_l_(677743)