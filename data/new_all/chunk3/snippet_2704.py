# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66144895/discord-bot-problem-discord-py-attributeerror-bot-object-has-no-attribute-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bot = _c_(542597, _a_(542596, _n_(542595, "commands", lambda: commands), "Bot"), command_prefix='.')
_l_(542598)

@_a_(542600, _n_(542599, "bot", lambda: bot), "event")
async def on_ready():
    _l_(542608)

    _c_(542603, _a_(542602, _n_(542601, "crypto_hour", lambda: crypto_hour), "start"))
    _l_(542604)
    _c_(542606, _n_(542605, "print", lambda: print), 'Bot is active!')
    _l_(542607)

@_c_(542611, _a_(542610, _n_(542609, "tasks", lambda: tasks), "loop"), hours=10)
async def crypto_hour():
    _l_(542667)

    channel = _c_(542614, _a_(542613, _n_(542612, "bot", lambda: bot), "get_channel"), 809155804170682408)
    _l_(542615)
    embed = _c_(542622, _a_(542617, _n_(542616, "discord", lambda: discord), "Embed"), title = ":D",
        color = _c_(542621, _a_(542620, _a_(542619, _n_(542618, "discord", lambda: discord), "Color"), "blue")),
    )
    _l_(542623)
    url = 'http://api.coinlayer.com/live?access_key='
    _l_(542624)
    async with _c_(542627, _a_(542626, _n_(542625, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
        _l_(542666)

        raw_response = await _c_(542631, _a_(542629, _n_(542628, "session", lambda: session), "get"), _n_(542630, "url", lambda: url))
        _l_(542632)
        response = await _c_(542635, _a_(542634, _n_(542633, "raw_response", lambda: raw_response), "text"))
        _l_(542636)
        response = _c_(542640, _a_(542638, _n_(542637, "json", lambda: json), "loads"), _n_(542639, "response", lambda: response))
        _l_(542641)
        _c_(542644, _a_(542643, _n_(542642, "embed", lambda: embed), "set_author"), name=':D')
        _l_(542645)
        _c_(542651, _a_(542647, _n_(542646, "embed", lambda: embed), "add_field"), name='• **Bitcoin (BTC)**:', value=_c_(542650, _n_(542648, "str", lambda: str), f"{_n_(542649, 'response', lambda: response)['rates']['BTC']}PLN"), inline=True)
        _l_(542652)
        _c_(542658, _a_(542654, _n_(542653, "embed", lambda: embed), "add_field"), name='• **Ethereum (ETH)**:', value=_c_(542657, _n_(542655, "str", lambda: str), f"{_n_(542656, 'response', lambda: response)['rates']['ETH']}PLN"), inline=True)
        _l_(542659)
        await _c_(542664, _a_(542662, _a_(542661, _n_(542660, "bot", lambda: bot), "channel"), "send"), embed=_n_(542663, "embed", lambda: embed))
        _l_(542665)