# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67428943/understanding-cause-of-an-attributeerror
# bot.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import discord
  _l_(365652)

except ImportError:
  pass
try:
  from discord import message
  _l_(365654)

except ImportError:
  pass
try:
  import os
  _l_(365656)

except ImportError:
  pass
try:
  import time
  _l_(365658)

except ImportError:
  pass

client = _c_(365661, _a_(365660, _n_(365659, "discord", lambda: discord), "Client"))
_l_(365662)

msg = _a_(365664, _n_(365663, "message", lambda: message), "content")
_l_(365665)
sendmsg = _a_(365668, _a_(365667, _n_(365666, "message", lambda: message), "channel"), "send")
_l_(365669)
ss = 'not chanting'
_l_(365670)

@_a_(365672, _n_(365671, "client", lambda: client), "event")
async def on_ready():
  _l_(365681)

  _c_(365676, _n_(365673, "print", lambda: print), f'{_a_(365675, _n_(365674, "client", lambda: client), "user")} has connected to Discord!')
  _l_(365677)
  _c_(365679, _n_(365678, 'print', lambda: print), 'I am ready to chant.')
  _l_(365680)

async def chant():
  _l_(365692)

  await _c_(365684, _a_(365683, _n_(365682, 'asyncio', lambda: asyncio), 'time'), 1)
  _l_(365685)
  _c_(365687, _n_(365686, 'print', lambda: print), 'test passed!')
  _l_(365688)
  await _c_(365690, _n_(365689, 'sendmsg', lambda: sendmsg), 'passed the test')
  _l_(365691)

async def on_message():
  _l_(365739)

  if _n_(365693, 'msg', lambda: msg) == '$chant help':
    _l_(365700)

    _c_(365695, _n_(365694, 'print', lambda: print), 'The command \"$chant help\" was called')
    _l_(365696)
    await _c_(365698, _n_(365697, 'sendmsg', lambda: sendmsg), '$chant help - gives a list of commands I can do\n$start chanting - starts chanting in the specified channel\n$stop chanting - stops chanting')
    _l_(365699)

  if _n_(365701, 'ss', lambda: ss) == 'not chanting':
    _l_(365714)

    if _n_(365702, 'msg', lambda: msg) == '$start chanting':
      _l_(365713)

      _c_(365704, _n_(365703, 'print', lambda: print), 'The command \"$start chanting\" was called')
      _l_(365705)
      ss = 'chanting'
      _l_(365706)
      await _c_(365708, _n_(365707, 'sendmsg', lambda: sendmsg), 'Ok. Chanting now.')
      _l_(365709)
      await _c_(365711, _n_(365710, 'sendmsg', lambda: sendmsg), 'reference (this message triggers the code to chant)')
      _l_(365712)

  if _n_(365715, 'ss', lambda: ss) == 'chanting':
    _l_(365738)

    if _n_(365716, 'msg', lambda: msg) == '$stop chanting':
      _l_(365737)

      _c_(365718, _n_(365717, 'print', lambda: print), 'The command \"$stop chanting\" was called')
      _l_(365719)
      ss = 'not chanting'
      _l_(365720)
      await _c_(365722, _n_(365721, 'sendmsg', lambda: sendmsg), 'Ok. Stopping chanting...')
      _l_(365723)
      await _c_(365725, _n_(365724, 'sendmsg', lambda: sendmsg), 'Please wait...')
      _l_(365726)
    
    elif _a_(365728, _n_(365727, 'message', lambda: message), 'user') == '{client.user}':
      _l_(365736)

      if _c_(365731, _a_(365730, _n_(365729, 'msg', lambda: msg), 'contains'), 'reference'):
        _l_(365735)

        _c_(365733, _n_(365732, 'chant', lambda: chant))
        _l_(365734)
_c_(365742, _a_(365741, _n_(365740, 'client', lambda: client), 'run'), 'no token 4 u')
_l_(365743)