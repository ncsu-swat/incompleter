# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59754188/getting-attribute-error-module-mod-commands-has-no-attribute-ban-even-tho
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(421865)

except ImportError:
    pass
try:
    import programm
    _l_(421867)

except ImportError:
    pass

def createEmbed(guild, title, description, colour : _a_(421869, _n_(421868, "discord", lambda: discord), "colour")):
    _l_(421892)

    embed = _c_(421875, _a_(421871, _n_(421870, "discord", lambda: discord), "Embed"), title = _n_(421872, "title", lambda: title), description=_n_(421873, "description", lambda: description), colour=_n_(421874, "colour", lambda: colour))
    _l_(421876)
    _c_(421886, _a_(421878, _n_(421877, "embed", lambda: embed), "set_footer"), text=_a_(421880, _n_(421879, "guild", lambda: guild), "name") + '||%.2fs' % _c_(421883, _a_(421882, _n_(421881, "programm", lambda: programm), "getLatency")), icon_url=_a_(421885, _n_(421884, "guild", lambda: guild), "icon_url"))
    _l_(421887)
    _n_(421888, "embed", lambda: embed).type = 'rich'
    _l_(421889)
    aux = _n_(421890, "embed", lambda: embed)
    _l_(421891)
    return aux