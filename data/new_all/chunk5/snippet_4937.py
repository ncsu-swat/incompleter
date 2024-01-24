# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39553483/attributeerror-module-discordoragisearch-has-no-attribute-isvalidmessage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import DiscordoragiSearch
    _l_(665551)

except ImportError:
    pass

...
_l_(665552)

@_a_(665555, _a_(665554, _n_(665553, "Discord", lambda: Discord), "client"), "event")
async def on_message(message):
    _l_(665594)

    _c_(665557, _n_(665556, "print", lambda: print), 'Message recieved')
    _l_(665558)
    #Is the message valid (i.e. it's not made by Discordoragi and I haven't seen it already). If no, try to add it to the "already seen pile" and skip to the next message. If yes, keep going.
    if not _c_(665562, _a_(665560, _n_(665559, "DiscordoragiSearch", lambda: DiscordoragiSearch), "isValidMessage"), _n_(665561, "message", lambda: message)):
        _l_(665593)

        try:
            _l_(665588)

            if not _c_(665567, _a_(665564, _n_(665563, "DatabaseHandler", lambda: DatabaseHandler), "messageExists"), _a_(665566, _n_(665565, "message", lambda: message), "id")):
                _l_(665580)

                _c_(665578, _a_(665569, _n_(665568, "DatabaseHandler", lambda: DatabaseHandler), "addMessage"), _a_(665571, _n_(665570, "message", lambda: message), "id"), _a_(665574, _a_(665573, _n_(665572, "message", lambda: message), "author"), "id"), _a_(665577, _a_(665576, _n_(665575, "message", lambda: message), "server"), "id"), False)
                _l_(665579)
        except _n_(665581, "Exception", lambda: Exception):
            _l_(665587)

            _c_(665584, _a_(665583, _n_(665582, "traceback", lambda: traceback), "print_exc"))
            _l_(665585)
            pass
            _l_(665586)
    else:
        await _c_(665591, _n_(665589, "process_message", lambda: process_message), _n_(665590, "message", lambda: message))
        _l_(665592)