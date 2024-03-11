# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72585255/os-rename-error-the-system-cannot-move-the-file-to-a-different-disk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(414875)

except ImportError:
    pass
try:
    import tkinter.filedialog
    _l_(414877)

except ImportError:
    pass
try:
    import os
    _l_(414879)

except ImportError:
    pass
try:
    import pathlib
    _l_(414881)

except ImportError:
    pass

window=_c_(414883, _n_(414882, "Tk", lambda: Tk))
_l_(414884)
_c_(414887, _a_(414886, _n_(414885, "window", lambda: window), "title"), 'Hello Python')
_l_(414888)
_c_(414891, _a_(414890, _n_(414889, "window", lambda: window), "geometry"), "300x200+10+10")
_l_(414892)
_c_(414895, _a_(414894, _n_(414893, "window", lambda: window), "resizable"), False, False)
_l_(414896)
_c_(414899, _a_(414898, _n_(414897, "window", lambda: window), "configure"), bg='white')
_l_(414900)

brackets = False
_l_(414901)

def rename():
    _l_(414945)

    fileNumber = 1
    _l_(414902)
    folderPath = _c_(414906, _a_(414904, _a_(414903, tkinter, "filedialog"), "askdirectory"), parent=_n_(414905, "window", lambda: window), initialdir='Documents', title='Please select a folder')
    _l_(414907)
    for filename in _c_(414911, _a_(414909, _n_(414908, "os", lambda: os), "listdir"), _n_(414910, "folderPath", lambda: folderPath)):
        _l_(414944)

        fileExt = _a_(414916, _c_(414915, _a_(414913, _n_(414912, "pathlib", lambda: pathlib), "Path"), _n_(414914, "filename", lambda: filename)), "suffix")
        _l_(414917)
        filePath = _n_(414918, "folderPath", lambda: folderPath) + '/' + _n_(414919, "filename", lambda: filename)
        _l_(414920)
        if (_n_(414921, "fileExt", lambda: fileExt) != '.py') :
            _l_(414943)

            if _n_(414922, "brackets", lambda: (brackets)):
                _l_(414941)

                _c_(414930, _a_(414924, _n_(414923, "os", lambda: os), "rename"), _n_(414925, "filePath", lambda: filePath), _c_(414928, _n_(414926, "str", lambda: str), _n_(414927, "fileNumber", lambda: fileNumber)) + ')' + _n_(414929, "fileExt", lambda: fileExt))
                _l_(414931)
            else:
                _c_(414939, _a_(414933, _n_(414932, "os", lambda: os), "rename"), _n_(414934, "filePath", lambda: filePath), _c_(414937, _n_(414935, "str", lambda: str), _n_(414936, "fileNumber", lambda: fileNumber)) + _n_(414938, "fileExt", lambda: fileExt))
                _l_(414940)
            fileNumber += 1
            _l_(414942)

lbl=_c_(414948, _n_(414946, "Label", lambda: Label), _n_(414947, "window", lambda: window), text="Welcome to rename it!", fg='black', bg='white', font=("Helvetica", 20))
_l_(414949)
_c_(414953, _a_(414951, _n_(414950, "lbl", lambda: lbl), "place"), relx = 0.5, y = 25, anchor=_n_(414952, "CENTER", lambda: CENTER))
_l_(414954)

btn=_c_(414958, _n_(414955, "Button", lambda: Button), _n_(414956, "window", lambda: window), text="Rename", fg='blue', command=_n_(414957, "rename", lambda: rename))
_l_(414959)
_c_(414962, _a_(414961, _n_(414960, "btn", lambda: btn), "place"), x=80, y=100)
_l_(414963)

_c_(414966, _a_(414965, _n_(414964, "window", lambda: window), "mainloop"))
_l_(414967)