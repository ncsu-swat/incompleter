# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62335566/nameerror-in-a-discord-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from var_secrets import *
    _l_(357222)

except ImportError:
    pass
try:
    import os
    _l_(357224)

except ImportError:
    pass
try:
    import json
    _l_(357226)

except ImportError:
    pass
try:
    import pickle
    _l_(357228)

except ImportError:
    pass
try:
    import random
    _l_(357230)

except ImportError:
    pass
try:
    import asyncio
    _l_(357232)

except ImportError:
    pass
try:
    import discord
    _l_(357234)

except ImportError:
    pass
try:
    from imgurpython import ImgurClient
    _l_(357236)

except ImportError:
    pass

# DISCORD  VARS #
#client = discord.Client()

BOT_PREFIX = ";"
_l_(357237)
CHANNEL_IDs  = ("449281327988998156")
_l_(357238)

# PYTHON VALS #
class bcolors:
    _l_(357247)

    HEADER = '\033[95m'
    _l_(357239)
    OKBLUE = '\033[94m'
    _l_(357240)
    OKGREEN = '\033[92m'
    _l_(357241)
    WARNING = '\033[93m'
    _l_(357242)
    FAIL = '\033[91m'
    _l_(357243)
    ENDC = '\033[0m'
    _l_(357244)
    BOLD = '\033[1m'
    _l_(357245)
    UNDERLINE = '\033[4m'
    _l_(357246)

# Globals #

imgr_client = _c_(357251, _n_(357248, "ImgurClient", lambda: ImgurClient), _n_(357249, "imgr_client_id", lambda: imgr_client_id), _n_(357250, "imgr_client_secret", lambda: imgr_client_secret))
_l_(357252)

# Image Vars #
white = (255,255,255,255)
_l_(357253)
black = (0, 0, 0, 255)
_l_(357254)