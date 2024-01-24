# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67059050/typeerror-init-takes-1-positional-argument-but-2-were-given-announcemen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
   import discord
   _l_(336801)

except ImportError:
   pass
try:
   from discord.ext import commands
   _l_(336803)

except ImportError:
   pass
try:
   from discord.ext.commands import Bot
   _l_(336805)

except ImportError:
   pass
try:
   import asyncio
   _l_(336807)

except ImportError:
   pass
try:
   import time
   _l_(336809)

except ImportError:
   pass
try:
   from discord.ext.commands import has_permissions
   _l_(336811)

except ImportError:
   pass

client = _c_(336814, _a_(336813, _n_(336812, "commands", lambda: commands), "Bot"), command_prefix = "+")
_l_(336815)
_c_(336818, _a_(336817, _n_(336816, "client", lambda: client), "remove_command"), "help")
_l_(336819)

@_a_(336821, _n_(336820, "client", lambda: client), "event")
async def on_ready():
   _l_(336834)

   _c_(336826, _n_(336822, "print", lambda: print), _a_(336825, _a_(336824, _n_(336823, "client", lambda: client), "user"), "name"))
   _l_(336827)
   _c_(336829, _n_(336828, "print", lambda: print), "Online")
   _l_(336830)
   _c_(336832, _n_(336831, "print", lambda: print), "-------")
   _l_(336833)

@_c_(336837, _a_(336836, _n_(336835, "client", lambda: client), "command"), pass_context=True)
async def announce(ctx,*,message):
   _l_(336855)

   embed = _c_(336841, _a_(336839, _n_(336838, "discord", lambda: discord), "Embed"), "Information",description=_n_(336840, "message", lambda: message),color=0x9200ea)
   _l_(336842)
   _c_(336845, _a_(336844, _n_(336843, "embed", lambda: embed), "set_footer"), text="Made by Elanovic#7940")
   _l_(336846)
   await _c_(336853, _a_(336848, _n_(336847, "client", lambda: client), "send_message"), _a_(336851, _a_(336850, _n_(336849, "ctx", lambda: ctx), "message"), "channel"),embed=_n_(336852, "embed", lambda: embed))
   _l_(336854)

_c_(336858, _a_(336857, _n_(336856, "client", lambda: client), "run"), "TOKEN")
_l_(336859)