# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67401599/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(469475)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(469477)

except ImportError:
    pass

DISCORD_TOKEN = "hahasikeyouwontgetm"
_l_(469478)

client = _c_(469481, _a_(469480, _n_(469479, "commands", lambda: commands), "Bot"), command_prefix="a!")
_l_(469482)


@_a_(469484, _n_(469483, "client", lambda: client), "event")
async def on_ready():
    _l_(469504)

    guild_count = 0
    _l_(469485)

    for guild in _a_(469487, _n_(469486, "client", lambda: client), "guilds"):
        _l_(469497)

        _c_(469493, _n_(469488, "print", lambda: print), f"- {_a_(469490, _n_(469489, 'guild', lambda: guild), 'id')} (name: {_a_(469492, _n_(469491, 'guild', lambda: guild), 'name')})")
        _l_(469494)

        guild_count = _n_(469495, "guild_count", lambda: guild_count) + 1
        _l_(469496)

    _c_(469502, _n_(469498, "print", lambda: print), "AnythingBot is in " + _c_(469501, _n_(469499, "str", lambda: str), _n_(469500, "guild_count", lambda: guild_count)) + " guilds.")
    _l_(469503)


@_c_(469507, _a_(469506, _n_(469505, "client", lambda: client), "command"))
async def order(ctx, arg):
    _l_(469527)

    if _n_(469508, "arg", lambda: arg) == "burger":
        _l_(469526)

        embed = _c_(469514, _a_(469510, _n_(469509, "discord", lambda: discord), "Embed"), title="here burger",
            color=_a_(469513, _a_(469512, _n_(469511, "ctx", lambda: ctx), "author"), "color")
        )
        _l_(469515)
        _c_(469518, _a_(469517, _n_(469516, "embed", lambda: embed), "set_image"), url='https://media.discordapp.net/attachments/839166049755856906/839166099336593428/burger.jpg'
                            '?width=670&height=670'
                        )
        _l_(469519)
        await _c_(469524, _a_(469522, _a_(469521, _n_(469520, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(469523, "embed", lambda: embed))
        _l_(469525)


@_c_(469530, _a_(469529, _n_(469528, "client", lambda: client), "command"))
async def math(ctx, arg, arg2, arg3):
    _l_(469591)

    mathed = 0
    _l_(469531)
    answer = 0
    _l_(469532)
    if _n_(469533, "arg2", lambda: arg2) == "+":
        _l_(469572)

        answer = _c_(469536, _n_(469534, "float", lambda: float), _n_(469535, "arg", lambda: arg)) + _c_(469539, _n_(469537, "float", lambda: float), _n_(469538, "arg3", lambda: arg3))
        _l_(469540)
        mathed = 1
        _l_(469541)
    elif _n_(469542, "arg2", lambda: arg2) == "-":
        _l_(469571)

        answer = _c_(469545, _n_(469543, "float", lambda: float), _n_(469544, "arg", lambda: arg)) - _c_(469548, _n_(469546, "float", lambda: float), _n_(469547, "arg3", lambda: arg3))
        _l_(469549)
        mathed = 1
        _l_(469550)
    elif _n_(469551, "arg2", lambda: arg2) == "/":
        _l_(469570)

        answer = _c_(469554, _n_(469552, "float", lambda: float), _n_(469553, "arg", lambda: arg)) / _c_(469557, _n_(469555, "float", lambda: float), _n_(469556, "arg3", lambda: arg3))
        _l_(469558)
        mathed = 1
        _l_(469559)
    elif _n_(469560, "arg2", lambda: arg2) == "*":
        _l_(469569)

        answer = _c_(469563, _n_(469561, "float", lambda: float), _n_(469562, "arg", lambda: arg)) * _c_(469566, _n_(469564, "float", lambda: float), _n_(469565, "arg3", lambda: arg3))
        _l_(469567)
        mathed = 1
        _l_(469568)
    embed = _c_(469581, _a_(469574, _n_(469573, "discord", lambda: discord), "Embed"), title="The answer is: " + _c_(469577, _n_(469575, "str", lambda: str), _n_(469576, "answer", lambda: answer)),
        color=_a_(469580, _a_(469579, _n_(469578, "ctx", lambda: ctx), "author"), "color")
    )
    _l_(469582)
    if _n_(469583, "mathed", lambda: mathed) == 1:
        _l_(469590)

        await _c_(469588, _a_(469586, _a_(469585, _n_(469584, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(469587, "embed", lambda: embed))
        _l_(469589)


@_c_(469594, _a_(469593, _n_(469592, "client", lambda: client), "command"))
async def jail(ctx, arg, arg2):
    _l_(469717)

    jailtime = _c_(469597, _n_(469595, "int", lambda: int), _n_(469596, "arg2", lambda: arg2)) * 60
    _l_(469598)
    arg = _c_(469601, _a_(469600, _n_(469599, "arg", lambda: arg), "replace"), "<@!", "")
    _l_(469602)
    arg = _c_(469605, _a_(469604, _n_(469603, "arg", lambda: arg), "replace"), ">", "")
    _l_(469606)
    prisoner = await _c_(469610, _a_(469608, _n_(469607, "client", lambda: client), "fetch_user"), user_id=_n_(469609, "arg", lambda: arg))
    _l_(469611)
    isadmin = False
    _l_(469612)
    admin = _c_(469619, _a_(469615, _a_(469614, _n_(469613, "discord", lambda: discord), "utils"), "get"), _a_(469618, _a_(469617, _n_(469616, "ctx", lambda: ctx), "guild"), "roles"), name='Admin')
    _l_(469620)
    default = _c_(469627, _a_(469623, _a_(469622, _n_(469621, "discord", lambda: discord), "utils"), "get"), _a_(469626, _a_(469625, _n_(469624, "ctx", lambda: ctx), "guild"), "roles"), name='Member')
    _l_(469628)
    jailed = _c_(469635, _a_(469631, _a_(469630, _n_(469629, "discord", lambda: discord), "utils"), "get"), _a_(469634, _a_(469633, _n_(469632, "ctx", lambda: ctx), "guild"), "roles"), name='Jailed')
    _l_(469636)

    embedj = _c_(469647, _a_(469638, _n_(469637, "discord", lambda: discord), "Embed"), title="Jailed " + _a_(469640, _n_(469639, "prisoner", lambda: prisoner), "display_name") + " for " + _c_(469643, _n_(469641, "str", lambda: str), _n_(469642, "jailtime", lambda: jailtime)) + "m.",
        color=_a_(469646, _a_(469645, _n_(469644, "ctx", lambda: ctx), "author"), "color")
    )
    _l_(469648)

    embedn = _c_(469654, _a_(469650, _n_(469649, "discord", lambda: discord), "Embed"), title="You must be a staff member to use this command.",
        color=_a_(469653, _a_(469652, _n_(469651, "ctx", lambda: ctx), "author"), "color"),
        author="loser"
    )
    _l_(469655)

    embedu = _c_(469663, _a_(469657, _n_(469656, "discord", lambda: discord), "Embed"), title=_a_(469659, _n_(469658, "prisoner", lambda: prisoner), "display_name") + " has been unjailed.",
        color=_a_(469662, _a_(469661, _n_(469660, "ctx", lambda: ctx), "author"), "color")
    )
    _l_(469664)

    if _n_(469665, "admin", lambda: admin) in _a_(469669, _a_(469668, _a_(469667, _n_(469666, "ctx", lambda: ctx), "message"), "author"), "roles"):
        _l_(469716)

        if _n_(469670, "admin", lambda: admin) in _n_(469671, "prisoner", lambda: prisoner):
            _l_(469673)

            isadmin = True
            _l_(469672)

        await _c_(469678, _a_(469676, _a_(469675, _n_(469674, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(469677, "embedj", lambda: embedj))
        _l_(469679)
        await _c_(469683, _a_(469681, _n_(469680, "client", lambda: client), "add_roles"), _n_(469682, "jailed", lambda: jailed))
        _l_(469684)

        _c_(469688, _a_(469686, _n_(469685, "time", lambda: time), "sleep"), _n_(469687, "jailtime", lambda: jailtime))
        _l_(469689)

        await _c_(469694, _a_(469692, _a_(469691, _n_(469690, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(469693, "embedu", lambda: embedu))
        _l_(469695)

        if _n_(469696, "isadmin", lambda: isadmin):
            _l_(469703)

            await _c_(469701, _a_(469698, _n_(469697, "client", lambda: client), "add_roles"), _n_(469699, "prisoner", lambda: prisoner), _n_(469700, "admin", lambda: admin))
            _l_(469702)
        await _c_(469708, _a_(469705, _n_(469704, "client", lambda: client), "add_roles"), _n_(469706, "prisoner", lambda: prisoner), _n_(469707, "default", lambda: default))
        _l_(469709)
    else:
        await _c_(469714, _a_(469712, _a_(469711, _n_(469710, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(469713, "embedn", lambda: embedn))
        _l_(469715)


_c_(469721, _a_(469719, _n_(469718, "client", lambda: client), "run"), _n_(469720, "DISCORD_TOKEN", lambda: DISCORD_TOKEN))
_l_(469722)