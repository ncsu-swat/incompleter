# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65002409/typeerror-event-registered-must-be-a-coroutine-function-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord, asyncio, time, discord.guild, random, os, youtube_dl
    _l_(454852)

except ImportError:
    pass
try:
    import os
    _l_(454854)

except ImportError:
    pass
try:
    import asyncio
    _l_(454856)

except ImportError:
    pass
try:
    import math
    _l_(454858)

except ImportError:
    pass
try:
    import random
    _l_(454860)

except ImportError:
    pass
try:
    import youtube_dl
    _l_(454862)

except ImportError:
    pass
try:
    import json
    _l_(454864)

except ImportError:
    pass
try:
    from discord.ext import commands, tasks
    _l_(454866)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot, guild_only
    _l_(454868)

except ImportError:
    pass
try:
    from itertools import cycle
    _l_(454870)

except ImportError:
    pass


def get_prefix(client, message):
    _l_(454886)

    with _c_(454872, _n_(454871, "open", lambda: open), 'prefixes.json', 'r') as f:
        _l_(454885)

        prefixes = _c_(454876, _a_(454874, _n_(454873, "json", lambda: json), "load"), _n_(454875, "f", lambda: f))
        _l_(454877)
        aux = _n_(454878, "prefixes", lambda: prefixes)[_c_(454883, _n_(454879, "str", lambda: str), _a_(454882, _a_(454881, _n_(454880, "message", lambda: message), "guild"), "id"))]
        _l_(454884)


        return aux