# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51300845/attributeerror-module-http-server-has-no-attribute-threadinghttpserver
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def run(server_class=_n_(406162, "HTTPServer", lambda: HTTPServer), handler_class=_n_(406163, "BaseHTTPRequestHandler", lambda: BaseHTTPRequestHandler)):
    _l_(406174)

    server_address = ('', 8000)
    _l_(406164)
    httpd = _c_(406168, _n_(406165, "server_class", lambda: server_class), _n_(406166, "server_address", lambda: server_address), _n_(406167, "handler_class", lambda: handler_class))
    _l_(406169)
    _c_(406172, _a_(406171, _n_(406170, "httpd", lambda: httpd), "serve_forever"))
    _l_(406173)