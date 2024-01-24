# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34117236/filenotfounderror-errno-2-in-joining-the-file-directories
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests,os,bs4
    _l_(544080)

except ImportError:
    pass
# Download the page.
_c_(544082, _n_(544081, "print", lambda: print), 'Downloading page...')
_l_(544083)
res=_c_(544086, _a_(544085, _n_(544084, "requests", lambda: requests), "get"), 'https://imgur.com/search?q=cute+dog')
_l_(544087)
_c_(544090, _a_(544089, _n_(544088, "res", lambda: res), "raise_for_status"))
_l_(544091)

soup=_c_(544096, _a_(544093, _n_(544092, "bs4", lambda: bs4), "BeautifulSoup"), _a_(544095, _n_(544094, "res", lambda: res), "text"),"html.parser")
_l_(544097)

# Find the URL of the image.
comicElem=_c_(544100, _a_(544099, _n_(544098, "soup", lambda: soup), "select"), '#imagelist img')
_l_(544101)
for i in _c_(544103, _n_(544102, "range", lambda: range), 10):
    _l_(544147)

    comicUrl=_c_(544107, _a_(544106, _n_(544104, "comicElem", lambda: comicElem)[_n_(544105, "i", lambda: i)], "get"), 'src')
    _l_(544108)
    # Download the image.
    _c_(544111, _n_(544109, "print", lambda: print), 'Downloading image %s...' %_n_(544110, "comicUrl", lambda: (comicUrl)))
    _l_(544112)
    res=_c_(544116, _a_(544114, _n_(544113, "requests", lambda: requests), "get"), 'https:'+_n_(544115, "comicUrl", lambda: comicUrl))
    _l_(544117)
    _c_(544120, _a_(544119, _n_(544118, "res", lambda: res), "raise_for_status"))
    _l_(544121)
    # Save the image to f:\\images
    imageFile=_c_(544132, _n_(544122, "open", lambda: open), _c_(544131, _a_(544125, _a_(544124, _n_(544123, "os", lambda: os), "path"), "join"), 'f:\\image',_c_(544130, _a_(544128, _a_(544127, _n_(544126, "os", lambda: os), "path"), "basename"), _n_(544129, "comicUrl", lambda: comicUrl))),'wb')
    _l_(544133)
    for chunk in _c_(544136, _a_(544135, _n_(544134, "res", lambda: res), "iter_content"), 100000):
        _l_(544142)

        _c_(544140, _a_(544138, _n_(544137, "imageFile", lambda: imageFile), "write"), _n_(544139, "chunk", lambda: chunk))
        _l_(544141)
    _c_(544145, _a_(544144, _n_(544143, "imageFile", lambda: imageFile), "close"))
    _l_(544146)