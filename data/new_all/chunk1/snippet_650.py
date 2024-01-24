# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71369200/pycord-error-discord-errors-extensionfailed-extension-cogs-cmds-raised-an-er
# cogs/cmds.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(403330)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(403332)

except ImportError:
    pass

class Cmds(_a_(403334, _n_(403333, "commands", lambda: commands), "Cog")):
    _l_(403349)

    def __init__(self, bot):
        _l_(403338)

        _n_(403335, "self", lambda: self).bot = _n_(403336, "bot", lambda: bot)
        _l_(403337)

    @_c_(403341, _a_(403340, _n_(403339, "commands", lambda: commands), "command"))
    async def echo(self, ctx, msg:_n_(403342, "str", lambda: str)):
        _l_(403348)

        """Sends the specified text in the chat"""

        await _c_(403346, _a_(403344, _n_(403343, "ctx", lambda: ctx), "send"), _n_(403345, "msg", lambda: msg))
        _l_(403347)

def setup(bot):
    _l_(403357)

    _c_(403355, _a_(403351, _n_(403350, "bot", lambda: bot), "add_cog"), _c_(403354, _n_(403352, "Cmds", lambda: Cmds), _n_(403353, "bot", lambda: bot)))
    _l_(403356)