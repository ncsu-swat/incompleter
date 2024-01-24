# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70186078/typeerror-event-missing-1-required-positional-argument-coro
# -*- coding: utf-8 -*-

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(373482)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(373484)

except ImportError:
    pass
try:
    from config import  token
    _l_(373486)

except ImportError:
    pass
try:
    import  youtube_dl
    _l_(373488)

except ImportError:
    pass
try:
    import os
    _l_(373490)

except ImportError:
    pass

bot = _c_(373493, _a_(373492, _n_(373491, "commands", lambda: commands), "Bot"), command_prefix='!')
_l_(373494)

@_a_(373496, _n_(373495, "bot", lambda: bot), "event")
async def on_ready():
    _l_(373500)

    _c_(373498, _n_(373497, "print", lambda: print), 'bot online!')
    _l_(373499)

@_c_(373503, _a_(373502, _n_(373501, "bot", lambda: bot), "event"))
async def on_message():
    _l_(373507)

    _c_(373505, _n_(373504, "print", lambda: print), 'New Message!')
    _l_(373506)

_c_(373511, _a_(373509, _n_(373508, "bot", lambda: bot), "run"), _n_(373510, "token", lambda: token))
_l_(373512)