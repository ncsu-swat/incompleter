# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(1542055)

    import requests
    _l_(1542046)
except _n_(1542047, "ImportError", lambda: ImportError):
    _l_(1542054)

    try:
        _l_(1542053)

        import urllib.request
        _l_(1542048)
    except _n_(1542049, "AttributeError", lambda: AttributeError):
        _l_(1542052)

        try:
            import urllib
            _l_(1542051)

        except ImportError:
            pass


def get_content(url):
    _l_(1542084)

    try:
        _l_(1542083)

        aux = _a_(1542060, _c_(1542059, _a_(1542057, _n_(1542056, "requests", lambda: requests), "get"), _n_(1542058, "url", lambda: url)), "content") # Returns requests.models.Response.
        _l_(1542061) # Returns requests.models.Response.
        return aux # Returns requests.models.Response.
    except _n_(1542062, "NameError", lambda: NameError):
        _l_(1542082)

        try:
            _l_(1542081)

            with _c_(1542066, _a_(1542064, _a_(1542063, urllib, "request"), "urlopen"), _n_(1542065, "index_url", lambda: index_url)) as response:
                _l_(1542071)

                aux = _c_(1542069, _a_(1542068, _n_(1542067, "response", lambda: response), "read")) # Returns http.client.HTTPResponse.
                _l_(1542070) # Returns http.client.HTTPResponse.
                return aux # Returns http.client.HTTPResponse.
        except _n_(1542072, "AttributeError", lambda: AttributeError):
            _l_(1542080)

            aux = _c_(1542078, _a_(1542077, _c_(1542076, _a_(1542074, _n_(1542073, "urllib", lambda: urllib), "urlopen"), _n_(1542075, "url", lambda: url)), "read")) # Returns an instance.
            _l_(1542079) # Returns an instance.
            return aux # Returns an instance.

