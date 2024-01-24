# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import mod_commands
    _l_(465830)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(465832)

except ImportError:
    pass
try:
    import discord
    _l_(465834)

except ImportError:
    pass

bot = _c_(465838, _a_(465836, _n_(465835, "commands", lambda: commands), "Bot"), command_prefix='~',description=_n_(465837, "description", lambda: description))
_l_(465839)

@_c_(465842, _a_(465841, _n_(465840, "bot", lambda: bot), "command"), name='ban')
@_c_(465845, _a_(465844, _n_(465843, "commands", lambda: commands), "has_permissions"), ban_members=True)
@_c_(465848, _a_(465847, _n_(465846, "commands", lambda: commands), "bot_has_permissions"), ban_members=True)
async def ban(ctx, members : _a_(465850, _n_(465849, "commands", lambda: commands), "Greedy")[_a_(465852, _n_(465851, "discord", lambda: discord), "Member")], *, reason = 'Idiotisches Verhalten'):
    _l_(465860)

    await _c_(465858, _a_(465854, _n_(465853, "mod_commands", lambda: mod_commands), "ban"), _n_(465855, "ctx", lambda: ctx), _n_(465856, "members", lambda: members), _n_(465857, "reason", lambda: reason))
    _l_(465859)

def getLatency():
    _l_(465864)

    aux = _a_(465862, _n_(465861, "bot", lambda: bot), "latency")
    _l_(465863)
    return aux

_c_(465868, _a_(465866, _n_(465865, "bot", lambda: bot), "run"), _n_(465867, "TOKEN", lambda: TOKEN))
_l_(465869)