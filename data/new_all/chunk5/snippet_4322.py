# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59695216/receiving-a-python-typeerror-expected-str-bytes-or-os-pathlike-object-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(657547)

except ImportError:
    pass
try:
    import shutil
    _l_(657549)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(657551)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(657553)

except ImportError:
    pass

def browse_button():
    _l_(657558)

    filePath = _c_(657556, _a_(657555, _n_(657554, "filedialog", lambda: filedialog), "askopenfilename"))
    _l_(657557)
def browse_button():
    _l_(657564)

    global folder_path
    _l_(657559)
    folderPath = _c_(657562, _a_(657561, _n_(657560, "filedialog", lambda: filedialog), "askdirectory"))
    _l_(657563)

def browse_button():
    _l_(657570)

    global destination
    _l_(657565)
    destination = _c_(657568, _a_(657567, _n_(657566, "filedialog", lambda: filedialog), "askdirectory"))
    _l_(657569)

root = _c_(657572, _n_(657571, "Tk", lambda: Tk))
_l_(657573)

filePath = _c_(657575, _n_(657574, "StringVar", lambda: StringVar))
_l_(657576)
lbl1 = _c_(657580, _n_(657577, "Label", lambda: Label), master=_n_(657578, "root", lambda: root),textvariable=_n_(657579, "filePath", lambda: filePath))
_l_(657581)
_c_(657584, _a_(657583, _n_(657582, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(657585)
button2 = _c_(657588, _n_(657586, "Button", lambda: Button), text="Browse Text File", command=_n_(657587, "browse_button", lambda: browse_button))
_l_(657589)
_c_(657592, _a_(657591, _n_(657590, "button2", lambda: button2), "grid"), row=0, column=3)
_l_(657593)


folderPath = _c_(657595, _n_(657594, "StringVar", lambda: StringVar))
_l_(657596)
lbl1 = _c_(657600, _n_(657597, "Label", lambda: Label), master=_n_(657598, "root", lambda: root),textvariable=_n_(657599, "folderPath", lambda: folderPath))
_l_(657601)
_c_(657604, _a_(657603, _n_(657602, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(657605)
button2 = _c_(657608, _n_(657606, "Button", lambda: Button), text="Browse Source Folder", command=_n_(657607, "browse_button", lambda: browse_button))
_l_(657609)
_c_(657612, _a_(657611, _n_(657610, "button2", lambda: button2), "grid"), row=0, column=6)
_l_(657613)


destination = _c_(657615, _n_(657614, "StringVar", lambda: StringVar))
_l_(657616)
lbl1 = _c_(657620, _n_(657617, "Label", lambda: Label), master=_n_(657618, "root", lambda: root),textvariable=_n_(657619, "destination", lambda: destination))
_l_(657621)
_c_(657624, _a_(657623, _n_(657622, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(657625)
button2 = _c_(657628, _n_(657626, "Button", lambda: Button), text="Browse Destination Folder", command=_n_(657627, "browse_button", lambda: browse_button))
_l_(657629)
_c_(657632, _a_(657631, _n_(657630, "button2", lambda: button2), "grid"), row=0, column=9)
_l_(657633)
 
filesToFind = []
_l_(657634)
with _c_(657637, _n_(657635, "open", lambda: open), _n_(657636, "filePath", lambda: filePath), "r") as fh:
    _l_(657647)

    for row in _n_(657638, "fh", lambda: fh):
        _l_(657646)

        _c_(657644, _a_(657640, _n_(657639, "filesToFind", lambda: filesToFind), "append"), _c_(657643, _a_(657642, _n_(657641, "row", lambda: row), "strip")))
        _l_(657645)


for filename in _c_(657651, _a_(657649, _n_(657648, "os", lambda: os), "listdir"), _n_(657650, "folderPath", lambda: folderPath)):
    _l_(657668)

    if _n_(657652, "filename", lambda: filename) in _n_(657653, "filesToFind", lambda: filesToFind):
        _l_(657667)

        filename = _c_(657659, _a_(657656, _a_(657655, _n_(657654, "os", lambda: os), "path"), "join"), _n_(657657, "folderPath", lambda: folderPath), _n_(657658, "filename", lambda: filename))
        _l_(657660)
        _c_(657665, _a_(657662, _n_(657661, "shutil", lambda: shutil), "copy"), _n_(657663, "filename", lambda: filename), _n_(657664, "destination", lambda: destination))
        _l_(657666)

_c_(657670, _n_(657669, "mainloop", lambda: mainloop))
_l_(657671)