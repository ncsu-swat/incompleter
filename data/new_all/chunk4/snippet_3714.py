# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69370337/filenotfounderror-errno-2-no-such-file-or-directory-even-though-it-gives-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import PyPDF2
    _l_(581437)

except ImportError:
    pass
try:
    import os
    _l_(581439)

except ImportError:
    pass
try:
    import time
    _l_(581441)

except ImportError:
    pass

#Scan Directory

directory = 'C:\\Users\\Username\\OneDrive\\Desktop\\python'
_l_(581442)
for file in _c_(581446, _a_(581444, _n_(581443, "os", lambda: os), "listdir"), _n_(581445, "directory", lambda: directory)):
    _l_(581496)

    if not _c_(581449, _a_(581448, _n_(581447, "file", lambda: file), "endswith"), ".pdf"):
        _l_(581451)

        continue
        _l_(581450)
    with _c_(581459, _n_(581452, "open", lambda: open), _c_(581458, _a_(581455, _a_(581454, _n_(581453, "os", lambda: os), "path"), "join"), _n_(581456, "directory", lambda: directory),_n_(581457, "file", lambda: file)), 'rb') as pdfFileObj:
        _l_(581495)

        pdfReader = _c_(581463, _a_(581461, _n_(581460, "PyPDF2", lambda: PyPDF2), "PdfFileReader"), _n_(581462, "pdfFileObj", lambda: pdfFileObj))
        _l_(581464)
        pageObj = _c_(581467, _a_(581466, _n_(581465, "pdfReader", lambda: pdfReader), "getPage"), 0)
        _l_(581468)
        text=_c_(581471, _a_(581470, _n_(581469, "pageObj", lambda: pageObj), "extractText"))
        _l_(581472)
        _c_(581475, _n_(581473, "print", lambda: print), "Writing File "+ _n_(581474, "file", lambda: file) +" to TXT.")
        _l_(581476)
        file2=_c_(581481, _n_(581477, "open", lambda: open), r"C:\Users\Username\OneDrive\Desktop\python\\"+_c_(581480, _a_(581479, _n_(581478, "file", lambda: file), "replace"), 'pdf','txt'),"a") #Write as TXT files
        _l_(581482) #Write as TXT files
        _c_(581486, _a_(581484, _n_(581483, "file2", lambda: file2), "writelines"), _n_(581485, "text", lambda: text))
        _l_(581487)
        _c_(581489, _n_(581488, "print", lambda: print), "Done saving.")
        _l_(581490)
        _c_(581493, _a_(581492, _n_(581491, "file2", lambda: file2), "close"))
        _l_(581494)