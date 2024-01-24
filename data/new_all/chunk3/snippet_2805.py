# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62668497/pypdf2-byte-data-vs-binary-data-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
    _l_(553744)

except ImportError:
    pass

file_path = "/file_path/.pdf"
_l_(553745)

input_pdf = _c_(553748, _n_(553746, "PdfFileReader", lambda: PdfFileReader), _n_(553747, "file_path", lambda: file_path))
_l_(553749)
output_file = _c_(553751, _n_(553750, "PdfFileWriter", lambda: PdfFileWriter))
_l_(553752)

cover_page = _c_(553755, _a_(553754, _n_(553753, "input_pdf", lambda: input_pdf), "getPage"), 0)
_l_(553756)
_c_(553760, _a_(553758, _n_(553757, "output_file", lambda: output_file), "addPage"), _n_(553759, "cover_page", lambda: cover_page))
_l_(553761)

with _c_(553763, _n_(553762, "open", lambda: open), "portion.pdf", "wb") as output_file:
    _l_(553769)

    _c_(553767, _a_(553765, _n_(553764, "output_file", lambda: output_file), "write"), _n_(553766, "output_file", lambda: output_file))
    _l_(553768)