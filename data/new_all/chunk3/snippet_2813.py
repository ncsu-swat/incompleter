# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62396146/discord-py-osu-stats-error-command-raised-an-exception-typeerror-list-indices
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(536055, _a_(536054, _n_(536053, "client", lambda: client), "command"))
async def osu(ctx, arg):
    _l_(536085)

    token = "secret token"
    _l_(536056)
    res = _c_(536061, _a_(536058, _n_(536057, "requests", lambda: requests), "get"), f"https://osu.ppy.sh/api/get_user?u={_n_(536059, 'arg', lambda: arg)}&k={_n_(536060, 'token', lambda: token)}")
    _l_(536062)

    nickname = _c_(536065, _a_(536064, _n_(536063, "res", lambda: res), "json"))['username']
    _l_(536066)

    embed = _c_(536073, _a_(536068, _n_(536067, "discord", lambda: discord), "Embed"), title="Ecco le statistiche di osu.", description=f'Speriamo sia forte lmao', color=_c_(536072, _a_(536071, _a_(536070, _n_(536069, 'discord', lambda: discord), 'Color'), 'orange')))
    _l_(536074)
    _c_(536078, _a_(536076, _n_(536075, 'embed', lambda: embed), 'add_field'), name="Nickname", description=_n_(536077, 'nickname', lambda: nickname))
    _l_(536079)

    await _c_(536083, _a_(536081, _n_(536080, 'ctx', lambda: ctx), 'send'), embed=_n_(536082, 'embed', lambda: embed))
    _l_(536084)