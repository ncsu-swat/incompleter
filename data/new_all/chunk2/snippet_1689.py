# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63288917/discord-py-attributeerror-embed-object-has-no-attribute-get
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(441009, _a_(441008, _n_(441007, "commands", lambda: commands), "command"))
async def test(self, ctx, messageID: _n_(441010, "int", lambda: int)):
    _l_(441035)

    channel = _c_(441014, _a_(441013, _a_(441012, _n_(441011, "self", lambda: self), "client"), "get_channel"), 740951313482907748)
    _l_(441015)
    
    message = await _c_(441019, _a_(441017, _n_(441016, "channel", lambda: channel), "fetch_message"), _n_(441018, "messageID", lambda: messageID))
    _l_(441020)
    embed = _a_(441022, _n_(441021, "message", lambda: message), "embeds")[0]
    _l_(441023)
    embed = _c_(441028, _a_(441026, _a_(441025, _n_(441024, "discord", lambda: discord), "Embed"), "from_dict"), _n_(441027, "embed", lambda: embed))
    _l_(441029)
    await _c_(441033, _a_(441031, _n_(441030, "ctx", lambda: ctx), "send"), embed=_n_(441032, "embed", lambda: embed))
    _l_(441034)