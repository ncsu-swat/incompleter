# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63027848/discord-py-error-typeerror-new-got-an-unexpected-keyword-argument-deny
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(413390)

except ImportError:
    pass
try:
    import random
    _l_(413392)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(413394)

except ImportError:
    pass
try:
    import asyncio
    _l_(413396)

except ImportError:
    pass
client = _c_(413399, _a_(413398, _n_(413397, "commands", lambda: commands), "Bot"), command_prefix='{')
_l_(413400)
_c_(413403, _a_(413402, _n_(413401, "client", lambda: client), "remove_command"), 'help')
_l_(413404)

@_a_(413406, _n_(413405, "client", lambda: client), "event")
async def on_ready():
    _l_(413410)

    _c_(413408, _n_(413407, "print", lambda: print), "Signed in")
    _l_(413409)

@_c_(413413, _a_(413412, _n_(413411, "client", lambda: client), "command"))
async def dm(ctx):
    _l_(413419)

    await _c_(413417, _a_(413416, _a_(413415, _n_(413414, "ctx", lambda: ctx), "author"), "send"), "What up chump?")
    _l_(413418)

_c_(413422, _a_(413421, _n_(413420, "client", lambda: client), "run"), 'TOKEN')
_l_(413423)