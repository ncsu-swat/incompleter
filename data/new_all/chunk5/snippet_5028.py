# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52356984/discord-py-attributeerror-context-object-has-no-attribute-server
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(700827, _a_(700826, _n_(700825, "commands", lambda: commands), "command"), pass_context=True, no_pm=True)                
async def unpin(self, ctx):
    _l_(700867)

    """Listen for a message then unpin any other messages older than 7 days"""
    server = _a_(700829, _n_(700828, "ctx", lambda: ctx), "server")
    _l_(700830)
    messages = await _c_(700838, _a_(700833, _a_(700832, _n_(700831, "self", lambda: self), "bot"), "pins_from"), _c_(700837, _a_(700836, _a_(700835, _n_(700834, "self", lambda: self), "bot"), "get_channel"), '490899209067823135'))
    _l_(700839)
    if _n_(700840, "server", lambda: server):
        _l_(700866)

        for msg in _n_(700841, "messages", lambda: messages):
            _l_(700865)

            if _a_(700847, (_c_(700844, _a_(700843, _n_(700842, "datetime", lambda: datetime), "now")) - _a_(700846, _n_(700845, "msg", lambda: msg), "timestamp")), "days") > 7:
                _l_(700864)

                try:
                    _l_(700863)

                    await _c_(700852, _a_(700850, _a_(700849, _n_(700848, "self", lambda: self), "bot"), "unpin_message"), _n_(700851, "msg", lambda: msg))
                    _l_(700853)
                    _c_(700855, _n_(700854, "print", lambda: print), "Unpinned")
                    _l_(700856)

                except _a_(700858, _n_(700857, "discord", lambda: discord), "Forbidden"):
                    _l_(700862)

                    _c_(700860, _n_(700859, "print", lambda: print), "No permissions to do that!")
                    _l_(700861)