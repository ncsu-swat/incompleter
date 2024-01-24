# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67491060/beginner-discord-bot-problems-attributeerror-nonetype-object-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(640836)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot
    _l_(640838)

except ImportError:
    pass

bot = _c_(640840, _n_(640839, "Bot", lambda: Bot), command_prefix='$')
_l_(640841)
intents = _c_(640846, _a_(640845, _c_(640844, _a_(640843, _n_(640842, "discord", lambda: discord), "Intents")), "all"))
_l_(640847)
TOKEN = 'changeditforexample'
_l_(640848)

@_a_(640850, _n_(640849, "bot", lambda: bot), "event")
async def on_ready():
    _l_(640856)

    _c_(640854, _n_(640851, "print", lambda: print), f'Bot connected as {_a_(640853, _n_(640852, "bot", lambda: bot), "user")}')
    _l_(640855)


@_c_(640859, _a_(640858, _n_(640857, 'bot', lambda: bot), 'command'), name='server')
async def fetchserverInfo(ctx):
    _l_(640884)

    guild = _a_(640861, _n_(640860, 'ctx', lambda: ctx), 'guild')
    _l_(640862)

    await _c_(640867, _a_(640864, _n_(640863, 'ctx', lambda: ctx), 'send'), f'Server Name: {_a_(640866, _n_(640865, "guild", lambda: guild), "name")}')
    _l_(640868)
    await _c_(640875, _a_(640870, _n_(640869, 'ctx', lambda: ctx), 'send'), f'Server Size: {_c_(640874, _n_(640871, "len", lambda: len), _a_(640873, _n_(640872, "guild", lambda: guild), "members"))}')
    _l_(640876)
    await _c_(640882, _a_(640878, _n_(640877, 'ctx', lambda: ctx), 'send'), f'Server owner: {_a_(640881, _a_(640880, _n_(640879, "guild", lambda: guild), "owner"), "display_name")}')
    _l_(640883)


_c_(640888, _a_(640886, _n_(640885, 'bot', lambda: bot), 'run'), _n_(640887, 'TOKEN', lambda: TOKEN))
_l_(640889)