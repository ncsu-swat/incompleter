# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64754301/uncaught-typeerror-cannot-read-property-sid-of-undefined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(404440)

except ImportError:
    pass
try:
    from aiohttp import web
    _l_(404442)

except ImportError:
    pass
try:
    import socketio
    _l_(404444)

except ImportError:
    pass
try:
    from aiohttp_middlewares import cors_middleware
    _l_(404446)

except ImportError:
    pass
try:
    from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS
    _l_(404448)

except ImportError:
    pass
sio = _c_(404451, _a_(404450, _n_(404449, "socketio", lambda: socketio), "AsyncServer"), async_mode='aiohttp',cors_allowed_origins='*')
_l_(404452)
app=_c_(404455, _a_(404454, _n_(404453, "web", lambda: web), "Application"))
_l_(404456)
_c_(404460, _a_(404458, _n_(404457, "sio", lambda: sio), "attach"), _n_(404459, "app", lambda: app))
_l_(404461)

async def index(request):
    _l_(404466)

    aux = _c_(404464, _a_(404463, _n_(404462, "web", lambda: web), "Response"), text="hello", content_type='text/html')
    _l_(404465)
    return aux

@_a_(404468, _n_(404467, "sio", lambda: sio), "event")
async def connect(sid, environ):
    _l_(404477)

    _c_(404471, _n_(404469, "print", lambda: print), 'Client connected',_n_(404470, "sid", lambda: sid))
    _l_(404472)
    await _c_(404475, _a_(404474, _n_(404473, "sio", lambda: sio), "emit"), 'message', "good")
    _l_(404476)

@_a_(404479, _n_(404478, "sio", lambda: sio), "event")
def disconnect(sid):
    _l_(404484)

    _c_(404482, _n_(404480, "print", lambda: print), 'Client disconnected',_n_(404481, "sid", lambda: sid))
    _l_(404483)

@_c_(404487, _a_(404486, _n_(404485, "sio", lambda: sio), "on"), 'message')
async def print_message(sid, message):
    _l_(404496)

    _c_(404490, _n_(404488, "print", lambda: print), "Socket ID: " , _n_(404489, "sid", lambda: sid))
    _l_(404491)
    _c_(404494, _n_(404492, "print", lambda: print), _n_(404493, "message", lambda: message))
    _l_(404495)

_c_(404501, _a_(404499, _a_(404498, _n_(404497, "app", lambda: app), "router"), "add_get"), '/', _n_(404500, "index", lambda: index))
_l_(404502)

if _n_(404503, "__name__", lambda: __name__) == '__main__':
    _l_(404509)

    _c_(404507, _a_(404505, _n_(404504, "web", lambda: web), "run_app"), _n_(404506, "app", lambda: app))
    _l_(404508)