# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59695431/nameerror-member-not-defined-with-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(577884, _a_(577883, _n_(577882, "client", lambda: client), "command"))
async def gift(ctx,*, member : _a_(577886, _n_(577885, "discord", lambda: discord), "Member")):
    _l_(577915)

    with _c_(577888, _n_(577887, "open", lambda: open), 'users.json', 'r') as f:
        _l_(577914)

        users = _c_(577892, _a_(577890, _n_(577889, "json", lambda: json), "load"), _n_(577891, "f", lambda: f))
        _l_(577893)

        await _c_(577898, _n_(577894, "update_data", lambda: update_data), _n_(577895, "users", lambda: users), _a_(577897, _n_(577896, "member", lambda: member), "id"))
        _l_(577899)
        await _c_(577904, _n_(577900, "add_coin", lambda: add_coin), _n_(577901, "users", lambda: users), _a_(577903, _n_(577902, "member", lambda: member), "id"), 1)
        _l_(577905)

        with _c_(577907, _n_(577906, "open", lambda: open), 'users.json', 'w') as f:
            _l_(577913)

            users = _c_(577911, _a_(577909, _n_(577908, "json", lambda: json), "dump"), _n_(577910, "f", lambda: f))
            _l_(577912)

async def update_data(users, user):
    _l_(577928)

    if not _a_(577917, _n_(577916, "member", lambda: member), "id") in _n_(577918, "users", lambda: users):
        _l_(577927)

        _n_(577919, "users", lambda: users)[_a_(577921, _n_(577920, "member", lambda: member), "id")] = {}
        _l_(577922)
        _n_(577923, "users", lambda: users)[_a_(577925, _n_(577924, "member", lambda: member), "id")]['coins'] = 0
        _l_(577926)

async def add_coin(users, user, coin):
    _l_(577941)

    _n_(577929, "users", lambda: users)[_a_(577931, _n_(577930, "member", lambda: member), "id")]['coins'] += _n_(577932, "coin", lambda: coin)
    _l_(577933)
    await _c_(577939, _a_(577935, _n_(577934, "ctx", lambda: ctx), "send"), f'{_a_(577937, _n_(577936, "member", lambda: member), "id")} has {_n_(577938, "coin", lambda: coin)} coins')
    _l_(577940)