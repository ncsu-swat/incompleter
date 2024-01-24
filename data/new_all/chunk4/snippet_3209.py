# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77350345/asyncio-gather-typeerror-an-asyncio-future-a-coroutine-or-an-awaitable-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import asyncio
    _l_(588614)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(588616)

except ImportError:
    pass
try:
    from requests_html import AsyncHTMLSession
    _l_(588618)

except ImportError:
    pass

async def fetch_proxies(url):
    _l_(588644)

    session = _c_(588620, _n_(588619, "AsyncHTMLSession", lambda: AsyncHTMLSession))
    _l_(588621)
    webpage = await _c_(588625, _a_(588623, _n_(588622, "session", lambda: session), "get"), _n_(588624, "url", lambda: url)) # headers=headers
    _l_(588626) # headers=headers
    await _c_(588629, _a_(588628, _n_(588627, "session", lambda: session), "close"))
    _l_(588630)
    soup = _c_(588635, _n_(588631, "BeautifulSoup", lambda: BeautifulSoup), _a_(588634, _a_(588633, _n_(588632, "webpage", lambda: webpage), "html"), "raw_html"), 'lxml')
    _l_(588636)
    tag = _c_(588639, _a_(588638, _n_(588637, "soup", lambda: soup), "find"), 'textarea', {'class':'form-control'})
    _l_(588640)
    aux = _a_(588642, _n_(588641, "tag", lambda: tag), "text")
    _l_(588643)
    return aux

async def check_valid_proxy(proxy):
    _l_(588666)

    try:
        _l_(588665)

        session = _c_(588646, _n_(588645, "AsyncHTMLSession", lambda: AsyncHTMLSession))
        _l_(588647)
        webpage = await _c_(588651, _a_(588649, _n_(588648, "session", lambda: session), "get"), 'https://ifconfig.me', proxies = {'https' : _n_(588650, "proxy", lambda: proxy)})
        _l_(588652)
        await _c_(588655, _a_(588654, _n_(588653, "session", lambda: session), "close"))
        _l_(588656)
        aux = _n_(588657, "proxy", lambda: proxy)
        _l_(588658)
        return aux
    except _n_(588659, "Exception", lambda: Exception) as err:
        _l_(588664)

        _c_(588662, _n_(588660, "print", lambda: print), _n_(588661, "err", lambda: err))
        _l_(588663)

async def main():
    _l_(588705)

    url = 'https://free-proxy-list.net'
    _l_(588667)
    proxy_fetch = await _c_(588670, _n_(588668, "fetch_proxies", lambda: fetch_proxies), _n_(588669, "url", lambda: url))
    _l_(588671)
    proxy_list = _c_(588674, _a_(588673, _n_(588672, "proxy_fetch", lambda: proxy_fetch), "split"), '\n')[3:-1]
    _l_(588675)
    tasks = []
    _l_(588676)
    for proxy in _n_(588677, "proxy_list", lambda: proxy_list):
        _l_(588697)

        task = _c_(588683, _a_(588679, _n_(588678, "asyncio", lambda: asyncio), "create_task"), _c_(588682, _n_(588680, "check_valid_proxy", lambda: check_valid_proxy), _n_(588681, "proxy", lambda: proxy)))
        _l_(588684)
        _c_(588688, _a_(588686, _n_(588685, "tasks", lambda: tasks), "append"), _n_(588687, "task", lambda: task))
        _l_(588689)
        _c_(588695, _a_(588691, _n_(588690, "tasks", lambda: tasks), "append"), await _c_(588694, _a_(588693, _n_(588692, "asyncio", lambda: asyncio), "sleep"), .1))
        _l_(588696)
    valid_proxies = _c_(588701, _a_(588699, _n_(588698, "asyncio", lambda: asyncio), "gather"), *_n_(588700, "tasks", lambda: tasks))
    _l_(588702)
    aux = _n_(588703, "valid_proxies", lambda: valid_proxies)
    _l_(588704)
    return aux

loop = _c_(588708, _a_(588707, _n_(588706, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(588709)
valid_proxy_list = _c_(588714, _a_(588711, _n_(588710, "loop", lambda: loop), "run_until_complete"), _c_(588713, _n_(588712, "main", lambda: main)))
_l_(588715)
_c_(588718, _n_(588716, "print", lambda: print), _n_(588717, "valid_proxy_list", lambda: valid_proxy_list))
_l_(588719)