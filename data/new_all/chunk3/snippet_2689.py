# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66682539/economy-bot-discord-py-rewrite-leaderboard-error-attributeerror-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(526617, _a_(526616, _n_(526615, "client", lambda: client), "command"), aliases = ["lb"])
async def leaderboard(ctx,x: _n_(526618, "int", lambda: int) = 10):
    _l_(526688)

    users = await _c_(526620, _n_(526619, "get_bank_data", lambda: get_bank_data))
    _l_(526621)
    leader_board = {}
    _l_(526622)
    total = []
    _l_(526623)
    for user in _n_(526624, "users", lambda: users):
        _l_(526643)

        name = _c_(526627, _n_(526625, "int", lambda: int), _n_(526626, "user", lambda: user))
        _l_(526628)
        total_amount = _n_(526629, "users", lambda: users)[_n_(526630, "user", lambda: user)]["wallet"] + _n_(526631, "users", lambda: users)[_n_(526632, "user", lambda: user)]["bank"]
        _l_(526633)
        _n_(526634, "leader_board", lambda: leader_board)[_n_(526635, "total_amount", lambda: total_amount)] = _n_(526636, "name", lambda: name)
        _l_(526637)
        _c_(526641, _a_(526639, _n_(526638, "total", lambda: total), "append"), _n_(526640, "total_amount", lambda: total_amount))
        _l_(526642)

    total = _c_(526646, _n_(526644, "sorted", lambda: sorted), _n_(526645, "total", lambda: total), reverse=True)
    _l_(526647)

    em = _c_(526654, _a_(526649, _n_(526648, "discord", lambda: discord), "Embed"), title=f"Top {_n_(526650, 'x', lambda: x)} Richest People", color=_c_(526653, _a_(526652, _n_(526651, "random", lambda: random), "randint"), 0, 0xffffff))
    _l_(526655)
    index = 1
    _l_(526656)
    for amt in _n_(526657, "total", lambda: total):
        _l_(526682)

        id_ = _n_(526658, "leader_board", lambda: leader_board)[_n_(526659, "amt", lambda: amt)]
        _l_(526660)
        member = _c_(526665, _a_(526663, _a_(526662, _n_(526661, "ctx", lambda: ctx), "guild"), "get_member"), _n_(526664, "id_", lambda: id_))
        _l_(526666)
        name = _a_(526668, _n_(526667, "member", lambda: member), "name")
        _l_(526669)
        _c_(526675, _a_(526671, _n_(526670, "em", lambda: em), "add_field"), name=f"{_n_(526672, 'index', lambda: index)}. {_n_(526673, 'name', lambda: name)}", value=f"{_n_(526674, 'amt', lambda: amt)}", inline=False)
        _l_(526676)
        if _n_(526677, "index", lambda: index) == _n_(526678, "x", lambda: x):
            _l_(526681)

            break
            _l_(526679)
        else:
            index += 1
            _l_(526680)
    await _c_(526686, _a_(526684, _n_(526683, "ctx", lambda: ctx), "send"), embed=_n_(526685, "em", lambda: em))
    _l_(526687)