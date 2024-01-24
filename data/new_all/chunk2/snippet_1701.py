# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62250609/attributeerror-levelingsystem-object-has-no-attribute-author
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(434601)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(434603)

except ImportError:
    pass
try:
    from discord.utils import get
    _l_(434605)

except ImportError:
    pass
try:
    import json
    _l_(434607)

except ImportError:
    pass
try:
    import random
    _l_(434609)

except ImportError:
    pass
try:
    import time
    _l_(434611)

except ImportError:
    pass


class LevelingSystem(_a_(434613, _n_(434612, "commands", lambda: commands), "Cog")):
    _l_(434674)

    """ Leveling system for discord """

    def __init__(self, bot):
        _l_(434617)

        _n_(434614, "self", lambda: self).bot = _n_(434615, "bot", lambda: bot)
        _l_(434616)

    @_c_(434621, _a_(434620, _a_(434619, _n_(434618, "commands", lambda: commands), "Cog"), "listener"))
    async def on_message(message, guild):
        _l_(434673)


        if _a_(434624, _a_(434623, _n_(434622, "message", lambda: message), "author"), "bot"):
            _l_(434641)

            aux = ""
            _l_(434625)
            return aux
        else:
            with _c_(434627, _n_(434626, "open", lambda: open), "X:\\Code\\Projects\\Python\\AlphaWolf\\cogs\\levels.json", 'r') as f:
                _l_(434633)

                levels = _c_(434631, _a_(434629, _n_(434628, "json", lambda: json), "load"), _n_(434630, "f", lambda: f))
                _l_(434632)

            await _c_(434639, _n_(434634, "update_data", lambda: update_data), _n_(434635, "levels", lambda: levels), _a_(434638, _a_(434637, _n_(434636, "message", lambda: message), "author"), "id"))
            _l_(434640)

        async def update_data(levels, user):
            _l_(434672)

            for member in _a_(434643, _n_(434642, "guild", lambda: guild), "members"):
                _l_(434671)

                if _n_(434644, "user", lambda: user) not in _n_(434645, "levels", lambda: levels):
                    _l_(434670)

                    _n_(434646, "levels", lambda: levels)[_n_(434647, "user", lambda: user)] = {}
                    _l_(434648)
                    _n_(434649, "levels", lambda: levels)[_n_(434650, "user", lambda: user)]["experience"] = 0
                    _l_(434651)
                    _n_(434652, "levels", lambda: levels)[_n_(434653, "user", lambda: user)]["level"] = 1
                    _l_(434654)
                    _c_(434659, _n_(434655, "print", lambda: print), _c_(434658, _a_(434656, " Registered {} to .json", "format"), _n_(434657, "user", lambda: user)))
                    _l_(434660)
                    with _c_(434662, _n_(434661, "open", lambda: open), "X:\\Code\\Projects\\Python\\AlphaWolf\\cogs\\levels.json", 'w') as f:
                        _l_(434669)

                        _c_(434667, _a_(434664, _n_(434663, "json", lambda: json), "dump"), _n_(434665, "levels", lambda: levels), _n_(434666, "f", lambda: f))
                        _l_(434668)

def setup(bot):
    _l_(434682)

    _c_(434680, _a_(434676, _n_(434675, "bot", lambda: bot), "add_cog"), _c_(434679, _n_(434677, "LevelingSystem", lambda: LevelingSystem), _n_(434678, "bot", lambda: bot)))
    _l_(434681)