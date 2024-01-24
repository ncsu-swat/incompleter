# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37503991/error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(659170)

except ImportError:
    pass
try:
    import requests
    _l_(659172)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(659174)

except ImportError:
    pass

symbolsfile = _c_(659176, _n_(659175, "open", lambda: open), "Stocklist.txt")
_l_(659177)

symbolslist = _c_(659180, _a_(659179, _n_(659178, "symbolsfile", lambda: symbolsfile), "read"))
_l_(659181)

thesymbolslist = _c_(659184, _a_(659183, _n_(659182, "symbolslist", lambda: symbolslist), "split"), "\n")
_l_(659185)

_c_(659188, _n_(659186, "print", lambda: print), _n_(659187, "thesymbolslist", lambda: thesymbolslist))
_l_(659189)


print_lock = _c_(659192, _a_(659191, _n_(659190, "threading", lambda: threading), "Lock"))
_l_(659193)

def th(ur):
    _l_(659219)

    theurl = "http://money.cnn.com/quote/quote.html?symb=" + _n_(659194, "ur", lambda: ur)
    _l_(659195)
    thepage = _c_(659199, _a_(659197, _n_(659196, "requests", lambda: requests), "get"), _n_(659198, "theurl", lambda: theurl))
    _l_(659200)
    soup = _c_(659204, _n_(659201, "BeautifulSoup", lambda: BeautifulSoup), _a_(659203, _n_(659202, "thepage", lambda: thepage), "content"),"html.parser")
    _l_(659205)
    textfind = _c_(659208, _a_(659207, _n_(659206, "soup", lambda: soup), "find"), 'span',{"stream":"last_36276"})
    _l_(659209)
    texttext = _a_(659211, _n_(659210, "textfind", lambda: textfind), "text")
    _l_(659212)
    with _n_(659213, "print_lock", lambda: print_lock):
        _l_(659218)

        _c_(659216, _n_(659214, "print", lambda: print), _n_(659215, "textfind", lambda: textfind))
        _l_(659217)

threadlist = []
_l_(659220)

for u in _n_(659221, "thesymbolslist", lambda: thesymbolslist):
    _l_(659237)

    t = _c_(659226, _a_(659223, _n_(659222, "threading", lambda: threading), "Thread"), target = _n_(659224, "th", lambda: th), args=(_n_(659225, "u", lambda: u),))
    _l_(659227)
    _c_(659230, _a_(659229, _n_(659228, "t", lambda: t), "start"))
    _l_(659231)

    _c_(659235, _a_(659233, _n_(659232, "threadlist", lambda: threadlist), "append"), _n_(659234, "t", lambda: t))
    _l_(659236)

for b in _n_(659238, "threadlist", lambda: threadlist):
    _l_(659243)

    _c_(659241, _a_(659240, _n_(659239, "b", lambda: b), "join"))
    _l_(659242)