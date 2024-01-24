# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67059050/typeerror-init-takes-1-positional-argument-but-2-were-given-announcemen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import discord
   _l_(361701)

except ImportError:
   pass
try:
   from discord.ext import commands
   _l_(361703)

except ImportError:
   pass
try:
   from discord.ext.commands import Bot
   _l_(361705)

except ImportError:
   pass
try:
   import asyncio
   _l_(361707)

except ImportError:
   pass
try:
   import time
   _l_(361709)

except ImportError:
   pass
try:
   from discord.ext.commands import has_permissions
   _l_(361711)

except ImportError:
   pass

client = _c_(361714, _a_(361713, _n_(361712, "commands", lambda: commands), "Bot"), command_prefix = "+")
_l_(361715)
_c_(361718, _a_(361717, _n_(361716, "client", lambda: client), "remove_command"), "help")
_l_(361719)

@_a_(361721, _n_(361720, "client", lambda: client), "event")
async def on_ready():
   _l_(361734)

   _c_(361726, _n_(361722, "print", lambda: print), _a_(361725, _a_(361724, _n_(361723, "client", lambda: client), "user"), "name"))
   _l_(361727)
   _c_(361729, _n_(361728, "print", lambda: print), "Online")
   _l_(361730)
   _c_(361732, _n_(361731, "print", lambda: print), "-------")
   _l_(361733)

@_c_(361737, _a_(361736, _n_(361735, "client", lambda: client), "command"), pass_context=True)
async def announce(ctx,*,message):
   _l_(361755)

   embed = _c_(361741, _a_(361739, _n_(361738, "discord", lambda: discord), "Embed"), "Information",description=_n_(361740, "message", lambda: message),color=0x9200ea)
   _l_(361742)
   _c_(361745, _a_(361744, _n_(361743, "embed", lambda: embed), "set_footer"), text="Made by Elanovic#7940")
   _l_(361746)
   await _c_(361753, _a_(361748, _n_(361747, "client", lambda: client), "send_message"), _a_(361751, _a_(361750, _n_(361749, "ctx", lambda: ctx), "message"), "channel"),embed=_n_(361752, "embed", lambda: embed))
   _l_(361754)

_c_(361758, _a_(361757, _n_(361756, "client", lambda: client), "run"), "TOKEN")
_l_(361759)