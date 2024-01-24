# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63841577/attributeerror-module-comtypes-gen-word-has-no-attribute-application-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import filedialog
    _l_(643049)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(643051)

except ImportError:
    pass
try:
    import sys
    _l_(643053)

except ImportError:
    pass
try:
    import os
    _l_(643055)

except ImportError:
    pass
try:
    import comtypes.client
    _l_(643057)

except ImportError:
    pass

window = _c_(643059, _n_(643058, "Tk", lambda: Tk))
_l_(643060)
_c_(643063, _a_(643062, _n_(643061, "window", lambda: window), "geometry"), "300x300")
_l_(643064)
_c_(643067, _a_(643066, _n_(643065, "window", lambda: window), "title"), "Hi")
_l_(643068)

label1 = _c_(643073, _a_(643072, _c_(643071, _n_(643069, "Label", lambda: Label), _n_(643070, "window", lambda: window), text="Hi", font=("arial", 16, "bold")), "pack"))
_l_(643074)


# start of select file button
def select_file():
    _l_(643127)

    _n_(643075, "window", lambda: window).filename = _c_(643078, _a_(643077, _n_(643076, "filedialog", lambda: filedialog), "askopenfilename"), initialdir="/", title="Select file",
                                               filetypes=(("word documents", "*.docx"), ("all files", "*.*")))
    _l_(643079)
    _c_(643083, _n_(643080, "print", lambda: print), _a_(643082, _n_(643081, "window", lambda: window), "filename"))
    _l_(643084)
    _c_(643086, _n_(643085, "print", lambda: print), "work")
    _l_(643087)

    wdFormatPDF = 17
    _l_(643088)

    in_file = _a_(643090, _n_(643089, "window", lambda: window), "filename")
    _l_(643091)
    out_file = _c_(643101, _a_(643094, _a_(643093, _n_(643092, "os", lambda: os), "path"), "join"), _c_(643100, _a_(643097, _a_(643096, _n_(643095, "os", lambda: os), "path"), "join"), _a_(643099, _n_(643098, "os", lambda: os), "environ")['USERPROFILE']), 'Desktop')
    _l_(643102)

    word = _c_(643105, _a_(643104, _a_(643103, comtypes, "client"), "CreateObject"), 'Word.Application')
    _l_(643106)
    doc = _c_(643111, _a_(643109, _a_(643108, _n_(643107, "word", lambda: word), "Documents"), "Open"), _n_(643110, "in_file", lambda: in_file))
    _l_(643112)
    _c_(643117, _a_(643114, _n_(643113, "doc", lambda: doc), "SaveAs"), _n_(643115, "out_file", lambda: out_file), FileFormat=_n_(643116, "wdFormatPDF", lambda: wdFormatPDF))
    _l_(643118)
    _c_(643121, _a_(643120, _n_(643119, "doc", lambda: doc), "Close"))
    _l_(643122)
    _c_(643125, _a_(643124, _n_(643123, "word", lambda: word), "Quit"))
    _l_(643126)


b = _c_(643131, _n_(643128, "Button", lambda: Button), _n_(643129, "window", lambda: window), text="Test", command=_n_(643130, "select_file", lambda: select_file))
_l_(643132)
_c_(643135, _a_(643134, _n_(643133, "b", lambda: b), "pack"))
_l_(643136)
# end of select file button

_c_(643139, _a_(643138, _n_(643137, "window", lambda: window), "mainloop"))
_l_(643140)