# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66959972/attributeerror-method-object-has-no-attribute-backend
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth import models
    _l_(472886)

except ImportError:
    pass

class DiscordUserOAuth2Manager(_a_(472888, _n_(472887, "models", lambda: models), "UserManager")):
    _l_(472909)

    def create_new_discord_user(self, user):
        _l_(472908)

        _c_(472890, _n_(472889, "print", lambda: print), 'Inside Discord User Manager')
        _l_(472891)
        discord_tag = '%s#%s' % (_n_(472892, "user", lambda: user)['username'], _n_(472893, "user", lambda: user)['discriminator'])
        _l_(472894)
        new_user = _c_(472904, _a_(472896, _n_(472895, "self", lambda: self), "create"), id=_n_(472897, "user", lambda: user)['id'],
            avatar=_n_(472898, "user", lambda: user)['avatar'],
            public_flags=_n_(472899, "user", lambda: user)['public_flags'],
            flags=_n_(472900, "user", lambda: user)['flags'],
            locale=_n_(472901, "user", lambda: user)['locale'],
            mfa_enabled=_n_(472902, "user", lambda: user)['mfa_enabled'],
            discord_tag=_n_(472903, "discord_tag", lambda: discord_tag)
        )
        _l_(472905)
        aux = _n_(472906, "new_user", lambda: new_user)
        _l_(472907)
        return aux