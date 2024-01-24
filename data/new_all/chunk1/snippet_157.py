# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49809261/attributeerror-type-object-user-has-no-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.models import User
    _l_(383937)

except ImportError:
    pass

class UserType(_n_(383938, "DjangoObjectType", lambda: DjangoObjectType)):
    _l_(383942)

    class Meta:
        _l_(383941)

        model = _n_(383939, "User", lambda: User)
        _l_(383940)