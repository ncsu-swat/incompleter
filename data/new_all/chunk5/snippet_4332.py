# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59502253/i-cant-use-bot-commands-and-typeerror-property-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(656175, _n_(656174, "manage", lambda: manage), "py")
_l_(656176)
try:
    import discord
    _l_(656178)

except ImportError:
    pass
try:
    import asyncio
    _l_(656180)

except ImportError:
    pass
try:
    import re
    _l_(656182)

except ImportError:
    pass
try:
    import json
    _l_(656184)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(656186)

except ImportError:
    pass
try:
    from discord import Permissions as permissions
    _l_(656188)

except ImportError:
    pass

class manage(_a_(656190, _n_(656189, "commands", lambda: commands), "Cog")):
    _l_(656247)

    def __init__(self, bot):
        _l_(656194)

        _n_(656191, "self", lambda: self).bot = _n_(656192, "bot", lambda: bot)
        _l_(656193)

    @_c_(656197, _a_(656196, _n_(656195, "commands", lambda: commands), "command"))
    @_c_(656200, _a_(656199, _n_(656198, "commands", lambda: commands), "guild_only"))
    @_c_(656203, _a_(656202, _n_(656201, "permissions", lambda: permissions), "administrator"))
    async def prefix(self, ctx, *, prefixes=""):
        _l_(656246)

        try:
            _l_(656219)

            with _c_(656205, _n_(656204, "open", lambda: open), 'config/setting.json') as json_file:
                _l_(656213)

                json_data = _c_(656209, _a_(656207, _n_(656206, "json", lambda: json), "load"), _n_(656208, "json_file", lambda: json_file))
                _l_(656210)
                prefix = _n_(656211, "json_data", lambda: json_data)["prefix"]
                _l_(656212)
        except:
            _l_(656218)

            await _c_(656216, _a_(656215, _n_(656214, "ctx", lambda: ctx), "send"), "An error occured.(Bot has an error.)")
            _l_(656217)
        if(_n_(656220, "prefixes", lambda: prefixes) != ""):
            _l_(656245)

            try:
                _l_(656244)

                custom_prefixes = _n_(656221, "prefixes", lambda: prefixes)
                _l_(656222)
                _n_(656223, "custom_prefixes", lambda: custom_prefixes)[_a_(656226, _a_(656225, _n_(656224, "ctx", lambda: ctx), "guild"), "id")] = _c_(656229, _a_(656228, _n_(656227, "prefixes", lambda: prefixes), "split")) or _n_(656230, "prefix", lambda: prefix)
                _l_(656231)
                await _c_(656237, _a_(656233, _n_(656232, "ctx", lambda: ctx), "send"), _c_(656236, _a_(656234, "Changed prefix. Now new prefix is **{}**.", "format"), _n_(656235, "custom_prefixes", lambda: custom_prefixes)))
                _l_(656238)
            except:
                _l_(656243)

                await _c_(656241, _a_(656240, _n_(656239, "ctx", lambda: ctx), "send"), "An error occured.(Check your command or bot has an error.)")
                _l_(656242)
def setup(bot):
    _l_(656255)

    _c_(656253, _a_(656249, _n_(656248, "bot", lambda: bot), "add_cog"), _c_(656252, _n_(656250, "manage", lambda: manage), _n_(656251, "bot", lambda: bot)))
    _l_(656254)