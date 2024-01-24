# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63565924/typeerror-module-object-is-not-callable-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(361329)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot
    _l_(361331)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(361333)

except ImportError:
    pass

client = _c_(361336, _a_(361335, _n_(361334, "commands", lambda: commands), "bot"), command_prefix = ".")
_l_(361337)

@_a_(361339, _n_(361338, "client", lambda: client), "event")
async def on_ready():
    _l_(361343)

    _c_(361341, _n_(361340, "print", lambda: print), "I'm in!")
    _l_(361342)


@_a_(361345, _n_(361344, "client", lambda: client), "event")
async def on_message(message):
    _l_(361367)

    _c_(361349, _n_(361346, "print", lambda: print), _a_(361348, _n_(361347, "message", lambda: message), "content"))
    _l_(361350)
    if _a_(361352, _n_(361351, "message", lambda: message), "author") == _a_(361354, _n_(361353, "client", lambda: client), "user"):
        _l_(361356)

        aux = ""
        _l_(361355)
        return aux
    
    if _c_(361360, _a_(361359, _a_(361358, _n_(361357, "message", lambda: message), "content"), "startswith"), "hello"):
        _l_(361366)

        await _c_(361364, _a_(361363, _a_(361362, _n_(361361, "message", lambda: message), "channel"), "send"), 'hello!')
        _l_(361365)

@_a_(361369, _n_(361368, "client", lambda: client), "event")
async def on_member_join(member):
    _l_(361373)

    _c_(361371, _n_(361370, "print", lambda: print), "someone's here!")
    _l_(361372)


@_a_(361375, _n_(361374, "client", lambda: client), "event")
async def on_typing(channel, user, when):
    _l_(361379)

    _c_(361377, _n_(361376, "print", lambda: print), "Lol, someone is typing!!1!")
    _l_(361378)

@_c_(361382, _a_(361381, _n_(361380, "client", lambda: client), "command"))
async def answer(ans):
    _l_(361387)

    await _c_(361385, _a_(361384, _n_(361383, "ans", lambda: ans), "send"), "Here is your answer")
    _l_(361386)