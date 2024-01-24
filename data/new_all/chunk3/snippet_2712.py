# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65814425/discords-new-support-for-slash-commands-attributeerror-with-discord-py-slash
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(556160)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(556162)

except ImportError:
    pass
try:
    from discord_slash import SlashCommand
    _l_(556164)

except ImportError:
    pass
try:
    from discord_slash import SlashContext
    _l_(556166)

except ImportError:
    pass

bot = _c_(556173, _a_(556168, _n_(556167, "commands", lambda: commands), "Bot"), command_prefix="!", intents=_c_(556172, _a_(556171, _a_(556170, _n_(556169, "discord", lambda: discord), "Intents"), "all")))
_l_(556174)
slash = _c_(556177, _n_(556175, "SlashCommand", lambda: SlashCommand), _n_(556176, "bot", lambda: bot))
_l_(556178)


@_c_(556181, _a_(556180, _n_(556179, "slash", lambda: slash), "slash"), name="test")
async def _test(ctx: _n_(556182, "SlashContext", lambda: SlashContext)):
    _l_(556192)

    embed = _c_(556185, _a_(556184, _n_(556183, "discord", lambda: discord), "Embed"), title="embed test")
    _l_(556186)
    await _c_(556190, _a_(556188, _n_(556187, "ctx", lambda: ctx), "send"), content="test", embeds=[_n_(556189, "embed", lambda: embed)])
    _l_(556191)




_c_(556195, _a_(556194, _n_(556193, "bot", lambda: bot), "run"), ".token.txt")
_l_(556196)