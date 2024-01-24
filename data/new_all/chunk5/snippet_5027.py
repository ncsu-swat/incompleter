# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52356984/discord-py-attributeerror-context-object-has-no-attribute-server
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(697231, _a_(697230, _n_(697229, "commands", lambda: commands), "command"), pass_context=True, no_pm=True)                
async def unpin(self, ctx):
    _l_(697271)

    """Listen for a message then unpin any other messages older than 7 days"""
    server = _a_(697233, _n_(697232, "ctx", lambda: ctx), "server")
    _l_(697234)
    messages = await _c_(697242, _a_(697237, _a_(697236, _n_(697235, "self", lambda: self), "bot"), "pins_from"), _c_(697241, _a_(697240, _a_(697239, _n_(697238, "self", lambda: self), "bot"), "get_channel"), '490899209067823135'))
    _l_(697243)
    if _n_(697244, "server", lambda: server):
        _l_(697270)

        for msg in _n_(697245, "messages", lambda: messages):
            _l_(697269)

            if _a_(697251, (_c_(697248, _a_(697247, _n_(697246, "datetime", lambda: datetime), "now")) - _a_(697250, _n_(697249, "msg", lambda: msg), "timestamp")), "days") > 7:
                _l_(697268)

                try:
                    _l_(697267)

                    await _c_(697256, _a_(697254, _a_(697253, _n_(697252, "self", lambda: self), "bot"), "unpin_message"), _n_(697255, "msg", lambda: msg))
                    _l_(697257)
                    _c_(697259, _n_(697258, "print", lambda: print), "Unpinned")
                    _l_(697260)

                except _a_(697262, _n_(697261, "discord", lambda: discord), "Forbidden"):
                    _l_(697266)

                    _c_(697264, _n_(697263, "print", lambda: print), "No permissions to do that!")
                    _l_(697265)