# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63059165/attributeerror-bot-object-has-no-attribute-pin-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
global stopcheck
_l_(663199)
stopcheck = 'test'
_l_(663200)
try:
  import asyncio
  _l_(663202)

except ImportError:
  pass
global time
_l_(663203)
time = 100
_l_(663204)
try:
  import os
  _l_(663206)

except ImportError:
  pass
ContinueAutoJoke = 'autojoke'
_l_(663207)
StopAutoJoke = 'o'
_l_(663208)
try:
  import discord
  _l_(663210)

except ImportError:
  pass
try:
  import time
  _l_(663212)

except ImportError:
  pass
try:
  import random
  _l_(663214)

except ImportError:
  pass
try:
  import discord
  _l_(663216)

except ImportError:
  pass
try:
  from discord.ext import commands
  _l_(663218)

except ImportError:
  pass



client = _c_(663221, _a_(663220, _n_(663219, "discord", lambda: discord), "Client"))
_l_(663222)
client = _c_(663225, _a_(663224, _n_(663223, "commands", lambda: commands), "Bot"), command_prefix = '$')
_l_(663226)

@_c_(663229, _a_(663228, _n_(663227, "client", lambda: client), "command"))
async def test(ctx):
  _l_(663247)

  message = await _c_(663232, _a_(663231, _n_(663230, "ctx", lambda: ctx), "send"), f'All messages gonna be deleted in 100 seconds')
  _l_(663233)
  await _c_(663237, _a_(663235, _n_(663234, 'client', lambda: client), 'pin_message'), _n_(663236, 'message', lambda: message))
  _l_(663238)
  for c in _c_(663240, _n_(663239, 'range', lambda: range), -100,0):
    _l_(663246)

    await _c_(663244, _a_(663242, _n_(663241, 'message', lambda: message), 'edit'), content=f'All messages gonna be deleted in {_n_(663243, "c", lambda: c)} seconds')
    _l_(663245)