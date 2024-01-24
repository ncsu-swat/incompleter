# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59028666/attributeerror-module-queue-has-no-attribute-simplequeue
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
async def fetch_html(url: _n_(383963, "str", lambda: str), session: _n_(383964, "ClientSession", lambda: ClientSession), **kwargs) -> _n_(383965, "str", lambda: str):
    _l_(383982)

    resp = await _c_(383970, _a_(383967, _n_(383966, "session", lambda: session), "request"), method='GET', url=_n_(383968, "url", lambda: url), **_n_(383969, "kwargs", lambda: kwargs))
    _l_(383971)
    _c_(383974, _a_(383973, _n_(383972, "resp", lambda: resp), "raise_for_status"))
    _l_(383975)
    html = await _c_(383978, _a_(383977, _n_(383976, "resp", lambda: resp), "text"))
    _l_(383979)
    aux = _n_(383980, "html", lambda: html)
    _l_(383981)
    return aux

async def bulk_crawl_and_write(file: _n_(383983, "IO", lambda: IO), urls: _n_(383984, "set", lambda: set), **kwargs) -> None:
    _l_(384006)

    urls = [
        'https://regex101.com/'
    ]
    _l_(383985)
    async with _c_(383987, _n_(383986, "ClientSession", lambda: ClientSession)) as session:
        _l_(384005)

        tasks = []
        _l_(383988)
        for url in _n_(383989, "urls", lambda: urls):
            _l_(383999)

            _c_(383997, _a_(383991, _n_(383990, "tasks", lambda: tasks), "append"), _c_(383996, _n_(383992, "fetch_html", lambda: fetch_html), url=_n_(383993, "url", lambda: url), session=_n_(383994, "session", lambda: session), **_n_(383995, "kwargs", lambda: kwargs)))
            _l_(383998)
        await _c_(384003, _a_(384001, _n_(384000, "asyncio", lambda: asyncio), "gather"), *_n_(384002, "tasks", lambda: tasks))
        _l_(384004)

if _n_(384007, "__name__", lambda: __name__) == '__main__':
    _l_(384014)

    _c_(384012, _a_(384009, _n_(384008, "asyncio", lambda: asyncio), "run"), _c_(384011, _n_(384010, "bulk_crawl_and_write", lambda: bulk_crawl_and_write), file=None, urls=None))
    _l_(384013)