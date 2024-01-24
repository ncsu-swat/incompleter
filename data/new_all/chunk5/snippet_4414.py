# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58086807/typeerror-object-of-type-nonetype-has-no-len-on-python-3-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from variables import MY_URL , OUT_FILE
    _l_(680327)

except ImportError:
    pass
try:
    import requests
    _l_(680329)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as soup
    _l_(680331)

except ImportError:
    pass
try:
    from urllib.request import urlopen as ureq
    _l_(680333)

except ImportError:
    pass
try:
    import ssl
    _l_(680335)

except ImportError:
    pass

_n_(680336, "ssl", lambda: ssl)._create_default_https_context = _a_(680338, _n_(680337, "ssl", lambda: ssl), "_create_unverified_context")
_l_(680339)
try:
    import csv
    _l_(680341)

except ImportError:
    pass

def agarrar_pagina():
    _l_(680389)


    for i in _c_(680343, _n_(680342, "range", lambda: range), 1,22):
        _l_(680388)

        uclient = _c_(680349, _n_(680344, "ureq", lambda: ureq), _n_(680345, "MY_URL", lambda: MY_URL)+_c_(680348, _a_(680346, 'categorias/todas/?page={}', "format"), _n_(680347, "i", lambda: i)))
        _l_(680350)
        page_html = _c_(680353, _a_(680352, _n_(680351, "uclient", lambda: uclient), "read"))
        _l_(680354)
        page_soup = _c_(680357, _n_(680355, "soup", lambda: soup), _n_(680356, "page_html", lambda: page_html), "html.parser")
        _l_(680358)
        contenedores = _c_(680361, _a_(680360, _n_(680359, "page_soup", lambda: page_soup), "findAll"), 'div', {'class':'cambur'})
        _l_(680362)
        contenedor=[]
        _l_(680363)
        for link in _n_(680364, "contenedor", lambda: contenedor):
            _l_(680387)

            link = _c_(680367, _a_(680366, _n_(680365, "contenedor", lambda: contenedor), "findAll"), 'a',['href'])
            _l_(680368)
            ulink = _c_(680372, _n_(680369, "ureq", lambda: ureq), _n_(680370, "MY_URL", lambda: MY_URL) + _n_(680371, "link", lambda: link))
            _l_(680373)
            page_link = _c_(680376, _a_(680375, _n_(680374, "ulink", lambda: ulink), "read"))
            _l_(680377)
            ulink = _c_(680379, _n_(680378, "close", lambda: close))
            _l_(680380)
            _c_(680383, _a_(680382, _n_(680381, "uclient", lambda: uclient), "close"))
            _l_(680384)
            aux = _n_(680385, "page_link", lambda: page_link)
            _l_(680386)

            return aux