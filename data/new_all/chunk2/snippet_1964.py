# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74867730/attributeerror-module-bs4-has-no-attribute-beautifulsoup4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests,os,bs4
    _l_(472122)

except ImportError:
    pass
url='http://xkcd.com'
_l_(472123)
_c_(472126, _a_(472125, _n_(472124, "os", lambda: os), "makedirs"), 'xkcd',exist_ok=True)
_l_(472127)
while not _c_(472130, _a_(472129, _n_(472128, "url", lambda: url), "endswith"), '#'):
    _l_(472205)

    _c_(472133, _n_(472131, "print", lambda: print), 'Загружается страница %s...' % _n_(472132, "url", lambda: url))
    _l_(472134)
    res = _c_(472138, _a_(472136, _n_(472135, "requests", lambda: requests), "get"), _n_(472137, "url", lambda: url))
    _l_(472139)
    _c_(472142, _a_(472141, _n_(472140, "res", lambda: res), "raise_for_status"))
    _l_(472143)
    soup = _c_(472148, _a_(472145, _n_(472144, "bs4", lambda: bs4), "BeautifulSoup4"), _a_(472147, _n_(472146, "res", lambda: res), "text"))
    _l_(472149)
    comicElem = _c_(472152, _a_(472151, _n_(472150, "soup", lambda: soup), "select"), '#comic img')
    _l_(472153)
    if _n_(472154, "comicElem", lambda: comicElem) == []:
        _l_(472204)

        _c_(472156, _n_(472155, "print", lambda: print), 'Не удалось найти изображение комиска.')
        _l_(472157)
    else:
        comicUrl = _c_(472160, _a_(472159, _n_(472158, "comicElem", lambda: comicElem)[0], "get"), 'src')
        _l_(472161)
        _c_(472164, _n_(472162, "print", lambda: print), 'Загружается изображение %s...' % _n_(472163, "comicUrl", lambda: (comicUrl)))
        _l_(472165)
        res = _c_(472169, _a_(472167, _n_(472166, "requests", lambda: requests), "get"), _n_(472168, "comicUrl", lambda: comicUrl))
        _l_(472170)
        _c_(472173, _a_(472172, _n_(472171, "res", lambda: res), "raise_for_status"))
        _l_(472174)
        imageFile = _c_(472186, _n_(472175, "open", lambda: open), _c_(472185, _a_(472178, _a_(472177, _n_(472176, "os", lambda: os), "path"), "join"), 'xkcd', _c_(472184, _c_(472182, _a_(472181, _a_(472180, _n_(472179, "os", lambda: os), "path"), "basename")), _n_(472183, "comicUrl", lambda: comicUrl))), 'wb')
        _l_(472187)
        for chunk in _c_(472190, _a_(472189, _n_(472188, "res", lambda: res), "iter_content"), 100000):
            _l_(472195)

            _c_(472193, _a_(472192, _n_(472191, "imageFile", lambda: imageFile), "close"))
            _l_(472194)
        prevLink = _c_(472198, _a_(472197, _n_(472196, "soup", lambda: soup), "select"), 'a[rel]="prev"')[0]
        _l_(472199)
        url = 'http://xkcd.com' + _c_(472202, _a_(472201, _n_(472200, "prevLink", lambda: prevLink), "get"), 'href')
        _l_(472203)
_c_(472207, _n_(472206, "print", lambda: print), 'Готово.')
_l_(472208)