# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68656152/command-raised-an-exception-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(646386, _a_(646385, _n_(646384, "client", lambda: client), "command"), aliases=["lb"])
async def leaderboardie(ctx, x=1):
    _l_(646455)

    users = await _c_(646388, _n_(646387, "get_bank_data", lambda: get_bank_data))
    _l_(646389)
    leader_board = {}
    _l_(646390)
    total = []
    _l_(646391)
    for user in _n_(646392, "users", lambda: users):
        _l_(646411)

        name = _c_(646395, _n_(646393, "int", lambda: int), _n_(646394, "user", lambda: user))
        _l_(646396)
        total_amount = _n_(646397, "users", lambda: users)[_n_(646398, "user", lambda: user)]["wallet"] + _n_(646399, "users", lambda: users)[_n_(646400, "user", lambda: user)]["bank"]
        _l_(646401)
        _n_(646402, "leader_board", lambda: leader_board)[_n_(646403, "total_amount", lambda: total_amount)] = _n_(646404, "name", lambda: name)
        _l_(646405)
        _c_(646409, _a_(646407, _n_(646406, "total", lambda: total), "append"), _n_(646408, "total_amount", lambda: total_amount))
        _l_(646410)

    total = _c_(646414, _n_(646412, "sorted", lambda: sorted), _n_(646413, "total", lambda: total), reverse=True)
    _l_(646415)

    em = _c_(646422, _a_(646417, _n_(646416, "discord", lambda: discord), "Embed"), title=f"Top {_n_(646418, 'x', lambda: x)} Richest People",
                       description="This is decided on the basis of raw money in the bank and wallet", color=_c_(646421, _a_(646420, _n_(646419, "discord", lambda: discord), "Color"), 0xfa43ee))
    _l_(646423)
    index = 1
    _l_(646424)
    for amt in _n_(646425, "total", lambda: total):
        _l_(646449)

        id_ = _n_(646426, "leader_board", lambda: leader_board)[_n_(646427, "amt", lambda: amt)]
        _l_(646428)
        member = _c_(646432, _a_(646430, _n_(646429, "client", lambda: client), "get_user"), _n_(646431, "id_", lambda: id_))
        _l_(646433)
        name = _a_(646435, _n_(646434, "member", lambda: member), "name")
        _l_(646436)
        _c_(646442, _a_(646438, _n_(646437, "em", lambda: em), "add_field"), name=f"{_n_(646439, 'index', lambda: index)}. {_n_(646440, 'name', lambda: name)}", value=f"{_n_(646441, 'amt', lambda: amt)}",  inline=False)
        _l_(646443)
        if _n_(646444, "index", lambda: index) == _n_(646445, "x", lambda: x):
            _l_(646448)

            break
            _l_(646446)
        else:
            index += 1
            _l_(646447)

    await _c_(646453, _a_(646451, _n_(646450, "ctx", lambda: ctx), "send"), embed=_n_(646452, "em", lambda: em))
    _l_(646454)