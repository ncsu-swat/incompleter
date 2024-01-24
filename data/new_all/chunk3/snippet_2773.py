# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63758974/attributeerror-moderation-object-has-no-attribute-channel
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(550169)

except ImportError:
    pass
try:
    import asyncio
    _l_(550171)

except ImportError:
    pass
try:
    import re
    _l_(550173)

except ImportError:
    pass
try:
    import os
    _l_(550175)

except ImportError:
    pass
try:
    import random
    _l_(550177)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(550179)

except ImportError:
    pass

class Moderation(_a_(550181, _n_(550180, "commands", lambda: commands), "Cog")):
    _l_(550196)

    def __init__(self, bot):
        _l_(550185)

        _n_(550182, "self", lambda: self).bot = _n_(550183, "bot", lambda: bot)
        _l_(550184)
    
    #Purge
    @_c_(550188, _a_(550187, _n_(550186, "commands", lambda: commands), "command"))
    async def purge(ctx, amount=10):
        _l_(550195)

        await _c_(550193, _a_(550191, _a_(550190, _n_(550189, "ctx", lambda: ctx), "channel"), "purge"), limit=_n_(550192, "amount", lambda: amount))
        _l_(550194)