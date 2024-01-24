# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63841577/attributeerror-module-comtypes-gen-word-has-no-attribute-application-when
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import filedialog
    _l_(596481)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(596483)

except ImportError:
    pass
try:
    import sys
    _l_(596485)

except ImportError:
    pass
try:
    import os
    _l_(596487)

except ImportError:
    pass
try:
    import comtypes.client
    _l_(596489)

except ImportError:
    pass

window = _c_(596491, _n_(596490, "Tk", lambda: Tk))
_l_(596492)
_c_(596495, _a_(596494, _n_(596493, "window", lambda: window), "geometry"), "300x300")
_l_(596496)
_c_(596499, _a_(596498, _n_(596497, "window", lambda: window), "title"), "Hi")
_l_(596500)

label1 = _c_(596505, _a_(596504, _c_(596503, _n_(596501, "Label", lambda: Label), _n_(596502, "window", lambda: window), text="Hi", font=("arial", 16, "bold")), "pack"))
_l_(596506)


# start of select file button
def select_file():
    _l_(596559)

    _n_(596507, "window", lambda: window).filename = _c_(596510, _a_(596509, _n_(596508, "filedialog", lambda: filedialog), "askopenfilename"), initialdir="/", title="Select file",
                                               filetypes=(("word documents", "*.docx"), ("all files", "*.*")))
    _l_(596511)
    _c_(596515, _n_(596512, "print", lambda: print), _a_(596514, _n_(596513, "window", lambda: window), "filename"))
    _l_(596516)
    _c_(596518, _n_(596517, "print", lambda: print), "work")
    _l_(596519)

    wdFormatPDF = 17
    _l_(596520)

    in_file = _a_(596522, _n_(596521, "window", lambda: window), "filename")
    _l_(596523)
    out_file = _c_(596533, _a_(596526, _a_(596525, _n_(596524, "os", lambda: os), "path"), "join"), _c_(596532, _a_(596529, _a_(596528, _n_(596527, "os", lambda: os), "path"), "join"), _a_(596531, _n_(596530, "os", lambda: os), "environ")['USERPROFILE']), 'Desktop')
    _l_(596534)

    word = _c_(596537, _a_(596536, _a_(596535, comtypes, "client"), "CreateObject"), 'Word.Application')
    _l_(596538)
    doc = _c_(596543, _a_(596541, _a_(596540, _n_(596539, "word", lambda: word), "Documents"), "Open"), _n_(596542, "in_file", lambda: in_file))
    _l_(596544)
    _c_(596549, _a_(596546, _n_(596545, "doc", lambda: doc), "SaveAs"), _n_(596547, "out_file", lambda: out_file), FileFormat=_n_(596548, "wdFormatPDF", lambda: wdFormatPDF))
    _l_(596550)
    _c_(596553, _a_(596552, _n_(596551, "doc", lambda: doc), "Close"))
    _l_(596554)
    _c_(596557, _a_(596556, _n_(596555, "word", lambda: word), "Quit"))
    _l_(596558)


b = _c_(596563, _n_(596560, "Button", lambda: Button), _n_(596561, "window", lambda: window), text="Test", command=_n_(596562, "select_file", lambda: select_file))
_l_(596564)
_c_(596567, _a_(596566, _n_(596565, "b", lambda: b), "pack"))
_l_(596568)
# end of select file button

_c_(596571, _a_(596570, _n_(596569, "window", lambda: window), "mainloop"))
_l_(596572)