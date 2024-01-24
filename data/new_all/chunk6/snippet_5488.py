# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58081123/pdfminer-typeerror-not-all-arguments-converted-during-string-formatting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(360015)

except ImportError:
    pass
try:
    from pdfminer.pdfdocument import PDFDocument
    _l_(360017)

except ImportError:
    pass
try:
    from pdfminer.layout import LTContainer, LTComponent, LTRect, LTLine, LAParams, LTTextLine
    _l_(360019)

except ImportError:
    pass
try:
    from pdfminer.pdfparser import PDFParser
    _l_(360021)

except ImportError:
    pass
try:
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    _l_(360023)

except ImportError:
    pass
try:
    from pdfminer.pdfdevice import PDFDevice, TagExtractor
    _l_(360025)

except ImportError:
    pass
try:
    from pdfminer.pdfpage import PDFPage
    _l_(360027)

except ImportError:
    pass
try:
    from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
    _l_(360029)

except ImportError:
    pass
try:
    from pdfminer.image import ImageWriter
    _l_(360031)

except ImportError:
    pass
try:
    from io import StringIO, BytesIO
    _l_(360033)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(360035)

except ImportError:
    pass
try:
    import re
    _l_(360037)

except ImportError:
    pass
try:
    import io
    _l_(360039)

except ImportError:
    pass



def convert_pdf_to_html(path):
    _l_(360107)

    rsrcmgr = _c_(360041, _n_(360040, "PDFResourceManager", lambda: PDFResourceManager))
    _l_(360042)
    retstr = _c_(360044, _n_(360043, "StringIO", lambda: StringIO))
    _l_(360045)
    outfp = _c_(360047, _n_(360046, "BytesIO", lambda: BytesIO))
    _l_(360048)
    codec = 'utf-8'
    _l_(360049)
    laparams = _c_(360051, _n_(360050, "LAParams", lambda: LAParams))
    _l_(360052)
    device = _c_(360058, _n_(360053, "HTMLConverter", lambda: HTMLConverter), _n_(360054, "rsrcmgr", lambda: rsrcmgr), _n_(360055, "outfp", lambda: outfp), imagewriter=_c_(360057, _n_(360056, "ImageWriter", lambda: ImageWriter), 'out'))
    _l_(360059)
    fp = _c_(360062, _n_(360060, "open", lambda: open), _n_(360061, "path", lambda: path), 'rb')
    _l_(360063)
    interpreter = _c_(360067, _n_(360064, "PDFPageInterpreter", lambda: PDFPageInterpreter), _n_(360065, "rsrcmgr", lambda: rsrcmgr), _n_(360066, "device", lambda: device)) 
    _l_(360068) 
    password = ""
    _l_(360069)
    maxpages = 0 #is for all
    _l_(360070) #is for all
    caching = True
    _l_(360071)
    pagenos=_c_(360073, _n_(360072, "set", lambda: set))
    _l_(360074)
    for page in _c_(360082, _a_(360076, _n_(360075, "PDFPage", lambda: PDFPage), "get_pages"), _n_(360077, "fp", lambda: fp), _n_(360078, "pagenos", lambda: pagenos), maxpages=_n_(360079, "maxpages", lambda: maxpages), password=_n_(360080, "password", lambda: password),caching=_n_(360081, "caching", lambda: caching), check_extractable=True):
        _l_(360088)

        _c_(360086, _a_(360084, _n_(360083, "interpreter", lambda: interpreter), "process_page"), _n_(360085, "page", lambda: page))
        _l_(360087)
    _c_(360091, _a_(360090, _n_(360089, "fp", lambda: fp), "close"))
    _l_(360092)
    _c_(360095, _a_(360094, _n_(360093, "device", lambda: device), "close"))
    _l_(360096)
    str = _c_(360099, _a_(360098, _n_(360097, "retstr", lambda: retstr), "getvalue"))
    _l_(360100)
    _c_(360103, _a_(360102, _n_(360101, "retstr", lambda: retstr), "close"))
    _l_(360104)
    aux = _n_(360105, "str", lambda: str)
    _l_(360106)
    return aux

_c_(360109, _n_(360108, "convert_pdf_to_html", lambda: convert_pdf_to_html), 'PDF - Remraam Ph 1 Mosque.pdf')
_l_(360110)