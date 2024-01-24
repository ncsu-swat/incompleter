# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59502253/i-cant-use-bot-commands-and-typeerror-property-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(672204, _n_(672203, "manage", lambda: manage), "py")
_l_(672205)
try:
    import discord
    _l_(672207)

except ImportError:
    pass
try:
    import asyncio
    _l_(672209)

except ImportError:
    pass
try:
    import re
    _l_(672211)

except ImportError:
    pass
try:
    import json
    _l_(672213)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(672215)

except ImportError:
    pass
try:
    from discord import Permissions as permissions
    _l_(672217)

except ImportError:
    pass

class manage(_a_(672219, _n_(672218, "commands", lambda: commands), "Cog")):
    _l_(672276)

    def __init__(self, bot):
        _l_(672223)

        _n_(672220, "self", lambda: self).bot = _n_(672221, "bot", lambda: bot)
        _l_(672222)

    @_c_(672226, _a_(672225, _n_(672224, "commands", lambda: commands), "command"))
    @_c_(672229, _a_(672228, _n_(672227, "commands", lambda: commands), "guild_only"))
    @_c_(672232, _a_(672231, _n_(672230, "permissions", lambda: permissions), "administrator"))
    async def prefix(self, ctx, *, prefixes=""):
        _l_(672275)

        try:
            _l_(672248)

            with _c_(672234, _n_(672233, "open", lambda: open), 'config/setting.json') as json_file:
                _l_(672242)

                json_data = _c_(672238, _a_(672236, _n_(672235, "json", lambda: json), "load"), _n_(672237, "json_file", lambda: json_file))
                _l_(672239)
                prefix = _n_(672240, "json_data", lambda: json_data)["prefix"]
                _l_(672241)
        except:
            _l_(672247)

            await _c_(672245, _a_(672244, _n_(672243, "ctx", lambda: ctx), "send"), "An error occured.(Bot has an error.)")
            _l_(672246)
        if(_n_(672249, "prefixes", lambda: prefixes) != ""):
            _l_(672274)

            try:
                _l_(672273)

                custom_prefixes = _n_(672250, "prefixes", lambda: prefixes)
                _l_(672251)
                _n_(672252, "custom_prefixes", lambda: custom_prefixes)[_a_(672255, _a_(672254, _n_(672253, "ctx", lambda: ctx), "guild"), "id")] = _c_(672258, _a_(672257, _n_(672256, "prefixes", lambda: prefixes), "split")) or _n_(672259, "prefix", lambda: prefix)
                _l_(672260)
                await _c_(672266, _a_(672262, _n_(672261, "ctx", lambda: ctx), "send"), _c_(672265, _a_(672263, "Changed prefix. Now new prefix is **{}**.", "format"), _n_(672264, "custom_prefixes", lambda: custom_prefixes)))
                _l_(672267)
            except:
                _l_(672272)

                await _c_(672270, _a_(672269, _n_(672268, "ctx", lambda: ctx), "send"), "An error occured.(Check your command or bot has an error.)")
                _l_(672271)
def setup(bot):
    _l_(672284)

    _c_(672282, _a_(672278, _n_(672277, "bot", lambda: bot), "add_cog"), _c_(672281, _n_(672279, "manage", lambda: manage), _n_(672280, "bot", lambda: bot)))
    _l_(672283)