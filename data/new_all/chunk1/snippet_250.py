# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57689928/why-am-i-getting-this-error-attributeerror-str-object-has-no-attribute-deco
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.tokens import PasswordResetTokenGenerator
    _l_(383218)

except ImportError:
    pass
try:
    from django.utils import six
    _l_(383220)

except ImportError:
    pass


class TokenGenerator(_n_(383221, "PasswordResetTokenGenerator", lambda: PasswordResetTokenGenerator)):
    _l_(383238)

    def _make_hash_value(self, user, timestamp):
        _l_(383237)

        aux = (
            _c_(383226, _a_(383223, _n_(383222, "six", lambda: six), "text_type"), _a_(383225, _n_(383224, "user", lambda: user), "pk")) + _c_(383230, _a_(383228, _n_(383227, "six", lambda: six), "text_type"), _n_(383229, "timestamp", lambda: timestamp)) + _c_(383235, _a_(383232, _n_(383231, "six", lambda: six), "text_type"), _a_(383234, _n_(383233, "user", lambda: user), "is_active"))
        )
        _l_(383236)
        return aux


account_activation_token = _c_(383240, _n_(383239, "TokenGenerator", lambda: TokenGenerator))
_l_(383241)