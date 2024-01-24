# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63894385/i-keep-getting-the-attributeerror-bot-object-has-no-attribute-fetch-member
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Menu(_n_(631143, "ListPageSource", lambda: ListPageSource)):
    _l_(631238)

    def __init__(self, ctx, data):
        _l_(631152)

        _n_(631144, "self", lambda: self).ctx = _n_(631145, "ctx", lambda: ctx)
        _l_(631146)

        _c_(631150, _a_(631148, _n_(631147, "super", lambda: super)(), "__init__"), _n_(631149, "data", lambda: data), per_page=10)
        _l_(631151)

    async def write_page(self, menu, offset, fields=[]):
        _l_(631201)

        offset = (_a_(631154, _n_(631153, "menu", lambda: menu), "current_page")*_a_(631156, _n_(631155, "self", lambda: self), "per_page")) + 1
        _l_(631157)
        len_data = _c_(631161, _n_(631158, "len", lambda: len), _a_(631160, _n_(631159, "self", lambda: self), "entries"))
        _l_(631162)

        embed = _c_(631168, _n_(631163, "Embed", lambda: Embed), title="XP Leaderboard", description="See who is on top!", colour=_a_(631167, _a_(631166, _a_(631165, _n_(631164, "self", lambda: self), "ctx"), "author"), "colour"))
        _l_(631169)
        _c_(631177, _a_(631171, _n_(631170, "embed", lambda: embed), "set_thumbnail"), url=_a_(631176, _a_(631175, _a_(631174, _a_(631173, _n_(631172, "self", lambda: self), "ctx"), "guild"), "me"), "avatar_url"))
        _l_(631178)
        _c_(631189, _a_(631180, _n_(631179, "embed", lambda: embed), "set_footer"), text=f"{_n_(631181, 'offset', lambda: offset):,} - {_c_(631187, _n_(631182, 'min', lambda: min), _n_(631183, 'len_data', lambda: len_data), _n_(631184, 'offset', lambda: offset)+_a_(631186, _n_(631185, 'self', lambda: self), 'per_page')-1):,} of {_n_(631188, 'len_data', lambda: len_data):,} members.")
        _l_(631190)
        
        for name, value in _n_(631191, "fields", lambda: fields):
            _l_(631198)

            _c_(631196, _a_(631193, _n_(631192, "embed", lambda: embed), "add_field"), name=_n_(631194, "name", lambda: name), value=_n_(631195, "value", lambda: value), inline=False)
            _l_(631197)
        aux = _n_(631199, "embed", lambda: embed)
        _l_(631200)

        return aux

    async def format_page(self, menu, entries):
        _l_(631237)

        offset = (_a_(631203, _n_(631202, "menu", lambda: menu), "current_page")*_a_(631205, _n_(631204, "self", lambda: self), "per_page")) + 1
        _l_(631206)
        fields = []
        _l_(631207)
        table = _c_(631223, _a_(631208, "\n", "join"), (f"{_n_(631209, 'idx', lambda: idx)+_n_(631210, 'offset', lambda: offset)}. {_a_(631217, _c_(631216, _a_(631214, _a_(631213, _a_(631212, _n_(631211, 'self', lambda: self), 'ctx'), 'bot'), 'fetch_member'), _n_(631215, 'entry', lambda: entry)[0]), 'display_name')} (XP: {_n_(631218, 'entry', lambda: entry)[1]} | Level {_n_(631219, 'entry', lambda: entry)[2]})" 
                for idx, entry in _c_(631222, _n_(631220, "enumerate", lambda: enumerate), _n_(631221, "entries", lambda: entries))))
        _l_(631224)

        _c_(631228, _a_(631226, _n_(631225, "fields", lambda: fields), "append"), ("Ranks", _n_(631227, "table", lambda: table)))
        _l_(631229)
        aux = await _c_(631235, _a_(631231, _n_(631230, "self", lambda: self), "write_page"), _n_(631232, "menu", lambda: menu), _n_(631233, "offset", lambda: offset), _n_(631234, "fields", lambda: fields))
        _l_(631236)

        return aux