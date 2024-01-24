# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71104277/discord-py-typeerror-command-name-error-missing-1-required-positional-argumen
# COG CLASS
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Entries(_a_(596372, _n_(596371, "commands", lambda: commands), "Cog")):
    _l_(596471)


    def __init__(self, client):
        _l_(596376)

        _n_(596373, "self", lambda: self).client = _n_(596374, "client", lambda: client)
        _l_(596375)

# START UP
    @_c_(596379, _a_(596378, _a_(596377, commands, "Cog"), "listener"))
    async def on_ready(self):
        _l_(596383)

        _c_(596381, _n_(596380, "print", lambda: print), 'Entry.py is connected.')
        _l_(596382)

# ENTER COMMAND
    @_c_(596385, _a_(596384, commands, "command"), name="entry", aliases=["enter","Enter","ENTER"])
    @_c_(596389, _a_(596386, commands, "cooldown"), 1, 180, _a_(596388, _a_(596387, commands, "BucketType"), "user"))
    async def entry(self, ctx):
        _l_(596409)

        filename = "entries.txt"
        _l_(596390)
        with _c_(596393, _n_(596391, "open", lambda: open), _n_(596392, "filename", lambda: filename), "a") as file:
            _l_(596408)

            _c_(596399, _a_(596395, _n_(596394, "file", lambda: file), "write"), f"{_a_(596398, _a_(596397, _n_(596396, 'ctx', lambda: ctx), 'author'), 'name')}\n")
            _l_(596400)
            await _c_(596406, _a_(596402, _n_(596401, "ctx", lambda: ctx), "send"), f"**@{_a_(596405, _a_(596404, _n_(596403, 'ctx', lambda: ctx), 'author'), 'name')} Your entry has been recorded. :white_check_mark:**")
            _l_(596407)

    @_a_(596410, entry, "error")
    async def command_name_error(self, ctx, error):
        _l_(596424)

        if _c_(596415, _n_(596411, "isinstance", lambda: isinstance), _n_(596412, "error", lambda: error), _a_(596414, _n_(596413, "commands", lambda: commands), "CommandOnCooldown")):
            _l_(596423)

            await _c_(596421, _a_(596417, _n_(596416, "ctx", lambda: ctx), "send"), f"**@{_a_(596420, _a_(596419, _n_(596418, 'ctx', lambda: ctx), 'author'), 'name')} You have already entered! :warning:**")
            _l_(596422)

# STOP COMMAND
    @_c_(596426, _a_(596425, commands, "command"))
    async def stop(self, ctx, *, command):
        _l_(596447)

        command = _c_(596431, _a_(596429, _a_(596428, _n_(596427, "self", lambda: self), "client"), "get_command"), _n_(596430, "command", lambda: command))
        _l_(596432)
        _c_(596435, _a_(596434, _n_(596433, "command", lambda: command), "update"), enabled=False)
        _l_(596436)
        await _c_(596440, _a_(596439, _a_(596438, _n_(596437, "ctx", lambda: ctx), "author"), "send"), f" The command **!enter** has been **disabled**.")
        _l_(596441)
        await _c_(596445, _a_(596444, _a_(596443, _n_(596442, "ctx", lambda: ctx), "channel"), "purge"), limit=1)
        _l_(596446)

# START COMMAND
    @_c_(596449, _a_(596448, commands, "command"))
    async def start(self, ctx, *, command):
        _l_(596470)

        command = _c_(596454, _a_(596452, _a_(596451, _n_(596450, "self", lambda: self), "client"), "get_command"), _n_(596453, "command", lambda: command))
        _l_(596455)
        _c_(596458, _a_(596457, _n_(596456, "command", lambda: command), "update"), enabled=True)
        _l_(596459)
        await _c_(596463, _a_(596462, _a_(596461, _n_(596460, "ctx", lambda: ctx), "author"), "send"), f" The command **!enter** has been **enabled**.")
        _l_(596464)
        await _c_(596468, _a_(596467, _a_(596466, _n_(596465, "ctx", lambda: ctx), "channel"), "purge"), limit=1)
        _l_(596469)

def setup(client):
    _l_(596479)

    _c_(596477, _a_(596473, _n_(596472, "client", lambda: client), "add_cog"), _c_(596476, _n_(596474, "Entries", lambda: Entries), _n_(596475, "client", lambda: client)))
    _l_(596478)