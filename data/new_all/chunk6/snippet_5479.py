# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59204850/python-error-attributeerror-module-string-has-no-attribute-lstrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(347427)

except ImportError:
    pass
try:
    import mechanize
    _l_(347429)

except ImportError:
    pass
try:
    import time
    _l_(347431)

except ImportError:
    pass
try:
    import urllib.request
    _l_(347433)

except ImportError:
    pass
try:
    import string
    _l_(347435)

except ImportError:
    pass


start = "http://www.irrelevantcheetah.com/browserimages.html"# test website 
_l_(347436)# test website 
filetype = _c_(347438, _n_(347437, "input", lambda: input), "What file type are you looking for?\n")
_l_(347439)

br = _c_(347442, _a_(347441, _n_(347440, "mechanize", lambda: mechanize), "Browser"))
_l_(347443)
r = _c_(347447, _a_(347445, _n_(347444, "br", lambda: br), "open"), _n_(347446, "start", lambda: start))
_l_(347448)
html = _c_(347451, _a_(347450, _n_(347449, "r", lambda: r), "read"))
_l_(347452)

soup = _c_(347455, _n_(347453, "BeautifulSoup", lambda: BeautifulSoup), _n_(347454, "html", lambda: html), "html5lib")
_l_(347456)
for link in _c_(347459, _a_(347458, _n_(347457, "soup", lambda: soup), "find_all"), 'a'):
    _l_(347490)

    linkText = _c_(347462, _n_(347460, "str", lambda: str), _n_(347461, "link", lambda: link))
    _l_(347463)
    fileName = _c_(347468, _n_(347464, "str", lambda: str), _c_(347467, _a_(347466, _n_(347465, "link", lambda: link), "get"), 'href'))
    _l_(347469)
    if _n_(347470, "filetype", lambda: filetype) in _n_(347471, "fileName", lambda: fileName):
        _l_(347489)

        image = _c_(347474, _a_(347473, _a_(347472, urllib, "request"), "URLopener"))
        _l_(347475)
        linkGet = "http://www.irrelevantcheetah.com" + _n_(347476, "fileName", lambda: fileName)
        _l_(347477)
        filesave = _c_(347481, _a_(347479, _n_(347478, "string", lambda: string), "lstrip"), _n_(347480, "fileName", lambda: fileName), '/')
        _l_(347482)
        _c_(347487, _a_(347484, _n_(347483, "image", lambda: image), "retrieve"), _n_(347485, "linkGet", lambda: linkGet), _n_(347486, "filesave", lambda: filesave))
        _l_(347488)