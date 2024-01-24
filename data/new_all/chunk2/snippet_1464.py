# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55593121/typeerror-tuple-indices-must-be-integers-or-slices-not-str-in-command
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(460338, _a_(460337, _n_(460336, "checks", lambda: checks), "can_embed"))
@_c_(460341, _a_(460340, _n_(460339, "commands", lambda: commands), "command"), name="botinfo")
async def botinfo(self, ctx: _n_(460342, "UKGCtx", lambda: UKGCtx)):
    _l_(460388)

    """Shows advanced information about the bot."""
    char_count = 0
    _l_(460343)
    deaths_count = 0
    _l_(460344)
    levels_count = 0
    _l_(460345)
    with _c_(460350, _n_(460346, "closing", lambda: closing), _c_(460349, _a_(460348, _n_(460347, "userDatabase", lambda: userDatabase), "cursor"))) as c:
        _l_(460387)

        _c_(460353, _a_(460352, _n_(460351, "c", lambda: c), "execute"), "SELECT COUNT(*) as count FROM chars")
        _l_(460354)
        result = _c_(460357, _a_(460356, _n_(460355, "c", lambda: c), "fetchone"))
        _l_(460358)
        if _n_(460359, "result", lambda: result) is not None:
            _l_(460362)

            char_count = _n_(460360, "result", lambda: result)["count"]
            _l_(460361)
        _c_(460365, _a_(460364, _n_(460363, "c", lambda: c), "execute"), "SELECT COUNT(*) as count FROM char_deaths")
        _l_(460366)
        result = _c_(460369, _a_(460368, _n_(460367, "c", lambda: c), "fetchone"))
        _l_(460370)
        if _n_(460371, "result", lambda: result) is not None:
            _l_(460374)

            deaths_count = _n_(460372, "result", lambda: result)["count"]
            _l_(460373)
        _c_(460377, _a_(460376, _n_(460375, "c", lambda: c), "execute"), "SELECT COUNT(*) as count FROM char_levelups")
        _l_(460378)
        result = _c_(460381, _a_(460380, _n_(460379, "c", lambda: c), "fetchone"))
        _l_(460382)
        if _n_(460383, "result", lambda: result) is not None:
            _l_(460386)

            levels_count = _n_(460384, "result", lambda: result)["count"]
            _l_(460385)