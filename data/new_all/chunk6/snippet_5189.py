# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63565924/typeerror-module-object-is-not-callable-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(336642)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot
    _l_(336644)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(336646)

except ImportError:
    pass

client = _c_(336649, _a_(336648, _n_(336647, "commands", lambda: commands), "bot"), command_prefix = ".")
_l_(336650)

@_a_(336652, _n_(336651, "client", lambda: client), "event")
async def on_ready():
    _l_(336656)

    _c_(336654, _n_(336653, "print", lambda: print), "I'm in!")
    _l_(336655)


@_a_(336658, _n_(336657, "client", lambda: client), "event")
async def on_message(message):
    _l_(336680)

    _c_(336662, _n_(336659, "print", lambda: print), _a_(336661, _n_(336660, "message", lambda: message), "content"))
    _l_(336663)
    if _a_(336665, _n_(336664, "message", lambda: message), "author") == _a_(336667, _n_(336666, "client", lambda: client), "user"):
        _l_(336669)

        aux = ""
        _l_(336668)
        return aux
    
    if _c_(336673, _a_(336672, _a_(336671, _n_(336670, "message", lambda: message), "content"), "startswith"), "hello"):
        _l_(336679)

        await _c_(336677, _a_(336676, _a_(336675, _n_(336674, "message", lambda: message), "channel"), "send"), 'hello!')
        _l_(336678)

@_a_(336682, _n_(336681, "client", lambda: client), "event")
async def on_member_join(member):
    _l_(336686)

    _c_(336684, _n_(336683, "print", lambda: print), "someone's here!")
    _l_(336685)


@_a_(336688, _n_(336687, "client", lambda: client), "event")
async def on_typing(channel, user, when):
    _l_(336692)

    _c_(336690, _n_(336689, "print", lambda: print), "Lol, someone is typing!!1!")
    _l_(336691)

@_c_(336695, _a_(336694, _n_(336693, "client", lambda: client), "command"))
async def answer(ans):
    _l_(336700)

    await _c_(336698, _a_(336697, _n_(336696, "ans", lambda: ans), "send"), "Here is your answer")
    _l_(336699)