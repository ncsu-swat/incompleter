# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68025435/attributeerror-io-textiowrapper-object-has-no-attribute-fp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(597635)

except ImportError:
    pass
try:
    import subprocess
    _l_(597637)

except ImportError:
    pass
try:
    import requests
    _l_(597639)

except ImportError:
    pass
try:
    import discord
    _l_(597641)

except ImportError:
    pass
try:
    import dhooks
    _l_(597643)

except ImportError:
    pass
try:
    from dhooks import Webhook, Embed
    _l_(597645)

except ImportError:
    pass

hook = _c_(597647, _n_(597646, "Webhook", lambda: Webhook), "hook")
_l_(597648)
Discord_txt = _c_(597650, _n_(597649, "open", lambda: open), "data.txt", "r+")
_l_(597651)
_c_(597655, _a_(597653, _n_(597652, "hook", lambda: hook), "send"), file=_n_(597654, "Discord_txt", lambda: Discord_txt))
_l_(597656)