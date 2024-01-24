# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75982418/attributeerror-module-discord-ui-has-no-attribute-actionrow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(637447)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(637449)

except ImportError:
    pass

# boring

intents = _c_(637453, _a_(637452, _a_(637451, _n_(637450, "discord", lambda: discord), "Intents"), "all"))
_l_(637454)
bot = _c_(637458, _a_(637456, _n_(637455, "commands", lambda: commands), "Bot"), command_prefix='!', intents=_n_(637457, "intents", lambda: intents))
_l_(637459)

THRESHOLD = 5
_l_(637460)

@_a_(637462, _n_(637461, "bot", lambda: bot), "event")
async def on_ready():
    _l_(637473)

    channel = _c_(637465, _a_(637464, _n_(637463, "bot", lambda: bot), "get_channel"), 1069346031281651843)
    _l_(637466)
# Used to make announcements in server, disabled atm (should prob make it more efficient)
#    await channel.send('', file=discord.File(''))
    _c_(637471, _n_(637467, "print", lambda: print), _c_(637470, _a_(637468, 'All systems go!', "format"), _n_(637469, "bot", lambda: bot)))
    _l_(637472)

# Pin feature
@_a_(637475, _n_(637474, "bot", lambda: bot), "event")
async def on_raw_reaction_add(payload):
    _l_(637499)

    if _a_(637478, _a_(637477, _n_(637476, "payload", lambda: payload), "emoji"), "name") == "📌":
        _l_(637495)

        channel = await _c_(637483, _a_(637480, _n_(637479, "bot", lambda: bot), "fetch_channel"), _a_(637482, _n_(637481, "payload", lambda: payload), "channel_id"))
        _l_(637484)
        message = await _c_(637489, _a_(637486, _n_(637485, "channel", lambda: channel), "fetch_message"), _a_(637488, _n_(637487, "payload", lambda: payload), "message_id"))
        _l_(637490)
        await _c_(637493, _a_(637492, _n_(637491, "message", lambda: message), "pin"))
        _l_(637494)
    _c_(637497, _n_(637496, "print", lambda: print), "Reaction added.")
    _l_(637498)

@_a_(637501, _n_(637500, "bot", lambda: bot), "event")
async def on_raw_reaction_remove(payload):
    _l_(637569)

    if _a_(637504, _a_(637503, _n_(637502, "payload", lambda: payload), "emoji"), "name") == "📌":
        _l_(637565)

        channel = await _c_(637509, _a_(637506, _n_(637505, "bot", lambda: bot), "fetch_channel"), _a_(637508, _n_(637507, "payload", lambda: payload), "channel_id"))
        _l_(637510)
        message = await _c_(637515, _a_(637512, _n_(637511, "channel", lambda: channel), "fetch_message"), _a_(637514, _n_(637513, "payload", lambda: payload), "message_id"))
        _l_(637516)
        pins = [_n_(637517, "reaction", lambda: reaction) for reaction in _a_(637519, _n_(637518, "message", lambda: message), "reactions") if _c_(637523, _n_(637520, "str", lambda: str), _a_(637522, _n_(637521, "reaction", lambda: reaction), "emoji")) == "📌"]
        _l_(637524)
        if _c_(637527, _n_(637525, "len", lambda: len), _n_(637526, "pins", lambda: pins)) == 0:
            _l_(637564)

            await _c_(637530, _a_(637529, _n_(637528, "message", lambda: message), "unpin"))
            _l_(637531)
            button = _c_(637538, _a_(637534, _a_(637533, _n_(637532, "discord", lambda: discord), "ui"), "Button"), label="View Unpinned Message", style=_a_(637537, _a_(637536, _n_(637535, "discord", lambda: discord), "ButtonStyle"), "grey"), custom_id="view_unpinned_message")
            _l_(637539)
            async def send_message(ctx: _a_(637541, _n_(637540, "discord", lambda: discord), "Interaction")):
                _l_(637549)

                await _c_(637547, _a_(637544, _a_(637543, _n_(637542, "ctx", lambda: ctx), "channel"), "send"), content=_a_(637546, _n_(637545, "message", lambda: message), "content"))
                _l_(637548)
            _n_(637550, "button", lambda: button).callback = _n_(637551, "send_message", lambda: send_message)
            _l_(637552)
            view_message_action_row = _c_(637557, _a_(637555, _a_(637554, _n_(637553, "discord", lambda: discord), "ui"), "ActionRow"), _n_(637556, "button", lambda: button))
            _l_(637558)
            await _c_(637562, _a_(637560, _n_(637559, "channel", lambda: channel), "send"), "A previously pinned message has been unpinned.", components=[_n_(637561, "view_message_action_row", lambda: view_message_action_row)])
            _l_(637563)
    _c_(637567, _n_(637566, "print", lambda: print), "A reaction has been removed.")
    _l_(637568)

# api token

_c_(637572, _a_(637571, _n_(637570, "bot", lambda: bot), "run"), 'TOKEN')
_l_(637573)