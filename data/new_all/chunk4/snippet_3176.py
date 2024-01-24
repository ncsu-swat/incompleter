# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25845161/ws4py-under-cherrypy-under-wsgi-exception-attributeerror-mod-wsgi-input-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cherrypy
    _l_(621044)

except ImportError:
    pass
try:
    from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
    _l_(621046)

except ImportError:
    pass
try:
    from ws4py.websocket import EchoWebSocket
    _l_(621048)

except ImportError:
    pass
try:
    import atexit
    _l_(621050)

except ImportError:
    pass
try:
    import logging
    _l_(621052)

except ImportError:
    pass

# see http://tools.cherrypy.org/wiki/ModWSGI
_c_(621056, _a_(621055, _a_(621054, _n_(621053, "cherrypy", lambda: cherrypy), "config"), "update"), {'environment': 'embedded'}) 
_l_(621057) 
if _c_(621061, _a_(621060, _a_(621059, _n_(621058, "cherrypy", lambda: cherrypy), "__version__"), "startswith"), '3.0') and _a_(621064, _a_(621063, _n_(621062, "cherrypy", lambda: cherrypy), "engine"), "state") == 0:
    _l_(621077)

    _c_(621068, _a_(621067, _a_(621066, _n_(621065, "cherrypy", lambda: cherrypy), "engine"), "start"), blocking=False)
    _l_(621069)
    _c_(621075, _a_(621071, _n_(621070, "atexit", lambda: atexit), "register"), _a_(621074, _a_(621073, _n_(621072, "cherrypy", lambda: cherrypy), "engine"), "stop"))
    _l_(621076)

class Root(_n_(621078, "object", lambda: object)):
    _l_(621085)

    def index(self):
        _l_(621079)

return 'I work!'    def ws(self):
        _l_(621082)

_c_(621081, _n_(621080, "print", lambda: print), 'THIS IS NEVER PRINTED :(')    index.exposed=True
    _l_(621083)
    ws.exposed=True
    _l_(621084)

# registering the websocket
conf={'/ws':{'tools.websocket.on': True,'tools.websocket.handler_cls': _n_(621086, "EchoWebSocket", lambda: EchoWebSocket)}}
_l_(621087)
_c_(621093, _a_(621092, _c_(621091, _n_(621088, "WebSocketPlugin", lambda: WebSocketPlugin), _a_(621090, _n_(621089, "cherrypy", lambda: cherrypy), "engine")), "subscribe"))
_l_(621094)
_a_(621096, _n_(621095, "cherrypy", lambda: cherrypy), "tools").websocket = _c_(621098, _n_(621097, "WebSocketTool", lambda: WebSocketTool))  
_l_(621099)  

#show stacktraces in console (for some reason this is not default in cherrypy+WSGI)
logger = _c_(621102, _a_(621101, _n_(621100, "logging", lambda: logging), "getLogger"))
_l_(621103)
_c_(621108, _a_(621105, _n_(621104, "logger", lambda: logger), "setLevel"), _a_(621107, _n_(621106, "logging", lambda: logging), "INFO"))
_l_(621109)
stream = _c_(621112, _a_(621111, _n_(621110, "logging", lambda: logging), "StreamHandler"))
_l_(621113)
_c_(621118, _a_(621115, _n_(621114, "stream", lambda: stream), "setLevel"), _a_(621117, _n_(621116, "logging", lambda: logging), "INFO"))
_l_(621119)
_c_(621123, _a_(621121, _n_(621120, "logger", lambda: logger), "addHandler"), _n_(621122, "stream", lambda: stream))
_l_(621124)

application = _c_(621130, _a_(621126, _n_(621125, "cherrypy", lambda: cherrypy), "Application"), _c_(621128, _n_(621127, "Root", lambda: Root)), script_name='', config=_n_(621129, "conf", lambda: conf))
_l_(621131)