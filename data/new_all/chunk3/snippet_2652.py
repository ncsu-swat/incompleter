# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67911019/discord-py-blacklist-cog-listener-flagging-error-typeerror-str-object-not-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(556345, _a_(556344, _a_(556343, _n_(556342, "commands", lambda: commands), "Cog"), "listener"))
async def on_message(self, message):
    _l_(556360)

    """Deletes a messaged that contains a blacklisted word"""

    msg = _c_(556348, _a_(556347, _n_(556346, "message", lambda: message), "content"))
    _l_(556349)

    for word in _n_(556350, "msg", lambda: msg):
        _l_(556359)


        if _c_(556353, _a_(556352, _n_(556351, "msg", lambda: msg), "find"), "blacklist") != -1:
            _l_(556358)


            await _c_(556356, _a_(556355, _n_(556354, "message", lambda: message), "delete"))
            _l_(556357)