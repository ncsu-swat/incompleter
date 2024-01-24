# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76367183/command-reload-raised-an-exception-typeerror-botbase-reload-extension-miss
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import discord
     _l_(538834)

except ImportError:
     pass
try:
     import settings
     _l_(538836)

except ImportError:
     pass
try:
     from discord.ext import commands
     _l_(538838)

except ImportError:
     pass
try:
     from discord.interactions import Interaction
     _l_(538840)

except ImportError:
     pass

@_c_(538843, _a_(538842, _n_(538841, "commands", lambda: commands), "hybrid_command"), name="reload", description="Reloads all extensions")
async def reload(ctx):
     _l_(538865)

     for cmd_file in _c_(538847, _a_(538846, _a_(538845, _n_(538844, "settings", lambda: settings), "CMDS_DIR"), "glob"), "*.py"):
          _l_(538864)

          if _a_(538849, _n_(538848, "cmd_file", lambda: cmd_file), "name") != "__init__.py":
               _l_(538863)

               extensions = f"extension.{_a_(538851, _n_(538850, 'cmd_file', lambda: cmd_file), 'name')[:-3]}"
               _l_(538852)
               await _c_(538857, _a_(538855, _a_(538854, _n_(538853, "commands", lambda: commands), "Bot"), "reload_extension"), name=_n_(538856, "extensions", lambda: extensions))
               _l_(538858)
               _c_(538861, _n_(538859, "print", lambda: print), f"Reloaded extension: {_n_(538860, 'extensions', lambda: extensions)}")
               _l_(538862)

async def setup(bot):
     _l_(538871)

     _c_(538869, _a_(538867, _n_(538866, "bot", lambda: bot), "add_command"), _n_(538868, "reload", lambda: reload))
     _l_(538870)