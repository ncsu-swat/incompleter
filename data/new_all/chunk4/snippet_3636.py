# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70917965/attributeerror-interaction-object-has-no-attribute-author
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(643663, _a_(643661, _n_(643660, "bot", lambda: bot), "slash_command"), name='credits', description='Checks social credit score', guild_ids=_n_(643662, "guild_id", lambda: guild_id))
async def creds(message):
    _l_(643682)

    member_data = _c_(643668, _n_(643664, "load_member_data", lambda: load_member_data), _a_(643667, _a_(643666, _n_(643665, "message", lambda: message), "author"), "id"))
    _l_(643669)
    await _c_(643680, _a_(643672, _a_(643671, _n_(643670, "message", lambda: message), "channel"), "send"), f"{_a_(643675, _a_(643674, _n_(643673, 'message', lambda: message), 'author'), 'mention')} has "+ _c_(643679, _n_(643676, "str", lambda: str), _a_(643678, _n_(643677, "member_data", lambda: member_data), "wallet")) +" Social Credit Points")
    _l_(643681)