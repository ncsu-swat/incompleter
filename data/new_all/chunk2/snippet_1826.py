# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(435966)

except ImportError:
    pass
try:
    from channels.routing import ProtocolTypeRouter, URLRouter
    _l_(435968)

except ImportError:
    pass
try:
    from channels.auth import AuthMiddlewareStack
    _l_(435970)

except ImportError:
    pass
try:
    from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
    _l_(435972)

except ImportError:
    pass
try:
    from qkchat.consumers import ChatConsumer
    _l_(435974)

except ImportError:
    pass

application = _c_(435985, _n_(435975, "ProtocolTypeRouter", lambda: ProtocolTypeRouter), {
    # Empty for now (http->django views is added by default)
    'websocket': _c_(435984, _n_(435976, "AllowedHostsOriginValidator", lambda: AllowedHostsOriginValidator), _c_(435983, _n_(435977, "AuthMiddlewareStack", lambda: AuthMiddlewareStack), _c_(435982, _n_(435978, "URLRouter", lambda: URLRouter), [
                    _c_(435981, _n_(435979, "url", lambda: url), r'^messages/(?P<username>[\w.@+-]+)/$', _n_(435980, "ChatConsumer", lambda: ChatConsumer)),    
            ])
        )
    )
})
_l_(435986)