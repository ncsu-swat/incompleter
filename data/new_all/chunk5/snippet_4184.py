# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61909480/filenotfounderror-errno-2-no-such-file-or-directory-but-the-file-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(703113)

except ImportError:
    pass
try:
    import sys
    _l_(703115)

except ImportError:
    pass
try:
    import Pmw
    _l_(703117)

except ImportError:
    pass
try:
    import time
    _l_(703119)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(703121)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(703123)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(703125)

except ImportError:
    pass

#Def Section
def close():
    _l_(703130)

    _c_(703128, _a_(703127, _n_(703126, "install", lambda: install), "destroy"))
    _l_(703129)

def Policy():
    _l_(703143)

    f= _c_(703134, _n_(703131, "open", lambda: open), _c_(703133, _n_(703132, "Policy", lambda: Policy)))
    _l_(703135)
    _c_(703141, _a_(703137, _n_(703136, "t", lambda: t), "insert"), 1.0, _c_(703140, _a_(703139, _n_(703138, "f", lambda: f), "read")))
    _l_(703142)

#dir_location
dir="~/Scrivania/Healir/Healir/Healir_OS/bin/files/"
_l_(703144)

#file dir_location
Logo_Img = _n_(703145, "dir", lambda: dir) + 'logo.png'
_l_(703146)
Policy = _n_(703147, "dir", lambda: dir) + 'Policy.txt'
_l_(703148)

#gui
install = _c_(703150, _n_(703149, "Tk", lambda: Tk))
_l_(703151)
_c_(703154, _a_(703153, _n_(703152, "install", lambda: install), "title"), 'Healir - Installation')
_l_(703155)
_c_(703158, _a_(703157, _n_(703156, "install", lambda: install), "configure"), bg='#FFF')
_l_(703159)
_c_(703162, _a_(703161, _n_(703160, "install", lambda: install), "attributes"), "-fullscreen", True)
_l_(703163)

#logo
Logo_Canvas = _c_(703166, _n_(703164, "Canvas", lambda: Canvas), _n_(703165, "install", lambda: install), width=100, height=100, bg='#FFF', highlightthickness=0)
_l_(703167)
_c_(703170, _a_(703169, _n_(703168, "Logo_Canvas", lambda: Logo_Canvas), "pack"))
_l_(703171)
Logo_Img = _c_(703174, _n_(703172, "PhotoImage", lambda: PhotoImage), file=_n_(703173, "Logo_Img", lambda: Logo_Img))
_l_(703175)
_c_(703180, _a_(703177, _n_(703176, "Logo_Canvas", lambda: Logo_Canvas), "create_image"), 0, 0, anchor=_n_(703178, "NW", lambda: NW), image=_n_(703179, "Logo_Img", lambda: Logo_Img))
_l_(703181)

#Privacy
Privacy = _c_(703184, _n_(703182, "Label", lambda: Label), _n_(703183, "install", lambda: install), text='Privacy Policy', font='Helvetica 28 bold', fg='#000', bg='#FFF')
_l_(703185)
_c_(703189, _a_(703187, _n_(703186, "Privacy", lambda: Privacy), "config"), anchor=_n_(703188, "CENTER", lambda: CENTER))
_l_(703190)
_c_(703193, _a_(703192, _n_(703191, "Privacy", lambda: Privacy), "pack"))
_l_(703194)

#text
text = _c_(703198, _n_(703195, "Text", lambda: Text), _n_(703196, "install", lambda: install), wrap=_n_(703197, "WORD", lambda: WORD), width=45, height= 20)
_l_(703199)
with _c_(703202, _n_(703200, "open", lambda: open), _n_(703201, "Policy", lambda: Policy), 'r') as f:
    _l_(703211)

    _c_(703209, _a_(703204, _n_(703203, "text", lambda: text), "insert"), _n_(703205, "INSERT", lambda: INSERT), _c_(703208, _a_(703207, _n_(703206, "f", lambda: f), "read")))
    _l_(703210)

_c_(703214, _a_(703213, _n_(703212, "install", lambda: install), "mainloop"))
_l_(703215)