# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39553483/attributeerror-module-discordoragisearch-has-no-attribute-isvalidmessage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import DiscordoragiSearch
    _l_(679373)

except ImportError:
    pass

...
_l_(679374)

@_a_(679377, _a_(679376, _n_(679375, "Discord", lambda: Discord), "client"), "event")
async def on_message(message):
    _l_(679416)

    _c_(679379, _n_(679378, "print", lambda: print), 'Message recieved')
    _l_(679380)
    #Is the message valid (i.e. it's not made by Discordoragi and I haven't seen it already). If no, try to add it to the "already seen pile" and skip to the next message. If yes, keep going.
    if not _c_(679384, _a_(679382, _n_(679381, "DiscordoragiSearch", lambda: DiscordoragiSearch), "isValidMessage"), _n_(679383, "message", lambda: message)):
        _l_(679415)

        try:
            _l_(679410)

            if not _c_(679389, _a_(679386, _n_(679385, "DatabaseHandler", lambda: DatabaseHandler), "messageExists"), _a_(679388, _n_(679387, "message", lambda: message), "id")):
                _l_(679402)

                _c_(679400, _a_(679391, _n_(679390, "DatabaseHandler", lambda: DatabaseHandler), "addMessage"), _a_(679393, _n_(679392, "message", lambda: message), "id"), _a_(679396, _a_(679395, _n_(679394, "message", lambda: message), "author"), "id"), _a_(679399, _a_(679398, _n_(679397, "message", lambda: message), "server"), "id"), False)
                _l_(679401)
        except _n_(679403, "Exception", lambda: Exception):
            _l_(679409)

            _c_(679406, _a_(679405, _n_(679404, "traceback", lambda: traceback), "print_exc"))
            _l_(679407)
            pass
            _l_(679408)
    else:
        await _c_(679413, _n_(679411, "process_message", lambda: process_message), _n_(679412, "message", lambda: message))
        _l_(679414)