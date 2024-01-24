# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53999771/discord-py-bot-rewrite-attributeerror-bot-object-has-no-attribute-send-messa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     from discord.ext.commands import Bot
     _l_(435261)

except ImportError:
     pass
try:
     import os
     _l_(435263)

except ImportError:
     pass

BOT_PREFIX = ("?")
_l_(435264)
access_token= _a_(435266, _n_(435265, "os", lambda: os), "environ")["ACCESS_TOKEN"]
_l_(435267)

client = _c_(435270, _n_(435268, "Bot", lambda: Bot), command_prefix=_n_(435269, "BOT_PREFIX", lambda: BOT_PREFIX))
_l_(435271)

@_a_(435273, _n_(435272, "client", lambda: client), "event")
async def on_message(message):
     _l_(435293)

     if _c_(435277, _a_(435276, _a_(435275, _n_(435274, "message", lambda: message), "content"), "startswith"), "?"):
          _l_(435292)

          newMessage = 'text' + _c_(435283, _a_(435282, _c_(435281, _n_(435278, "str", lambda: str), _a_(435280, _n_(435279, "message", lambda: message), "content"))[1:], "upper")) + '.png'
          _l_(435284)
          await _c_(435290, _a_(435286, _n_(435285, "client", lambda: client), "send_message"), _a_(435288, _n_(435287, "message", lambda: message), "channel"), _n_(435289, "newMessage", lambda: newMessage))
          _l_(435291)

_c_(435297, _a_(435295, _n_(435294, "client", lambda: client), "run"), _n_(435296, "access_token", lambda: access_token))
_l_(435298)