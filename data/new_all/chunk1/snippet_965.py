# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63758519/why-do-i-receive-this-error-in-python-pdfminer-typeerror-can-only-concatenate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pdfminer.layout import LAParams
    _l_(394032)

except ImportError:
    pass
try:
    from pdfminer.converter import TextConverter
    _l_(394034)

except ImportError:
    pass
try:
    from io import StringIO
    _l_(394036)

except ImportError:
    pass
try:
    from pdfminer.pdfpage import PDFPage
    _l_(394038)

except ImportError:
    pass

def get_pdf_file_content(path_to_pdf):
    _l_(394092)

    resource_manager = _c_(394040, _n_(394039, "PDFResourceManager", lambda: PDFResourceManager), caching=True)
    _l_(394041)
    out_text = _n_(394042, "StringIO", lambda: StringIO)
    _l_(394043)
    laParams = _c_(394045, _n_(394044, "LAParams", lambda: LAParams))
    _l_(394046)
    text_converter = _c_(394051, _n_(394047, "TextConverter", lambda: TextConverter), _n_(394048, "resource_manager", lambda: resource_manager), _n_(394049, "out_text", lambda: out_text), laparams= _n_(394050, "laParams", lambda: laParams))
    _l_(394052)
    fp = _c_(394055, _n_(394053, "open", lambda: open), _n_(394054, "path_to_pdf", lambda: path_to_pdf), 'rb')
    _l_(394056)
    interpreter = _c_(394060, _n_(394057, "PDFPageInterpreter", lambda: PDFPageInterpreter), _n_(394058, "resource_manager", lambda: resource_manager), _n_(394059, "text_converter", lambda: text_converter))
    _l_(394061)
    for page in _c_(394067, _a_(394063, _n_(394062, "PDFPage", lambda: PDFPage), "get_pages"), _n_(394064, "fp", lambda: fp), pagenos=_c_(394066, _n_(394065, "set", lambda: set)), maxpages=0, password="", caching= True, check_extractable= True):
        _l_(394073)

        _c_(394071, _a_(394069, _n_(394068, "interpreter", lambda: interpreter), "process_page"), _n_(394070, "page", lambda: page))
        _l_(394072)

    text = _c_(394076, _a_(394075, _n_(394074, "out_text", lambda: out_text), "getvalue"))
    _l_(394077)

    _c_(394080, _a_(394079, _n_(394078, "fp", lambda: fp), "close"))
    _l_(394081)
    _c_(394084, _a_(394083, _n_(394082, "text_converter", lambda: text_converter), "close"))
    _l_(394085)
    _c_(394088, _a_(394087, _n_(394086, "out_text", lambda: out_text), "close"))
    _l_(394089)
    aux = _n_(394090, "text", lambda: text)
    _l_(394091)

    return aux

path_to_pdf = "C:\\files\\raw\\AZO - CALLSTREET REPORT  AutoZone, Inc.(AZO), Q1 2002 Earnings Call, 5-December-2001 10 00 AM ET - 05-Dec-01.pdf"
_l_(394093)
_c_(394098, _n_(394094, "print", lambda: print), _c_(394097, _n_(394095, "get_pdf_file_content", lambda: get_pdf_file_content), _n_(394096, "path_to_pdf", lambda: path_to_pdf)))
_l_(394099)