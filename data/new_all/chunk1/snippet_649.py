# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71369200/pycord-error-discord-errors-extensionfailed-extension-cogs-cmds-raised-an-er
# main.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord, os, dotenv
    _l_(378161)

except ImportError:
    pass

# setup
bot = _c_(378168, _a_(378163, _n_(378162, "discord", lambda: discord), "Bot"), intents = _c_(378167, _a_(378166, _a_(378165, _n_(378164, "discord", lambda: discord), "Intents"), "default")),
    prefix = "zrun "
)
_l_(378169)

@_a_(378171, _n_(378170, "bot", lambda: bot), "event")
async def on_ready():
    _l_(378177)

    _c_(378175, _n_(378172, "print", lambda: print), f'Connected as {_a_(378174, _n_(378173, "bot", lambda: bot), "user")}')
    _l_(378176)

# load cmds
_c_(378180, _a_(378179, _n_(378178, 'bot', lambda: bot), 'load_extension'), 'cogs.cmds')
_l_(378181)

# get token and run bot
_c_(378184, _a_(378183, _n_(378182, 'dotenv', lambda: dotenv), 'load_dotenv'))
_l_(378185)
_c_(378191, _a_(378187, _n_(378186, 'bot', lambda: bot), 'run'), _c_(378190, _a_(378189, _n_(378188, 'os', lambda: os), 'getenv'), 'TOKEN'))
_l_(378192)