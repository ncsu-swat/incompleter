# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67059050/typeerror-init-takes-1-positional-argument-but-2-were-given-announcemen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import discord
   _l_(350878)

except ImportError:
   pass
try:
   from discord.ext import commands
   _l_(350880)

except ImportError:
   pass
try:
   from discord.ext.commands import Bot
   _l_(350882)

except ImportError:
   pass
try:
   import asyncio
   _l_(350884)

except ImportError:
   pass
try:
   import time
   _l_(350886)

except ImportError:
   pass
try:
   from discord.ext.commands import has_permissions
   _l_(350888)

except ImportError:
   pass

client = _c_(350891, _a_(350890, _n_(350889, "commands", lambda: commands), "Bot"), command_prefix = "+")
_l_(350892)
_c_(350895, _a_(350894, _n_(350893, "client", lambda: client), "remove_command"), "help")
_l_(350896)

@_a_(350898, _n_(350897, "client", lambda: client), "event")
async def on_ready():
   _l_(350911)

   _c_(350903, _n_(350899, "print", lambda: print), _a_(350902, _a_(350901, _n_(350900, "client", lambda: client), "user"), "name"))
   _l_(350904)
   _c_(350906, _n_(350905, "print", lambda: print), "Online")
   _l_(350907)
   _c_(350909, _n_(350908, "print", lambda: print), "-------")
   _l_(350910)

@_c_(350914, _a_(350913, _n_(350912, "client", lambda: client), "command"), pass_context=True)
async def announce(ctx,*,message):
   _l_(350932)

   embed = _c_(350918, _a_(350916, _n_(350915, "discord", lambda: discord), "Embed"), "Information",description=_n_(350917, "message", lambda: message),color=0x9200ea)
   _l_(350919)
   _c_(350922, _a_(350921, _n_(350920, "embed", lambda: embed), "set_footer"), text="Made by Elanovic#7940")
   _l_(350923)
   await _c_(350930, _a_(350925, _n_(350924, "client", lambda: client), "send_message"), _a_(350928, _a_(350927, _n_(350926, "ctx", lambda: ctx), "message"), "channel"),embed=_n_(350929, "embed", lambda: embed))
   _l_(350931)

_c_(350935, _a_(350934, _n_(350933, "client", lambda: client), "run"), "TOKEN")
_l_(350936)