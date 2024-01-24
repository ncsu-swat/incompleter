# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56970332/attributeerror-lxml-etree-qname-object-has-no-attribute-resolve
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from requests import Session
    _l_(523341)

except ImportError:
    pass
try:
    from requests.auth import HTTPBasicAuth
    _l_(523343)

except ImportError:
    pass
try:
    from zeep import Client, Settings
    _l_(523345)

except ImportError:
    pass
try:
    from zeep.cache import SqliteCache
    _l_(523347)

except ImportError:
    pass
try:
    from zeep.transports import Transport
    _l_(523349)

except ImportError:
    pass
try:
    from conf.shared_vars import B2B_PROXY, WSDL_PROXY
    _l_(523351)

except ImportError:
    pass

session = _c_(523353, _n_(523352, "Session", lambda: Session))
_l_(523354)
_n_(523355, "session", lambda: session).auth = _c_(523359, _n_(523356, "HTTPBasicAuth", lambda: HTTPBasicAuth), _n_(523357, "B2B_PROXY", lambda: B2B_PROXY)['key'], _n_(523358, "B2B_PROXY", lambda: B2B_PROXY)['secret'])
_l_(523360)
wsdl = _n_(523361, "WSDL_PROXY", lambda: WSDL_PROXY) + "SomeServices.wsdl"
_l_(523362)

client = _c_(523370, _n_(523363, "Client", lambda: Client), wsdl=_n_(523364, "wsdl", lambda: wsdl), 
    transport=_c_(523369, _n_(523365, "Transport", lambda: Transport), session=_n_(523366, "session", lambda: session), 
        cache=_c_(523368, _n_(523367, "SqliteCache", lambda: SqliteCache), path='./sqlite.db')))
_l_(523371)