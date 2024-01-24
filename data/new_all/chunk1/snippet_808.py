# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44862228/proxybroker-attributeerror-dict-object-has-no-attribute-expired
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(414533)

except ImportError:
    pass
try:
    from proxybroker import Broker
    _l_(414535)

except ImportError:
    pass

async def use(proxies):
    _l_(414555)

    while True:
        _l_(414554)

        proxy = await _c_(414538, _a_(414537, _n_(414536, "proxies", lambda: proxies), "get"))
        _l_(414539)
        if _n_(414540, "proxy", lambda: proxy) is None:
            _l_(414553)

            break
            _l_(414541)
        elif 'SOCKS5' in _a_(414543, _n_(414542, "proxy", lambda: proxy), "types"):
            _l_(414552)

            _c_(414546, _n_(414544, "print", lambda: print), 'Found SOCKS5 proxy: %s' % _n_(414545, "proxy", lambda: proxy))
            _l_(414547)
        else:
            _c_(414550, _n_(414548, "print", lambda: print), 'Found proxy: %s' % _n_(414549, "proxy", lambda: proxy))
            _l_(414551)

async def find(proxies, loop):
    _l_(414571)

    broker = _c_(414559, _n_(414556, "Broker", lambda: Broker), queue=_n_(414557, "proxies", lambda: proxies),
                    timeout=8,
                    attempts_conn=3,
                    max_concurrent_conn=200,
                    judges=['https://httpheader.net/', 'http://httpheader.net/'],
                    providers=['http://www.proxylists.net/', 'http://fineproxy.org/eng/'],
                    verify_ssl=False,
                    loop=_n_(414558, "loop", lambda: loop))
    _l_(414560)

    # only anonymous & high levels of anonymity for http protocol and high for others:
    types = [('HTTP', ('Anonymous', 'High')), 'HTTPS', 'SOCKS4', 'SOCKS5']
    _l_(414561)
    countries = ['US', 'GB', 'DE']
    _l_(414562)
    limit = 10
    _l_(414563)

    await _c_(414569, _a_(414565, _n_(414564, "broker", lambda: broker), "find"), types=_n_(414566, "types", lambda: types), countries=_n_(414567, "countries", lambda: countries), limit=_n_(414568, "limit", lambda: limit))
    _l_(414570)

if _n_(414572, "__name__", lambda: __name__) == '__main__':
    _l_(414598)

    loop = _c_(414575, _a_(414574, _n_(414573, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(414576)
    proxies = _c_(414580, _a_(414578, _n_(414577, "asyncio", lambda: asyncio), "Queue"), loop=_n_(414579, "loop", lambda: loop))
    _l_(414581)
    tasks = _c_(414591, _a_(414583, _n_(414582, "asyncio", lambda: asyncio), "gather"), _c_(414587, _n_(414584, "find", lambda: find), _n_(414585, "proxies", lambda: proxies), _n_(414586, "loop", lambda: loop)), _c_(414590, _n_(414588, "use", lambda: use), _n_(414589, "proxies", lambda: proxies)))
    _l_(414592)
    _c_(414596, _a_(414594, _n_(414593, "loop", lambda: loop), "run_until_complete"), _n_(414595, "tasks", lambda: tasks))
    _l_(414597)