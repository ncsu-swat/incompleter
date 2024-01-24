# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48625933/python-async-attributeerror-aexit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import aiohttp
    _l_(384270)

except ImportError:
    pass
try:
    import asyncio
    _l_(384272)

except ImportError:
    pass
try:
    import tqdm
    _l_(384274)

except ImportError:
    pass


async def fetch_url(session_, url_, timeout_=10):
    _l_(384300)

    with _c_(384278, _a_(384276, _n_(384275, "aiohttp", lambda: aiohttp), "Timeout"), _n_(384277, "timeout_", lambda: timeout_)):
        _l_(384299)

        async with _c_(384282, _a_(384280, _n_(384279, "session_", lambda: session_), "get"), _n_(384281, "url_", lambda: url_)) as response:
            _l_(384298)

            text = await _c_(384285, _a_(384284, _n_(384283, "response", lambda: response), "text"))
            _l_(384286)
            _c_(384294, _n_(384287, "print", lambda: print), _c_(384293, _a_(384288, "URL: {} - TEXT: {}", "format"), _n_(384289, "url_", lambda: url_), _c_(384292, _n_(384290, "len", lambda: len), _n_(384291, "text", lambda: text))))
            _l_(384295)
            aux = _n_(384296, "text", lambda: text)
            _l_(384297)
            return aux


async def parse_url(session, url, timeout=10):
    _l_(384318)

    # get doc from url
    async with await _c_(384305, _n_(384301, "fetch_url", lambda: fetch_url), _n_(384302, "session", lambda: session), _n_(384303, "url", lambda: url), _n_(384304, "timeout", lambda: timeout)) as doc:
        _l_(384317)

        _c_(384313, _n_(384306, "print", lambda: print), _c_(384312, _a_(384307, "DOC: {}", "format"), _n_(384308, "doc", lambda: doc), _c_(384311, _n_(384309, "len", lambda: len), _n_(384310, "doc", lambda: doc))))
        _l_(384314)
        aux = _n_(384315, "doc", lambda: doc)
        _l_(384316)
        return aux


async def parse_urls(session, urls, loop):
    _l_(384339)

    tasks = [_c_(384322, _n_(384319, "parse_url", lambda: parse_url), _n_(384320, "session", lambda: session), _n_(384321, "url", lambda: url)) for url in _n_(384323, "urls", lambda: urls)]
    _l_(384324)
    responses = [await _n_(384325, "f", lambda: f) for f in _c_(384335, _a_(384327, _n_(384326, "tqdm", lambda: tqdm), "tqdm"), _c_(384331, _a_(384329, _n_(384328, "asyncio", lambda: asyncio), "as_completed"), _n_(384330, "tasks", lambda: tasks)), total = _c_(384334, _n_(384332, "len", lambda: len), _n_(384333, "tasks", lambda: tasks)))]
    _l_(384336)
    aux = _n_(384337, "responses", lambda: responses)
    _l_(384338)
    return aux


if _n_(384340, "__name__", lambda: __name__) == '__main__':
    _l_(384369)


    tickers = ['CTXS', 'MSFT', 'AAPL', 'GPRO', 'G', 'INTC', 'SYNC', 'SYNA']
    _l_(384341)
    urls = [_c_(384344, _a_(384342, "https://finance.yahoo.com/quote/{}", "format"), _n_(384343, "ticker", lambda: ticker)) for ticker in _n_(384345, "tickers", lambda: tickers)]
    _l_(384346)

    loop = _c_(384349, _a_(384348, _n_(384347, "asyncio", lambda: asyncio), "get_event_loop"))
    _l_(384350)
    with _c_(384354, _a_(384352, _n_(384351, "aiohttp", lambda: aiohttp), "ClientSession"), loop=_n_(384353, "loop", lambda: loop)) as session:
        _l_(384368)

        parsed_data = _c_(384362, _a_(384356, _n_(384355, "loop", lambda: loop), "run_until_complete"), _c_(384361, _n_(384357, "parse_urls", lambda: parse_urls), _n_(384358, "session", lambda: session), _n_(384359, "urls", lambda: urls), _n_(384360, "loop", lambda: loop)))
        _l_(384363)
        _c_(384366, _n_(384364, "print", lambda: print), _n_(384365, "parsed_data", lambda: parsed_data))
        _l_(384367)