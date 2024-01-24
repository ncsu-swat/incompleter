# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75982418/attributeerror-module-discord-ui-has-no-attribute-actionrow
# Pin feature
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(642271, _n_(642270, "bot", lambda: bot), "event")
async def on_raw_reaction_add(payload):
    _l_(642295)

    if _a_(642274, _a_(642273, _n_(642272, "payload", lambda: payload), "emoji"), "name") == "📌":
        _l_(642291)

        channel = await _c_(642279, _a_(642276, _n_(642275, "bot", lambda: bot), "fetch_channel"), _a_(642278, _n_(642277, "payload", lambda: payload), "channel_id"))
        _l_(642280)
        message = await _c_(642285, _a_(642282, _n_(642281, "channel", lambda: channel), "fetch_message"), _a_(642284, _n_(642283, "payload", lambda: payload), "message_id"))
        _l_(642286)
        await _c_(642289, _a_(642288, _n_(642287, "message", lambda: message), "pin"))
        _l_(642290)
    _c_(642293, _n_(642292, "print", lambda: print), "Reaction added.")
    _l_(642294)

@_a_(642297, _n_(642296, "bot", lambda: bot), "event")
async def on_raw_reaction_remove(payload):
    _l_(642365)

    if _a_(642300, _a_(642299, _n_(642298, "payload", lambda: payload), "emoji"), "name") == "📌":
        _l_(642361)

        channel = await _c_(642305, _a_(642302, _n_(642301, "bot", lambda: bot), "fetch_channel"), _a_(642304, _n_(642303, "payload", lambda: payload), "channel_id"))
        _l_(642306)
        message = await _c_(642311, _a_(642308, _n_(642307, "channel", lambda: channel), "fetch_message"), _a_(642310, _n_(642309, "payload", lambda: payload), "message_id"))
        _l_(642312)
        pins = [_n_(642313, "reaction", lambda: reaction) for reaction in _a_(642315, _n_(642314, "message", lambda: message), "reactions") if _c_(642319, _n_(642316, "str", lambda: str), _a_(642318, _n_(642317, "reaction", lambda: reaction), "emoji")) == "📌"]
        _l_(642320)
        if _c_(642323, _n_(642321, "len", lambda: len), _n_(642322, "pins", lambda: pins)) == 0:
            _l_(642360)

            await _c_(642326, _a_(642325, _n_(642324, "message", lambda: message), "unpin"))
            _l_(642327)
            button = _c_(642334, _a_(642330, _a_(642329, _n_(642328, "discord", lambda: discord), "ui"), "Button"), label="View Unpinned Message", style=_a_(642333, _a_(642332, _n_(642331, "discord", lambda: discord), "ButtonStyle"), "grey"), custom_id="view_unpinned_message")
            _l_(642335)
            async def send_message(ctx: _a_(642337, _n_(642336, "discord", lambda: discord), "Interaction")):
                _l_(642345)

                await _c_(642343, _a_(642340, _a_(642339, _n_(642338, "ctx", lambda: ctx), "channel"), "send"), content=_a_(642342, _n_(642341, "message", lambda: message), "content"))
                _l_(642344)
            _n_(642346, "button", lambda: button).callback = _n_(642347, "send_message", lambda: send_message)
            _l_(642348)
            view_message_action_row = _c_(642353, _a_(642351, _a_(642350, _n_(642349, "discord", lambda: discord), "ui"), "ActionRow"), _n_(642352, "button", lambda: button))
            _l_(642354)
            await _c_(642358, _a_(642356, _n_(642355, "channel", lambda: channel), "send"), "A previously pinned message has been unpinned.", components=[_n_(642357, "view_message_action_row", lambda: view_message_action_row)])
            _l_(642359)
    _c_(642363, _n_(642362, "print", lambda: print), "A reaction has been removed.")
    _l_(642364)