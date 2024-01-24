# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48848465/web-scraping-pdf-using-url-python-3-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4 as bs
    _l_(576593)

except ImportError:
    pass
try:
    import urllib.request
    _l_(576595)

except ImportError:
    pass
try:
    from urllib.request import urlopen
    _l_(576597)

except ImportError:
    pass
try:
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    _l_(576599)

except ImportError:
    pass
try:
    from pdfminer.converter import TextConverter
    _l_(576601)

except ImportError:
    pass
try:
    from pdfminer.pdfpage import PDFPage
    _l_(576603)

except ImportError:
    pass
try:
    from pdfminer.layout import LAParams
    _l_(576605)

except ImportError:
    pass
try:
    from io import StringIO
    _l_(576607)

except ImportError:
    pass
try:
    from io import open
    _l_(576609)

except ImportError:
    pass

def convert_pdf_to_txt(path):
    _l_(576674)

    rsrcmgr = _c_(576611, _n_(576610, "PDFResourceManager", lambda: PDFResourceManager))
    _l_(576612)
    retstr = _c_(576614, _n_(576613, "StringIO", lambda: StringIO))
    _l_(576615)
    codec = 'utf-8'
    _l_(576616)
    laparams = _c_(576618, _n_(576617, "LAParams", lambda: LAParams))
    _l_(576619)
    device = _c_(576625, _n_(576620, "TextConverter", lambda: TextConverter), _n_(576621, "rsrcmgr", lambda: rsrcmgr), _n_(576622, "retstr", lambda: retstr), codec=_n_(576623, "codec", lambda: codec), laparams=_n_(576624, "laparams", lambda: laparams))
    _l_(576626)
    fp = _c_(576629, _n_(576627, "open", lambda: open), _n_(576628, "path", lambda: path), 'rb')
    _l_(576630)
    interpreter = _c_(576634, _n_(576631, "PDFPageInterpreter", lambda: PDFPageInterpreter), _n_(576632, "rsrcmgr", lambda: rsrcmgr), _n_(576633, "device", lambda: device))
    _l_(576635)
    password = ""
    _l_(576636)
    maxpages = 0
    _l_(576637)
    caching = True
    _l_(576638)
    pagenos=_c_(576640, _n_(576639, "set", lambda: set))
    _l_(576641)
    for page in _c_(576649, _a_(576643, _n_(576642, "PDFPage", lambda: PDFPage), "get_pages"), _n_(576644, "fp", lambda: fp), _n_(576645, "pagenos", lambda: pagenos), maxpages=_n_(576646, "maxpages", lambda: maxpages), password=_n_(576647, "password", lambda: password),caching=_n_(576648, "caching", lambda: caching), check_extractable=True):
        _l_(576655)

        _c_(576653, _a_(576651, _n_(576650, "interpreter", lambda: interpreter), "process_page"), _n_(576652, "page", lambda: page))
        _l_(576654)
    _c_(576658, _a_(576657, _n_(576656, "fp", lambda: fp), "close"))
    _l_(576659)
    _c_(576662, _a_(576661, _n_(576660, "device", lambda: device), "close"))
    _l_(576663)
    stri = _c_(576666, _a_(576665, _n_(576664, "retstr", lambda: retstr), "getvalue"))
    _l_(576667)
    _c_(576670, _a_(576669, _n_(576668, "retstr", lambda: retstr), "close"))
    _l_(576671)
    aux = _n_(576672, "stri", lambda: stri)
    _l_(576673)
    return aux

pdfFile = _c_(576676, _n_(576675, "urlopen", lambda: urlopen), "http://pythonscraping.com/pages/warandpeace/chapter1.pdf");
_l_(576677)
outputString = _c_(576680, _n_(576678, "convert_pdf_to_txt", lambda: convert_pdf_to_txt), _n_(576679, "pdfFile", lambda: pdfFile))
_l_(576681)

_c_(576684, _n_(576682, "print", lambda: print), _n_(576683, "outputString", lambda: outputString))
_l_(576685)
_c_(576688, _a_(576687, _n_(576686, "pdfFile", lambda: pdfFile), "close"))
_l_(576689)