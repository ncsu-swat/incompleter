# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66179269/attributeerror-tuple-object-has-no-attribute-set-author-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(451144, _a_(451143, _n_(451142, "tasks", lambda: tasks), "loop"), hours=24)
async def covid_hour():
    _l_(451261)

    channel = _c_(451147, _a_(451146, _n_(451145, "client", lambda: client), "get_channel"), 809881992367702117),
    _l_(451148)
    embed = _c_(451155, _a_(451150, _n_(451149, "discord", lambda: discord), "Embed"), title = "Dane dot. COVID-19 w Polsce:",
        color = _c_(451154, _a_(451153, _a_(451152, _n_(451151, "discord", lambda: discord), "Color"), "blue")),
    ),
    _l_(451156)
    url = 'API'
    _l_(451157)
    async with _c_(451160, _a_(451159, _n_(451158, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
        _l_(451260)

        raw_response = await _c_(451164, _a_(451162, _n_(451161, "session", lambda: session), "get"), _n_(451163, "url", lambda: url))
        _l_(451165)
        response = await _c_(451168, _a_(451167, _n_(451166, "raw_response", lambda: raw_response), "text"))
        _l_(451169)
        response = _c_(451173, _a_(451171, _n_(451170, "json", lambda: json), "loads"), _n_(451172, "response", lambda: response))
        _l_(451174)
        _c_(451180, _a_(451176, _n_(451175, "embed", lambda: embed), "set_author"), name=_c_(451179, _n_(451177, "str", lambda: str), f'{_n_(451178, "date", lambda: date)}'))
        _l_(451181)
        _c_(451186, _a_(451183, _n_(451182, 'embed', lambda: embed), 'add_field'), name='• **Kraj**:', value=_c_(451185, _n_(451184, 'str', lambda: str), f"Polska"), inline=False)
        _l_(451187)
        _c_(451193, _a_(451189, _n_(451188, "embed", lambda: embed), "add_field"), name='• **Nowe zakażenia**:', value=_c_(451192, _n_(451190, "str", lambda: str), f"{_n_(451191, 'response', lambda: response)['dailyInfected']}"), inline=True)
        _l_(451194)
        _c_(451200, _a_(451196, _n_(451195, "embed", lambda: embed), "add_field"), name='• **Nowe zgony**:', value=_c_(451199, _n_(451197, "str", lambda: str), f"{_n_(451198, 'response', lambda: response)['dailyDeceased']}"), inline=True)
        _l_(451201)
        _c_(451207, _a_(451203, _n_(451202, "embed", lambda: embed), "add_field"), name='• **Nowe testy**:', value=_c_(451206, _n_(451204, "str", lambda: str), f"{_n_(451205, 'respons', lambda: respons)['dailyTested']}"), inline=True)
        _l_(451208)
        _c_(451214, _a_(451210, _n_(451209, "embed", lambda: embed), "add_field"), name='• **Nowe uzdrowienia**:', value=_c_(451213, _n_(451211, "str", lambda: str), f"{_n_(451212, 'response', lambda: response)['dailyRecovered']}"), inline=True)
        _l_(451215)
        _c_(451221, _a_(451217, _n_(451216, "embed", lambda: embed), "add_field"), name='• **Aktualnie zakażonych**:', value=_c_(451220, _n_(451218, "str", lambda: str), f"{_n_(451219, 'respons', lambda: respons)['activeCase']}"), inline=True)
        _l_(451222)
        _c_(451228, _a_(451224, _n_(451223, "embed", lambda: embed), "add_field"), name='• **Łącznie potwierdzonych**:', value=_c_(451227, _n_(451225, "str", lambda: str), f"{_n_(451226, 'response', lambda: response)['infected']}"), inline=True)
        _l_(451229)
        _c_(451235, _a_(451231, _n_(451230, "embed", lambda: embed), "add_field"), name='• **Łączne zgony**:', value=_c_(451234, _n_(451232, "str", lambda: str), f"{_n_(451233, 'response', lambda: response)['deceased']}"), inline=True)
        _l_(451236)
        _c_(451242, _a_(451238, _n_(451237, "embed", lambda: embed), "add_field"), name='• **Wyzdrowiałych**:', value=_c_(451241, _n_(451239, "str", lambda: str), f"{_n_(451240, 'response', lambda: response)['recovered']}"), inline=True)
        _l_(451243)
        _c_(451249, _a_(451245, _n_(451244, "embed", lambda: embed), "add_field"), name='• **Nowych na kwarantannie**:', value=_c_(451248, _n_(451246, "str", lambda: str), f"{_n_(451247, 'response', lambda: response)['dailyQuarantine']}"), inline=True)
        _l_(451250)
        _c_(451253, _a_(451252, _n_(451251, "embed", lambda: embed), "set_footer"), text="dBot created by Diablo#4700")
        _l_(451254)
        await _c_(451258, _a_(451256, _n_(451255, "channel", lambda: channel), "send"), embed=_n_(451257, "embed", lambda: embed))
        _l_(451259)