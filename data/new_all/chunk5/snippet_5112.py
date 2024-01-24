# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63059165/attributeerror-bot-object-has-no-attribute-pin-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
global stopcheck
_l_(692719)
stopcheck = 'test'
_l_(692720)
try:
  import asyncio
  _l_(692722)

except ImportError:
  pass
global time
_l_(692723)
time = 100
_l_(692724)
try:
  import os
  _l_(692726)

except ImportError:
  pass
ContinueAutoJoke = 'autojoke'
_l_(692727)
StopAutoJoke = 'o'
_l_(692728)
try:
  import discord
  _l_(692730)

except ImportError:
  pass
try:
  import time
  _l_(692732)

except ImportError:
  pass
try:
  import random
  _l_(692734)

except ImportError:
  pass
try:
  import discord
  _l_(692736)

except ImportError:
  pass
try:
  from discord.ext import commands
  _l_(692738)

except ImportError:
  pass



client = _c_(692741, _a_(692740, _n_(692739, "discord", lambda: discord), "Client"))
_l_(692742)
client = _c_(692745, _a_(692744, _n_(692743, "commands", lambda: commands), "Bot"), command_prefix = '$')
_l_(692746)

@_c_(692749, _a_(692748, _n_(692747, "client", lambda: client), "command"))
async def test(ctx):
  _l_(692767)

  message = await _c_(692752, _a_(692751, _n_(692750, "ctx", lambda: ctx), "send"), f'All messages gonna be deleted in 100 seconds')
  _l_(692753)
  await _c_(692757, _a_(692755, _n_(692754, 'client', lambda: client), 'pin_message'), _n_(692756, 'message', lambda: message))
  _l_(692758)
  for c in _c_(692760, _n_(692759, 'range', lambda: range), -100,0):
    _l_(692766)

    await _c_(692764, _a_(692762, _n_(692761, 'message', lambda: message), 'edit'), content=f'All messages gonna be deleted in {_n_(692763, "c", lambda: c)} seconds')
    _l_(692765)