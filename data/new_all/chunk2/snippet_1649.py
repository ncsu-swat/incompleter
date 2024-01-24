# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66959972/attributeerror-method-object-has-no-attribute-backend
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(453381)

except ImportError:
    pass
try:
    from .managers import DiscordUserOAuth2Manager
    _l_(453383)

except ImportError:
    pass

class DiscordUser(_a_(453385, _n_(453384, "models", lambda: models), "Model")):
    _l_(453421)

    objects = _c_(453387, _n_(453386, "DiscordUserOAuth2Manager", lambda: DiscordUserOAuth2Manager))
    _l_(453388)

    id = _c_(453391, _a_(453390, _n_(453389, "models", lambda: models), "BigIntegerField"), primary_key=True)
    _l_(453392)
    discord_tag = _c_(453395, _a_(453394, _n_(453393, "models", lambda: models), "CharField"), max_length=100)
    _l_(453396)
    avatar = _c_(453399, _a_(453398, _n_(453397, "models", lambda: models), "CharField"), max_length=100)
    _l_(453400)
    public_flags = _c_(453403, _a_(453402, _n_(453401, "models", lambda: models), "BigIntegerField"))
    _l_(453404)
    flag = _c_(453407, _a_(453406, _n_(453405, "models", lambda: models), "IntegerField"))
    _l_(453408)
    locale = _c_(453411, _a_(453410, _n_(453409, "models", lambda: models), "CharField"), max_length=100)
    _l_(453412)
    mfa_enabled = _c_(453415, _a_(453414, _n_(453413, "models", lambda: models), "BooleanField"))
    _l_(453416)
    last_login = _c_(453419, _a_(453418, _n_(453417, "models", lambda: models), "DateTimeField"), null=True)
    _l_(453420)