# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70618400/typeerror-greedystr-is-invalid-discord-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(385371, _a_(385370, _n_(385369, "commands", lambda: commands), "command"))
async def temp(self, ctx: _a_(385373, _n_(385372, "commands", lambda: commands), "Context"), *arg):
    _l_(385405)

    user_id = _c_(385377, _a_(385375, _n_(385374, "re", lambda: re), "findall"), r'(?<=<@)[!&]?(\d{17,22})(?=> *$)', _n_(385376, "arg", lambda: arg)[-1])
    _l_(385378)
    if _c_(385381, _n_(385379, "len", lambda: len), _n_(385380, "user_id", lambda: user_id) ) == 0:
        _l_(385385)

        raise _c_(385383, _n_(385382, "TypeError", lambda: TypeError), 'Command "temp" missing 1 required positional argument: "user"')
        _l_(385384)
    user = _c_(385392, _a_(385388, _a_(385387, _n_(385386, "ctx", lambda: ctx), "guild"), "get_member"), _c_(385391, _n_(385389, "int", lambda: int), _n_(385390, "user_id", lambda: user_id)[0]))
    _l_(385393)
    message = _c_(385396, _a_(385394, ' ', "join"), _n_(385395, "arg", lambda: arg)[:-1])
    _l_(385397)
    await _c_(385403, _a_(385399, _n_(385398, "ctx", lambda: ctx), "send"), f'{_n_(385400, "message", lambda: message) = }, {_a_(385402, _n_(385401, "user", lambda: user), "mention")}')
    _l_(385404)