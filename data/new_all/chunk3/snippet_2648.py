# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67974081/attributeerror-module-embed-storage-has-no-attribute-help-command
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(572267)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(572269)

except ImportError:
    pass
try:
    import gsheet
    _l_(572271)

except ImportError:
    pass
try:
    import os
    _l_(572273)

except ImportError:
    pass
try:
    import embed_storage
    _l_(572275)

except ImportError:
    pass

async def help(ctx, argument='Helping'):
    _l_(572284)

    await _c_(572282, _a_(572277, _n_(572276, "ctx", lambda: ctx), "send"), embed=_c_(572281, _a_(572279, _n_(572278, "embed_storage", lambda: embed_storage), "help_command"), 'stargazer', _n_(572280, "argument", lambda: argument)))
    _l_(572283)