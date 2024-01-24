# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61909480/filenotfounderror-errno-2-no-such-file-or-directory-but-the-file-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(698922)

except ImportError:
    pass
try:
    import sys
    _l_(698924)

except ImportError:
    pass
try:
    import Pmw
    _l_(698926)

except ImportError:
    pass
try:
    import time
    _l_(698928)

except ImportError:
    pass
try:
    import tkinter as tk
    _l_(698930)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(698932)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(698934)

except ImportError:
    pass

#Def Section
def close():
    _l_(698939)

    _c_(698937, _a_(698936, _n_(698935, "install", lambda: install), "destroy"))
    _l_(698938)

def Policy():
    _l_(698952)

    f= _c_(698943, _n_(698940, "open", lambda: open), _c_(698942, _n_(698941, "Policy", lambda: Policy)))
    _l_(698944)
    _c_(698950, _a_(698946, _n_(698945, "t", lambda: t), "insert"), 1.0, _c_(698949, _a_(698948, _n_(698947, "f", lambda: f), "read")))
    _l_(698951)

#dir_location
dir="~/Scrivania/Healir/Healir/Healir_OS/bin/files/"
_l_(698953)

#file dir_location
Logo_Img = _n_(698954, "dir", lambda: dir) + 'logo.png'
_l_(698955)
Policy = _n_(698956, "dir", lambda: dir) + 'Policy.txt'
_l_(698957)

#gui
install = _c_(698959, _n_(698958, "Tk", lambda: Tk))
_l_(698960)
_c_(698963, _a_(698962, _n_(698961, "install", lambda: install), "title"), 'Healir - Installation')
_l_(698964)
_c_(698967, _a_(698966, _n_(698965, "install", lambda: install), "configure"), bg='#FFF')
_l_(698968)
_c_(698971, _a_(698970, _n_(698969, "install", lambda: install), "attributes"), "-fullscreen", True)
_l_(698972)

#logo
Logo_Canvas = _c_(698975, _n_(698973, "Canvas", lambda: Canvas), _n_(698974, "install", lambda: install), width=100, height=100, bg='#FFF', highlightthickness=0)
_l_(698976)
_c_(698979, _a_(698978, _n_(698977, "Logo_Canvas", lambda: Logo_Canvas), "pack"))
_l_(698980)
Logo_Img = _c_(698983, _n_(698981, "PhotoImage", lambda: PhotoImage), file=_n_(698982, "Logo_Img", lambda: Logo_Img))
_l_(698984)
_c_(698989, _a_(698986, _n_(698985, "Logo_Canvas", lambda: Logo_Canvas), "create_image"), 0, 0, anchor=_n_(698987, "NW", lambda: NW), image=_n_(698988, "Logo_Img", lambda: Logo_Img))
_l_(698990)

#Privacy
Privacy = _c_(698993, _n_(698991, "Label", lambda: Label), _n_(698992, "install", lambda: install), text='Privacy Policy', font='Helvetica 28 bold', fg='#000', bg='#FFF')
_l_(698994)
_c_(698998, _a_(698996, _n_(698995, "Privacy", lambda: Privacy), "config"), anchor=_n_(698997, "CENTER", lambda: CENTER))
_l_(698999)
_c_(699002, _a_(699001, _n_(699000, "Privacy", lambda: Privacy), "pack"))
_l_(699003)

#text
text = _c_(699007, _n_(699004, "Text", lambda: Text), _n_(699005, "install", lambda: install), wrap=_n_(699006, "WORD", lambda: WORD), width=45, height= 20)
_l_(699008)
with _c_(699011, _n_(699009, "open", lambda: open), _n_(699010, "Policy", lambda: Policy), 'r') as f:
    _l_(699020)

    _c_(699018, _a_(699013, _n_(699012, "text", lambda: text), "insert"), _n_(699014, "INSERT", lambda: INSERT), _c_(699017, _a_(699016, _n_(699015, "f", lambda: f), "read")))
    _l_(699019)

_c_(699023, _a_(699022, _n_(699021, "install", lambda: install), "mainloop"))
_l_(699024)