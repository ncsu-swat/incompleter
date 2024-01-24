# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bot_utility
    _l_(434269)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(434271)

except ImportError:
    pass

async def ban(ctx, members, reason):
    _l_(434343)

    _c_(434273, _n_(434272, "print", lambda: print), 'command => mod_commands.ban')
    _l_(434274)
    bannableMembers = []
    _l_(434275)
    for member in _n_(434276, "members", lambda: members):
        _l_(434313)

        if_a_(434279, _a_(434278, _n_(434277, "member", lambda: member), "guild_permissions"), "administrator"):
            _l_(434312)

            await _c_(434286, _a_(434281, _n_(434280, "ctx", lambda: ctx), "send"), _c_(434285, _a_(434282, '{} kann nicht gebannt werden.', "format"), _a_(434284, _n_(434283, "member", lambda: member), "display_name")))
            _l_(434287)
        else:
            _c_(434291, _a_(434289, _n_(434288, "bannableMembers", lambda: bannableMembers), "append"), _n_(434290, "member", lambda: member))
            _l_(434292)
            embed = _c_(434298, _a_(434294, _n_(434293, "bot_utility", lambda: bot_utility), "createEmbed"), _a_(434296, _n_(434295, "ctx", lambda: ctx), "guild"), 'Du wurdest gebannt', 'Grund: ' + _n_(434297, "reason", lambda: reason), 0xFF0000)
            _l_(434299)
            await _c_(434303, _a_(434301, _n_(434300, "member", lambda: member), "send"), embed=_n_(434302, "embed", lambda: embed))
            _l_(434304)
            await _c_(434310, _a_(434307, _a_(434306, _n_(434305, "ctx", lambda: ctx), "guild"), "ban"), _n_(434308, "member", lambda: member), reason=_n_(434309, "reason", lambda: reason))
            _l_(434311)
    if(_n_(434314, "bannableMembers", lambda: bannableMembers) != None):
        _l_(434342)

        embed = _c_(434325, _a_(434316, _n_(434315, "bot_utility", lambda: bot_utility), "createEmbed"), _a_(434318, _n_(434317, "ctx", lambda: ctx), "guild"), 'Banns: (' + _c_(434323, _n_(434319, "str", lambda: str), _c_(434322, _n_(434320, "len", lambda: len), _n_(434321, "bannableMembers", lambda: bannableMembers))) + ')', 'Grund: ' + _n_(434324, "reason", lambda: reason), 0xff0000)
        _l_(434326)
        for member in _n_(434327, "bannableMembers", lambda: bannableMembers):
            _l_(434336)

            _c_(434334, _a_(434329, _n_(434328, "embed", lambda: embed), "add_field"), name=_a_(434331, _n_(434330, "member", lambda: member), "display_name"), value=_a_(434333, _n_(434332, "member", lambda: member), "id"))
            _l_(434335)
        await _c_(434340, _a_(434338, _n_(434337, "ctx", lambda: ctx), "send"), embed=_n_(434339, "embed", lambda: embed))
        _l_(434341)