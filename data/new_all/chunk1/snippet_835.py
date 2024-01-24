# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66274519/attributeerror-str-object-has-no-attribute-get-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(396307)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(396309)

except ImportError:
    pass

intents = _c_(396313, _a_(396312, _a_(396311, _n_(396310, "discord", lambda: discord), "Intents"), "default"))
_l_(396314)
_n_(396315, "intents", lambda: intents).members = True
_l_(396316)
Bot = _c_(396320, _a_(396318, _n_(396317, "commands", lambda: commands), "Bot"), command_prefix="&", intents=_n_(396319, "intents", lambda: intents))
_l_(396321)

@_a_(396323, _n_(396322, "Bot", lambda: Bot), "event")
async def on_ready():
    _l_(396334)

    await _c_(396329, _a_(396325, _n_(396324, "Bot", lambda: Bot), "change_presence"), activity=_c_(396328, _a_(396327, _n_(396326, "discord", lambda: discord), "Activity"), type=4, emoji="😁", name="hello")) # The error is related to this line
    _l_(396330) # The error is related to this line
    _c_(396332, _n_(396331, "print", lambda: print), "ready!")
    _l_(396333)

_c_(396338, _a_(396336, _n_(396335, "Bot", lambda: Bot), "run"), _n_(396337, "TOKEN", lambda: TOKEN))
_l_(396339)