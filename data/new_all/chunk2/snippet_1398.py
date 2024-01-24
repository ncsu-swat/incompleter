# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65002409/typeerror-event-registered-must-be-a-coroutine-function-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(463583, _n_(463582, "client", lambda: client), "event")
async def on_ready():
    _l_(463591)

    _c_(463586, _a_(463585, _n_(463584, "change_status", lambda: change_status), "start"))
    _l_(463587)
    _c_(463589, _n_(463588, "print", lambda: print), 'Bot is online')
    _l_(463590)



@_c_(463594, _a_(463593, _n_(463592, "tasks", lambda: tasks), "loop"), seconds=3600)
async def change_status():
    _l_(463608)

    await _c_(463606, _a_(463596, _n_(463595, "client", lambda: client), "change_presence"), status=_a_(463599, _a_(463598, _n_(463597, "discord", lambda: discord), "Status"), "idle"), activity=_c_(463605, _a_(463601, _n_(463600, "discord", lambda: discord), "Game"), _c_(463604, _n_(463602, "next", lambda: next), _n_(463603, "status", lambda: status))))
    _l_(463607)



@_a_(463610, _n_(463609, "client", lambda: client), "event")
def on_guild_join(client, message):
    _l_(463635)

    with _c_(463612, _n_(463611, "open", lambda: open), 'prefixes.json', 'r') as f:
        _l_(463618)

        prefixes = _c_(463616, _a_(463614, _n_(463613, "json", lambda: json), "load"), _n_(463615, "f", lambda: f))
        _l_(463617)


    _n_(463619, "prefixes", lambda: prefixes)[_c_(463624, _n_(463620, "str", lambda: str), _a_(463623, _a_(463622, _n_(463621, "message", lambda: message), "guild"), "id"))] = '.'
    _l_(463625)

    with _c_(463627, _n_(463626, "open", lambda: open), 'prefixes.json', 'w') as f:
        _l_(463634)

        _c_(463632, _a_(463629, _n_(463628, "json", lambda: json), "dump"), _n_(463630, "prefixes", lambda: prefixes), _n_(463631, "f", lambda: f), indent=4)
        _l_(463633)



@_a_(463637, _n_(463636, "client", lambda: client), "event")
async def on_guild_remove(guild):
    _l_(463663)

    with _c_(463639, _n_(463638, "open", lambda: open), 'prefixes.json', 'r') as f:
        _l_(463645)

        prefixes = _c_(463643, _a_(463641, _n_(463640, "json", lambda: json), "load"), _n_(463642, "f", lambda: f))
        _l_(463644)


    _c_(463652, _a_(463647, _n_(463646, "prefixes", lambda: prefixes), "pop"), _c_(463651, _n_(463648, "str", lambda: str), _a_(463650, _n_(463649, "guild", lambda: guild), "id")))
    _l_(463653)

    with _c_(463655, _n_(463654, "open", lambda: open), 'prefixes.json', 'w') as f:
        _l_(463662)

        _c_(463660, _a_(463657, _n_(463656, "json", lambda: json), "dump"), _n_(463658, "prefixes", lambda: prefixes), _n_(463659, "f", lambda: f), indent=4)
        _l_(463661)



@_c_(463666, _a_(463665, _n_(463664, "client", lambda: client), "command"), pass_context = True)
async def prefix(ctx, prefix):
    _l_(463692)

    with _c_(463668, _n_(463667, "open", lambda: open), 'prefixes.json', 'r') as f:
        _l_(463674)

        prefixes = _c_(463672, _a_(463670, _n_(463669, "json", lambda: json), "load"), _n_(463671, "f", lambda: f))
        _l_(463673)


    _n_(463675, "prefixes", lambda: prefixes)[_c_(463680, _n_(463676, "str", lambda: str), _a_(463679, _a_(463678, _n_(463677, "ctx", lambda: ctx), "guild"), "id"))] = _n_(463681, "prefix", lambda: prefix)
    _l_(463682)

    with _c_(463684, _n_(463683, "open", lambda: open), 'prefixes.json', 'w') as f:
        _l_(463691)

        _c_(463689, _a_(463686, _n_(463685, "json", lambda: json), "dump"), _n_(463687, "prefixes", lambda: prefixes), _n_(463688, "f", lambda: f), indent=4)
        _l_(463690)