# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59695216/receiving-a-python-typeerror-expected-str-bytes-or-os-pathlike-object-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(648782)

except ImportError:
    pass
try:
    import shutil
    _l_(648784)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(648786)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(648788)

except ImportError:
    pass

def browse_button_1():
    _l_(648794)

    global filePath
    _l_(648789)
    filePath = _c_(648792, _a_(648791, _n_(648790, "filedialog", lambda: filedialog), "askopenfilename"))
    _l_(648793)

def browse_button_2():
    _l_(648800)

    global folder_path
    _l_(648795)
    folderPath = _c_(648798, _a_(648797, _n_(648796, "filedialog", lambda: filedialog), "askdirectory"))
    _l_(648799)

def browse_button_3():
    _l_(648806)

    global destination
    _l_(648801)
    destination = _c_(648804, _a_(648803, _n_(648802, "filedialog", lambda: filedialog), "askdirectory"))
    _l_(648805)

def browse_button_4():
    _l_(648811)

    global run
    _l_(648807)
    run = _c_(648809, _n_(648808, "runScript", lambda: runScript))
    _l_(648810)

root = _c_(648813, _n_(648812, "Tk", lambda: Tk))
_l_(648814)

def runScript():
    _l_(648858)


    filesToFind = []
    _l_(648815)
    with _c_(648820, _n_(648816, "open", lambda: open), _c_(648819, _a_(648818, _n_(648817, "filePath", lambda: filePath), "get")), "r") as fh:
        _l_(648830)

        for row in _n_(648821, "fh", lambda: fh):
            _l_(648829)

            _c_(648827, _a_(648823, _n_(648822, "filesToFind", lambda: filesToFind), "append"), _c_(648826, _a_(648825, _n_(648824, "row", lambda: row), "strip")))
            _l_(648828)

    for filename in _c_(648836, _a_(648832, _n_(648831, "os", lambda: os), "listdir"), _c_(648835, _a_(648834, _n_(648833, "folderPath", lambda: folderPath), "get"))):
        _l_(648857)

        if _n_(648837, "filename", lambda: filename) in _n_(648838, "filesToFind", lambda: filesToFind):
            _l_(648856)

            filename = _c_(648846, _a_(648841, _a_(648840, _n_(648839, "os", lambda: os), "path"), "join"), _c_(648844, _a_(648843, _n_(648842, "folderPath", lambda: folderPath), "get")), _n_(648845, "filename", lambda: filename))
            _l_(648847)
            _c_(648854, _a_(648849, _n_(648848, "shutil", lambda: shutil), "copy"), _n_(648850, "filename", lambda: filename), _c_(648853, _a_(648852, _n_(648851, "destination", lambda: destination), "get")))
            _l_(648855)

filePath = _c_(648860, _n_(648859, "StringVar", lambda: StringVar))
_l_(648861)
lbl1 = _c_(648865, _n_(648862, "Label", lambda: Label), master=_n_(648863, "root", lambda: root),textvariable=_n_(648864, "filePath", lambda: filePath))
_l_(648866)
_c_(648869, _a_(648868, _n_(648867, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(648870)
button2 = _c_(648873, _n_(648871, "Button", lambda: Button), text="Browse Text File", command=_n_(648872, "browse_button_1", lambda: browse_button_1))
_l_(648874)
_c_(648877, _a_(648876, _n_(648875, "button2", lambda: button2), "grid"), row=0, column=3)
_l_(648878)


folderPath = _c_(648880, _n_(648879, "StringVar", lambda: StringVar))
_l_(648881)
lbl1 = _c_(648885, _n_(648882, "Label", lambda: Label), master=_n_(648883, "root", lambda: root),textvariable=_n_(648884, "folderPath", lambda: folderPath))
_l_(648886)
_c_(648889, _a_(648888, _n_(648887, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(648890)
button3 = _c_(648893, _n_(648891, "Button", lambda: Button), text="Browse Source Folder", command=_n_(648892, "browse_button_2", lambda: browse_button_2))
_l_(648894)
_c_(648897, _a_(648896, _n_(648895, "button3", lambda: button3), "grid"), row=0, column=6)
_l_(648898)


destination = _c_(648900, _n_(648899, "StringVar", lambda: StringVar))
_l_(648901)
lbl1 = _c_(648905, _n_(648902, "Label", lambda: Label), master=_n_(648903, "root", lambda: root),textvariable=_n_(648904, "destination", lambda: destination))
_l_(648906)
_c_(648909, _a_(648908, _n_(648907, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(648910)
button4 = _c_(648913, _n_(648911, "Button", lambda: Button), text="Browse Destination Folder", command=_n_(648912, "browse_button_3", lambda: browse_button_3))
_l_(648914)
_c_(648917, _a_(648916, _n_(648915, "button4", lambda: button4), "grid"), row=0, column=9)
_l_(648918)


run = _c_(648920, _n_(648919, "StringVar", lambda: StringVar))
_l_(648921)
lbl1 = _c_(648925, _n_(648922, "Label", lambda: Label), master=_n_(648923, "root", lambda: root),textvariable=_n_(648924, "run", lambda: run))
_l_(648926)
_c_(648929, _a_(648928, _n_(648927, "lbl1", lambda: lbl1), "grid"), row=0, column=1)
_l_(648930)
button5 = _c_(648933, _n_(648931, "Button", lambda: Button), text="Run Script", command=_n_(648932, "runScript", lambda: runScript))
_l_(648934)
_c_(648937, _a_(648936, _n_(648935, "button5", lambda: button5), "grid"), row=0, column=12)
_l_(648938)

_c_(648940, _n_(648939, "mainloop", lambda: mainloop))
_l_(648941)