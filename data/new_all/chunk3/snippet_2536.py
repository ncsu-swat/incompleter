# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72495771/attributeerror-module-wsgi-has-no-attribute-application
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import webbrowser
    _l_(538873)

except ImportError:
    pass
try:
    import time
    _l_(538875)

except ImportError:
    pass

#!/usr/bin/env python

try:
    _l_(538881)

    # For Python 3.0 and later
    from urllib.request import urlopen
    _l_(538876)
except _n_(538877, "ImportError", lambda: ImportError):
    _l_(538880)

    try:
        from urllib2 import urlopen
        _l_(538879)

    except ImportError:
        pass
try:
    import certifi
    _l_(538883)

except ImportError:
    pass
try:
    import json
    _l_(538885)

except ImportError:
    pass

def get_jsonparsed_data(url):
    _l_(538904)

    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = _c_(538891, _n_(538886, "urlopen", lambda: urlopen), _n_(538887, "url", lambda: url), cafile=_c_(538890, _a_(538889, _n_(538888, "certifi", lambda: certifi), "where")))
    _l_(538892)
    data = _c_(538897, _a_(538896, _c_(538895, _a_(538894, _n_(538893, "response", lambda: response), "read")), "decode"), "utf-8")
    _l_(538898)
    aux = _c_(538902, _a_(538900, _n_(538899, "json", lambda: json), "loads"), _n_(538901, "data", lambda: data))
    _l_(538903)
    return aux

url = ("https://financialmodelingprep.com/api/v3/quote/AAPL,FB?apikey=d099f1f81bf9a62d0f16b90c3dc3f718")
_l_(538905)
_c_(538910, _n_(538906, "print", lambda: print), _c_(538909, _n_(538907, "get_jsonparsed_data", lambda: get_jsonparsed_data), _n_(538908, "url", lambda: url)))
_l_(538911)

country = _c_(538914, _n_(538912, "get_jsonparsed_data", lambda: get_jsonparsed_data), _n_(538913, "url", lambda: url))
_l_(538915)
count = 0
_l_(538916)
for result in _n_(538917, "country", lambda: country):
    _l_(538929)

    if _n_(538918, "count", lambda: count) == 0:
        _l_(538928)

        header = _c_(538921, _a_(538920, _n_(538919, "result", lambda: result), "keys"))
        _l_(538922)
        for head in _n_(538923, "header", lambda: header):
            _l_(538926)

            html_content = f"<div> {_n_(538924, 'head', lambda: head)} </div>"
            _l_(538925)
        count += 1
        _l_(538927)


with _c_(538931, _n_(538930, "open", lambda: open), "index.html", "w") as html_file:
    _l_(538948)

    _c_(538935, _a_(538933, _n_(538932, "html_file", lambda: html_file), "write"), _n_(538934, "html_content", lambda: html_content))
    _l_(538936)
    _c_(538938, _n_(538937, "print", lambda: print), "Html file created successfully !!")
    _l_(538939)

    _c_(538942, _a_(538941, _n_(538940, "time", lambda: time), "sleep"), 2)
    _l_(538943)
    _c_(538946, _a_(538945, _n_(538944, "webbrowser", lambda: webbrowser), "open_new_tab"), "index.html")
    _l_(538947)