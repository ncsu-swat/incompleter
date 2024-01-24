# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67491060/beginner-discord-bot-problems-attributeerror-nonetype-object-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(537809)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot
    _l_(537811)

except ImportError:
    pass

bot = _c_(537813, _n_(537812, "Bot", lambda: Bot), command_prefix='$')
_l_(537814)
intents = _c_(537819, _a_(537818, _c_(537817, _a_(537816, _n_(537815, "discord", lambda: discord), "Intents")), "all"))
_l_(537820)
TOKEN = 'changeditforexample'
_l_(537821)

@_a_(537823, _n_(537822, "bot", lambda: bot), "event")
async def on_ready():
    _l_(537829)

    _c_(537827, _n_(537824, "print", lambda: print), f'Bot connected as {_a_(537826, _n_(537825, "bot", lambda: bot), "user")}')
    _l_(537828)


@_c_(537832, _a_(537831, _n_(537830, 'bot', lambda: bot), 'command'), name='server')
async def fetchserverInfo(ctx):
    _l_(537857)

    guild = _a_(537834, _n_(537833, 'ctx', lambda: ctx), 'guild')
    _l_(537835)

    await _c_(537840, _a_(537837, _n_(537836, 'ctx', lambda: ctx), 'send'), f'Server Name: {_a_(537839, _n_(537838, "guild", lambda: guild), "name")}')
    _l_(537841)
    await _c_(537848, _a_(537843, _n_(537842, 'ctx', lambda: ctx), 'send'), f'Server Size: {_c_(537847, _n_(537844, "len", lambda: len), _a_(537846, _n_(537845, "guild", lambda: guild), "members"))}')
    _l_(537849)
    await _c_(537855, _a_(537851, _n_(537850, 'ctx', lambda: ctx), 'send'), f'Server owner: {_a_(537854, _a_(537853, _n_(537852, "guild", lambda: guild), "owner"), "display_name")}')
    _l_(537856)


_c_(537861, _a_(537859, _n_(537858, 'bot', lambda: bot), 'run'), _n_(537860, 'TOKEN', lambda: TOKEN))
_l_(537862)