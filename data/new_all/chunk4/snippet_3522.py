# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72884714/attributeerror-nonetype-object-has-no-attribute-languages
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import ocrmypdf
    _l_(588187)

except ImportError:
    pass
try:
    import camelot
    _l_(588189)

except ImportError:
    pass
try:
    from tkinter import Tk
    _l_(588191)

except ImportError:
    pass
try:
    from tkinter.filedialog import askopenfilename
    _l_(588193)

except ImportError:
    pass


_c_(588197, _a_(588196, _c_(588195, _n_(588194, "Tk", lambda: Tk)), "withdraw")) # we don't want a full GUI, so keep the root window from appearing
_l_(588198) # we don't want a full GUI, so keep the root window from appearing
filename = _c_(588200, _n_(588199, "askopenfilename", lambda: askopenfilename)) # show an "Open" dialog box and return the path to the selected file
_l_(588201) # show an "Open" dialog box and return the path to the selected file
_c_(588204, _n_(588202, "print", lambda: print), _n_(588203, "filename", lambda: filename))
_l_(588205)

# if filename is not None:
if _n_(588206, "__name__", lambda: __name__) == '__main__':
    _l_(588212)

    _c_(588210, _a_(588208, _n_(588207, "ocrmypdf", lambda: ocrmypdf), "ocr"), _n_(588209, "filename", lambda: filename), 'output.pdf', deskew=True,)
    _l_(588211)

file = "output.pdf"
_l_(588213)
tables = _c_(588217, _a_(588215, _n_(588214, "camelot", lambda: camelot), "read_pdf"), _n_(588216, "file", lambda: file), pages = "1-end", flavor='stream')
_l_(588218)
_c_(588222, _n_(588219, "print", lambda: print), _a_(588221, _n_(588220, "tables", lambda: tables), "n"))
_l_(588223)
tables=_c_(588227, _a_(588225, _n_(588224, "camelot", lambda: camelot), "read_pdf"), _n_(588226, "file", lambda: file), pages='1-end', flavor='stream')
_l_(588228)
_c_(588232, _a_(588230, _n_(588229, "tables", lambda: tables), "export"), _n_(588231, "filename", lambda: filename) + ".xlsx", f='excel')
_l_(588233)