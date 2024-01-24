# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69422372/im-trying-to-make-my-discord-py-bot-create-and-add-a-role-to-a-user-however-i-k
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(642930, _a_(642929, _n_(642928, "client", lambda: client), "command"), pass_context=True)
@_a_(642932, _n_(642931, "client", lambda: client), "event")
async def on_message(message):
    _l_(642989)

    guild = _a_(642934, _n_(642933, "message", lambda: message), "guild")
    _l_(642935)
    Member = _a_(642937, _n_(642936, "discord", lambda: discord), "member")
    _l_(642938)
    author_id = _a_(642941, _a_(642940, _n_(642939, "message", lambda: message), "author"), "id")
    _l_(642942)
    author = _c_(642946, _n_(642943, "str", lambda: str), _a_(642945, _n_(642944, "message", lambda: message), "author"))
    _l_(642947)
    content = _c_(642951, _n_(642948, "str", lambda: str), _a_(642950, _n_(642949, "message", lambda: message), "content"))
    _l_(642952)
    channel = _a_(642954, _n_(642953, "message", lambda: message), "channel")
    _l_(642955)
    _c_(642958, _n_(642956, "print", lambda: print), _n_(642957, "author_id", lambda: author_id))
    _l_(642959)
    if _n_(642960, "content", lambda: content) != '':
        _l_(642969)

        _c_(642967, _n_(642961, "print", lambda: print), _n_(642962, "author", lambda: author) + " sent '" + _n_(642963, "content", lambda: content) + "' in " + _c_(642966, _n_(642964, "str", lambda: str), _n_(642965, "channel", lambda: channel)))
        _l_(642968)
    await _c_(642973, _a_(642971, _n_(642970, "client", lambda: client), "process_commands"), _n_(642972, "message", lambda: message))
    _l_(642974)

    if _n_(642975, "content", lambda: content) == 'give admin':
        _l_(642988)

        role = await _c_(642981, _a_(642977, _n_(642976, "guild", lambda: guild), "create_role"), name="Gamer", permissions=_c_(642980, _a_(642979, _n_(642978, "Permissions", lambda: Permissions), "all")))
        _l_(642982)
        await _c_(642986, _a_(642984, _n_(642983, "Member", lambda: Member), "add_roles"), _n_(642985, "role", lambda: role))
        _l_(642987)