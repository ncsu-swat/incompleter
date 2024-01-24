# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37503991/error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(688360)

except ImportError:
    pass
try:
    import requests
    _l_(688362)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(688364)

except ImportError:
    pass

symbolsfile = _c_(688366, _n_(688365, "open", lambda: open), "Stocklist.txt")
_l_(688367)

symbolslist = _c_(688370, _a_(688369, _n_(688368, "symbolsfile", lambda: symbolsfile), "read"))
_l_(688371)

thesymbolslist = _c_(688374, _a_(688373, _n_(688372, "symbolslist", lambda: symbolslist), "split"), "\n")
_l_(688375)

_c_(688378, _n_(688376, "print", lambda: print), _n_(688377, "thesymbolslist", lambda: thesymbolslist))
_l_(688379)


print_lock = _c_(688382, _a_(688381, _n_(688380, "threading", lambda: threading), "Lock"))
_l_(688383)

def th(ur):
    _l_(688409)

    theurl = "http://money.cnn.com/quote/quote.html?symb=" + _n_(688384, "ur", lambda: ur)
    _l_(688385)
    thepage = _c_(688389, _a_(688387, _n_(688386, "requests", lambda: requests), "get"), _n_(688388, "theurl", lambda: theurl))
    _l_(688390)
    soup = _c_(688394, _n_(688391, "BeautifulSoup", lambda: BeautifulSoup), _a_(688393, _n_(688392, "thepage", lambda: thepage), "content"),"html.parser")
    _l_(688395)
    textfind = _c_(688398, _a_(688397, _n_(688396, "soup", lambda: soup), "find"), 'span',{"stream":"last_36276"})
    _l_(688399)
    texttext = _a_(688401, _n_(688400, "textfind", lambda: textfind), "text")
    _l_(688402)
    with _n_(688403, "print_lock", lambda: print_lock):
        _l_(688408)

        _c_(688406, _n_(688404, "print", lambda: print), _n_(688405, "textfind", lambda: textfind))
        _l_(688407)

threadlist = []
_l_(688410)

for u in _n_(688411, "thesymbolslist", lambda: thesymbolslist):
    _l_(688427)

    t = _c_(688416, _a_(688413, _n_(688412, "threading", lambda: threading), "Thread"), target = _n_(688414, "th", lambda: th), args=(_n_(688415, "u", lambda: u),))
    _l_(688417)
    _c_(688420, _a_(688419, _n_(688418, "t", lambda: t), "start"))
    _l_(688421)

    _c_(688425, _a_(688423, _n_(688422, "threadlist", lambda: threadlist), "append"), _n_(688424, "t", lambda: t))
    _l_(688426)

for b in _n_(688428, "threadlist", lambda: threadlist):
    _l_(688433)

    _c_(688431, _a_(688430, _n_(688429, "b", lambda: b), "join"))
    _l_(688432)