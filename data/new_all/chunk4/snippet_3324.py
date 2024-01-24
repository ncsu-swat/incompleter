# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75664440/attributeerror-nonetype-object-has-no-attribute-get-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pdf_reader = _c_(614684, _a_(614682, _n_(614681, "pypdf", lambda: pypdf), "PdfReader"), _n_(614683, "file_path", lambda: file_path), strict=False)
_l_(614685)
_c_(614689, _n_(614686, "print", lambda: print), _a_(614688, _n_(614687, "pdf_reader", lambda: pdf_reader), "trailer")['/Root']['/Pages']) 
_l_(614690) 