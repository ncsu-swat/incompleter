# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70113301/typeerror-module-object-is-not-callable-on-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from discord.ext import commands
    _l_(543308)

except ImportError:
    pass

token = 'token goess here'
_l_(543309)

client = _c_(543312, _a_(543311, _n_(543310, "commands", lambda: commands), "bot"), command_prefix = '__')
_l_(543313)

@_a_(543315, _n_(543314, "client", lambda: client), "event")
async def on_ready():
    _l_(543319)

    _c_(543317, _n_(543316, "print", lambda: print), 'Bot is ready')
    _l_(543318)

_c_(543323, _a_(543321, _n_(543320, "client", lambda: client), "run"), _n_(543322, "token", lambda: token))
_l_(543324)