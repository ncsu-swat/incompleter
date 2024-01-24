# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66143141/i-have-problem-with-discord-py-typeerror-can-only-concatenate-str-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(549300, _a_(549299, _n_(549298, "client", lambda: client), "command"), pass_context=True)
async def bitcoin(ctx):
    _l_(549325)

    url = 'http://api.coinlayer.com/live?access_key='
    _l_(549301)
    async with _c_(549304, _a_(549303, _n_(549302, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
        _l_(549324)

        raw_response = await _c_(549308, _a_(549306, _n_(549305, "session", lambda: session), "get"), _n_(549307, "url", lambda: url))
        _l_(549309)
        response = await _c_(549312, _a_(549311, _n_(549310, "raw_response", lambda: raw_response), "text"))
        _l_(549313)
        response = _c_(549317, _a_(549315, _n_(549314, "json", lambda: json), "loads"), _n_(549316, "response", lambda: response))
        _l_(549318)
        await _c_(549322, _a_(549320, _n_(549319, "ctx", lambda: ctx), "send"), "Bitcoin price is: $" + _n_(549321, "response", lambda: response)['rates']['BTC'])
        _l_(549323)