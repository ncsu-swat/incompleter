# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62858221/typeerror-pdffilewriter-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
    _l_(706297)

except ImportError:
    pass
pdf_file_path = "oranges.pdf"
_l_(706298)
file_base_name = _c_(706301, _a_(706300, _n_(706299, "pdf_file_path", lambda: pdf_file_path), "replace"), ".pdf","")
_l_(706302)

pdf = _c_(706305, _n_(706303, "PdfFileReader", lambda: PdfFileReader), _n_(706304, "pdf_file_path", lambda: pdf_file_path)) #Creating PDF instance
_l_(706306) #Creating PDF instance
pages = [0,2,4]
_l_(706307)

pdfwriter = _c_(706309, _n_(706308, "PdfFileWriter", lambda: PdfFileWriter)) #Creating pdfWriter instance
_l_(706310) #Creating pdfWriter instance
_n_(706311, "print", lambda: print)
_l_(706312)

for page_num in _n_(706313, "pages", lambda: pages):
    _l_(706323)

    _c_(706321, _a_(706316, _c_(706315, _n_(706314, "pdfwriter", lambda: pdfwriter)), "addPage"), _c_(706320, _a_(706318, _n_(706317, "pdf", lambda: pdf), "getPage"), _n_(706319, "page_num", lambda: page_num)))
    _l_(706322)
with _c_(706328, _n_(706324, "open", lambda: open), _c_(706327, _a_(706325, "{0}_subset", "format"), _n_(706326, "file_base_name", lambda: file_base_name)),'wb') as f:
    _l_(706337)

    _c_(706332, _a_(706330, _n_(706329, "pdfwriter", lambda: pdfwriter), "write"), _n_(706331, "f", lambda: f))
    _l_(706333)
    _a_(706335, _n_(706334, "f", lambda: f), "close")
    _l_(706336)