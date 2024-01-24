# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48055880/attributeerror-exit-with-socketserver-on-python-3-4-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.request
    _l_(413886)

except ImportError:
    pass
try:
    import http.server
    _l_(413888)

except ImportError:
    pass
try:
    import socketserver
    _l_(413890)

except ImportError:
    pass
PORT = 8000
_l_(413891)

def requestHandler(request, client_address,server):
    _l_(413904)

    # test to print to console when the handler is invoked. 
    _c_(413902, _n_(413892, "print", lambda: print), "Request = " + _c_(413895, _n_(413893, "str", lambda: str), _n_(413894, "request", lambda: request)) + " Client Address = " + _c_(413898, _n_(413896, "str", lambda: str), _n_(413897, "client_address", lambda: client_address)) + " Server = " + _c_(413901, _n_(413899, "str", lambda: str), _n_(413900, "server", lambda: server)))
    _l_(413903)

def startWebServer():
    _l_(413921)

    Handler = _n_(413905, "requestHandler", lambda: requestHandler)
    _l_(413906)
    with _c_(413911, _a_(413908, _n_(413907, "socketserver", lambda: socketserver), "TCPServer"), ("", _n_(413909, "PORT", lambda: PORT)), _n_(413910, "Handler", lambda: Handler)) as httpd:
        _l_(413920)

        _c_(413914, _n_(413912, "print", lambda: print), "serving at port", _n_(413913, "PORT", lambda: PORT))
        _l_(413915)
        _c_(413918, _a_(413917, _n_(413916, "httpd", lambda: httpd), "serve_forever"))
        _l_(413919)

def main():
    _l_(413925)

    _c_(413923, _n_(413922, "startWebServer", lambda: startWebServer))
    _l_(413924)

_c_(413927, _n_(413926, "main", lambda: main))
_l_(413928)