# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56369406/discord-bot-attributeerror-client-object-has-no-attribute-commands
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(552647)

except ImportError:
    pass
try:
    import asyncio
    _l_(552649)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(552651)

except ImportError:
    pass
try:
    from discord.ext.commands import Bot
    _l_(552653)

except ImportError:
    pass

TOKEN = [_n_(552654, "REDACTED", lambda: REDACTED)]
_l_(552655)



# client = discord.Client()

client = _c_(552657, _n_(552656, "Bot", lambda: Bot), "!")
_l_(552658)

@_a_(552660, _n_(552659, "client", lambda: client), "event")
async def on_message(message):
    _l_(552692)

    # we do not want the bot to reply to itself
    if _a_(552662, _n_(552661, "message", lambda: message), "author") == _a_(552664, _n_(552663, "client", lambda: client), "user"):
        _l_(552666)

        aux = ""
        _l_(552665)
        return aux

    if _c_(552670, _a_(552669, _a_(552668, _n_(552667, "message", lambda: message), "content"), "startswith"), '!hello'):
        _l_(552691)

        @_c_(552673, _a_(552672, _n_(552671, "client", lambda: client), "command"), pass_context=True)
        async def broadcast(ctx, *, msg):
            _l_(552690)

            for server in _a_(552675, _n_(552674, "bot", lambda: bot), "guilds"):
                _l_(552689)

                for channel in _a_(552677, _n_(552676, "server", lambda: server), "channels"):
                    _l_(552688)

                    try:
                        _l_(552687)

                        await _c_(552681, _a_(552679, _n_(552678, "channel", lambda: channel), "send"), _n_(552680, "msg", lambda: msg))
                        _l_(552682)
                    except _n_(552683, "Exception", lambda: Exception):
                        _l_(552685)

                        continue
                        _l_(552684)
                    else:
                        break
                        _l_(552686)