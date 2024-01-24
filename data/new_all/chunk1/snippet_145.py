# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59481105/typeerror-an-asyncio-future-a-coroutine-or-an-awaitable-is-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bs4
    _l_(415525)

except ImportError:
    pass
try:
    import asyncio
    _l_(415527)

except ImportError:
    pass
try:
    import aiohttp
    _l_(415529)

except ImportError:
    pass


async def parse(page):
    _l_(415544)

    soup=_c_(415533, _a_(415531, _n_(415530, "bs4", lambda: bs4), "BeautifulSoup"), _n_(415532, "page", lambda: page),'html.parser')
    _l_(415534)
    _c_(415537, _a_(415536, _n_(415535, "soup", lambda: soup), "prettify"))
    _l_(415538)
    _c_(415542, _n_(415539, "print", lambda: print), _a_(415541, _n_(415540, "soup", lambda: soup), "title"))
    _l_(415543)



async def request():
    _l_(415557)

    async with _c_(415547, _a_(415546, _n_(415545, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
        _l_(415556)

        async with _c_(415550, _a_(415549, _n_(415548, "session", lambda: session), "get"), "https://google.com") as resp:
            _l_(415555)

            await _c_(415553, _n_(415551, "parse", lambda: parse), _n_(415552, "resp", lambda: resp))
            _l_(415554)



loop=_c_(415560, _a_(415559, _n_(415558, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(415561)
_c_(415565, _a_(415563, _n_(415562, "loop", lambda: loop), "run_until_complete"), _n_(415564, "request", lambda: request))
_l_(415566)