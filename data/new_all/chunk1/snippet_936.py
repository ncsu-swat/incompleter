# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/17270387/pypdf2-typeerror-when-trying-to-extract-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filename = "myfile.pdf"
_l_(402740)
f = _c_(402743, _n_(402741, "open", lambda: open), _n_(402742, "filename", lambda: filename),'rb')
_l_(402744)
mypdf = _c_(402747, _n_(402745, "PdfFileReader", lambda: PdfFileReader), _n_(402746, "f", lambda: f))
_l_(402748)
_c_(402755, _n_(402749, "print", lambda: print), _n_(402750, "f", lambda: f),_n_(402751, "mypdf", lambda: mypdf),_c_(402754, _a_(402753, _n_(402752, "mypdf", lambda: mypdf), "getNumPages")))
_l_(402756)
_c_(402763, _n_(402757, "print", lambda: print), _c_(402762, _a_(402761, _c_(402760, _a_(402759, _n_(402758, "mypdf", lambda: mypdf), "getPage"), 0), "extractText")))
_l_(402764)