# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66187544/discord-py-covid-module-doesnt-work-attributeerror-extra-no-attribute-allow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(533026, _a_(533025, _n_(533024, "tasks", lambda: tasks), "loop"), hours=24)
async def covid_hour():
    _l_(533087)

    channel = _c_(533029, _a_(533028, _n_(533027, "client", lambda: client), "get_channel"), 809881992367702117)
    _l_(533030)
    embed = _c_(533037, _a_(533032, _n_(533031, "discord", lambda: discord), "Embed"), title = "Dane dot. COVID-19 w Polsce:",
        color = _c_(533036, _a_(533035, _a_(533034, _n_(533033, "discord", lambda: discord), "Color"), "red"))
    )
    _l_(533038)
    url = 'API'
    _l_(533039)
    async with _c_(533042, _a_(533041, _n_(533040, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
        _l_(533086)

        raw_response = await _c_(533046, _a_(533044, _n_(533043, "session", lambda: session), "get"), _n_(533045, "url", lambda: url))
        _l_(533047)
        response = await _c_(533050, _a_(533049, _n_(533048, "raw_response", lambda: raw_response), "text"))
        _l_(533051)
        response = _c_(533055, _a_(533053, _n_(533052, "json", lambda: json), "loads"), _n_(533054, "response", lambda: response))
        _l_(533056)
        _c_(533062, _a_(533058, _n_(533057, "embed", lambda: embed), "set_author"), name=_c_(533061, _n_(533059, "str", lambda: str), f'{_n_(533060, "date", lambda: date)}'))
        _l_(533063)
        _c_(533068, _a_(533065, _n_(533064, 'embed', lambda: embed), 'add_field'), name='• **Kraj**:', value=_c_(533067, _n_(533066, 'str', lambda: str), f"Polska"), inline=False)
        _l_(533069)
        _c_(533075, _a_(533071, _n_(533070, "embed", lambda: embed), "add_field"), name='• **Nowe zakażenia**:', value=_c_(533074, _n_(533072, "str", lambda: str), f"{_n_(533073, 'response', lambda: response)['dailyInfected']}"), inline=True)
        _l_(533076)
        _c_(533079, _a_(533078, _n_(533077, "embed", lambda: embed), "set_footer"), text="dBot created by Diablo#4700")
        _l_(533080)
        await _c_(533084, _a_(533082, _n_(533081, "channel", lambda: channel), "send"), embed=_n_(533083, "embed", lambda: embed))
        _l_(533085)