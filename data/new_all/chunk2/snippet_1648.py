# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66959972/attributeerror-method-object-has-no-attribute-backend
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.backends import BaseBackend
    _l_(450840)

except ImportError:
    pass
try:
    from .models import DiscordUser
    _l_(450842)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(450844)

except ImportError:
    pass

class DiscordAuthenticationBackend(_n_(450845, "BaseBackend", lambda: BaseBackend)):
    _l_(450874)

    def authenticate(self, request, user):
        _l_(450873)

        find_user = _c_(450850, _a_(450848, _a_(450847, _n_(450846, "DiscordUser", lambda: DiscordUser), "objects"), "filter"), id=_n_(450849, "user", lambda: user)['id'])
        _l_(450851)
        if _c_(450854, _n_(450852, "len", lambda: len), _n_(450853, "find_user", lambda: find_user)) == 0:
            _l_(450870)

            _c_(450856, _n_(450855, "print", lambda: print), "User was not found. Saving...")
            _l_(450857)
            new_user = _a_(450860, _a_(450859, _n_(450858, "DiscordUser", lambda: DiscordUser), "objects"), "create_new_discord_user")
            _l_(450861)
            _n_(450862, "user", lambda: (user))
            _l_(450863)
            _c_(450866, _n_(450864, "print", lambda: print), _n_(450865, "new_user", lambda: new_user))
            _l_(450867)
            aux = _n_(450868, "new_user", lambda: new_user)
            _l_(450869)
            return aux
        aux = _n_(450871, "find_user", lambda: find_user)
        _l_(450872)
        return aux