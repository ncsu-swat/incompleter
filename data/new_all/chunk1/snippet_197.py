# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72771120/pymupdf-attributeerror-document-object-has-no-attribute-loadpage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fitz
    _l_(411845)

except ImportError:
    pass
# read pdf file
pdf = _c_(411849, _a_(411847, _n_(411846, "fitz", lambda: fitz), "open"), _n_(411848, "file_path_name", lambda: file_path_name))
_l_(411850)
# load pdf page using index
page = _c_(411853, _a_(411852, _n_(411851, "pdf", lambda: pdf), "loadPage"), 0)
_l_(411854)