# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73310014/command-raised-an-exception-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(589647, _a_(589646, _n_(589645, "client", lambda: client), "command"))
@_c_(589651, _a_(589649, _n_(589648, "commands", lambda: commands), "has_role"), _n_(589650, "MANAGEMENT_ROLE_ID", lambda: MANAGEMENT_ROLE_ID))
async def archive(ctx: _a_(589653, _n_(589652, "commands", lambda: commands), "Context")):
    _l_(589686)

    transcript = await _c_(589659, _a_(589655, _n_(589654, "chat_exporter", lambda: chat_exporter), "export"), _a_(589657, _n_(589656, "ctx", lambda: ctx), "channel"),
        tz_info="UTC",
        military_time=True, 
        bot=_n_(589658, "client", lambda: client)
        )
    _l_(589660)

    if _n_(589661, "transcript", lambda: transcript) is None:
        _l_(589663)

        aux = ""
        _l_(589662)
        return aux

    _c_(589666, _n_(589664, "print", lambda: print), _n_(589665, "transcript", lambda: transcript))
    _l_(589667)
    transcript_file = _c_(589679, _a_(589669, _n_(589668, "discord", lambda: discord), "File"), _c_(589675, _a_(589671, _n_(589670, "io", lambda: io), "BytesIO"), _c_(589674, _a_(589673, _n_(589672, "transcript", lambda: transcript), "encode"))),
        filename=f"transcript-{_a_(589678, _a_(589677, _n_(589676, 'ctx', lambda: ctx), 'channel'), 'name')}",
    )
    _l_(589680)

    await _c_(589684, _a_(589682, _n_(589681, "ctx", lambda: ctx), "send"), file=_n_(589683, "transcript_file", lambda: transcript_file))
    _l_(589685)