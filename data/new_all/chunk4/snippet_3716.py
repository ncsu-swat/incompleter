# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69370337/filenotfounderror-errno-2-no-such-file-or-directory-even-though-it-gives-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import PyPDF2
    _l_(632899)

except ImportError:
    pass
try:
    import os
    _l_(632901)

except ImportError:
    pass
try:
    import time
    _l_(632903)

except ImportError:
    pass

#Scan Directory

directory = 'C:\\Users\\Username\\OneDrive\\Desktop\\python'
_l_(632904)
for file in _c_(632908, _a_(632906, _n_(632905, "os", lambda: os), "listdir"), _n_(632907, "directory", lambda: directory)):
    _l_(632958)

    if not _c_(632911, _a_(632910, _n_(632909, "file", lambda: file), "endswith"), ".pdf"):
        _l_(632913)

        continue
        _l_(632912)
    with _c_(632921, _n_(632914, "open", lambda: open), _c_(632920, _a_(632917, _a_(632916, _n_(632915, "os", lambda: os), "path"), "join"), _n_(632918, "directory", lambda: directory),_n_(632919, "file", lambda: file)), 'rb') as pdfFileObj:
        _l_(632957)

        pdfReader = _c_(632925, _a_(632923, _n_(632922, "PyPDF2", lambda: PyPDF2), "PdfFileReader"), _n_(632924, "pdfFileObj", lambda: pdfFileObj))
        _l_(632926)
        pageObj = _c_(632929, _a_(632928, _n_(632927, "pdfReader", lambda: pdfReader), "getPage"), 0)
        _l_(632930)
        text=_c_(632933, _a_(632932, _n_(632931, "pageObj", lambda: pageObj), "extractText"))
        _l_(632934)
        _c_(632937, _n_(632935, "print", lambda: print), "Writing File "+ _n_(632936, "file", lambda: file) +" to TXT.")
        _l_(632938)
        file2=_c_(632943, _n_(632939, "open", lambda: open), r"C:\Users\Username\OneDrive\Desktop\python\\"+_c_(632942, _a_(632941, _n_(632940, "file", lambda: file), "replace"), 'pdf','txt'),"a") #Write as TXT files
        _l_(632944) #Write as TXT files
        _c_(632948, _a_(632946, _n_(632945, "file2", lambda: file2), "writelines"), _n_(632947, "text", lambda: text))
        _l_(632949)
        _c_(632951, _n_(632950, "print", lambda: print), "Done saving.")
        _l_(632952)
        _c_(632955, _a_(632954, _n_(632953, "file2", lambda: file2), "close"))
        _l_(632956)