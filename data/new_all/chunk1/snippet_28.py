# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Command(_n_(396407, "BaseCommand", lambda: BaseCommand)):
    _l_(396442)


    def handle(self, *args, **options):
        _l_(396441)

        users = _c_(396411, _a_(396410, _a_(396409, _n_(396408, "User", lambda: User), "objects"), "all"))
        _l_(396412)
        try:
            _l_(396440)

            for user in _n_(396413, "users", lambda: users):
                _l_(396434)

                hostname = '%s.%s' % (_a_(396415, _n_(396414, "user", lambda: user), "username"), _a_(396417, _n_(396416, "settings", lambda: settings), "NETWORK_DOMAIN"))
                _l_(396418)
                stats = _c_(396432, _a_(396421, _a_(396420, _n_(396419, "Stats", lambda: Stats), "objects"), "update_or_create"), user=_n_(396422, "user", lambda: user),
                    views=_c_(396425, _n_(396423, "display_pageviews", lambda: display_pageviews), _n_(396424, "hostname", lambda: hostname)),
                    visits=_c_(396428, _n_(396426, "display_visits", lambda: display_visits), _n_(396427, "hostname", lambda: hostname)),
                    unique_visits=_c_(396431, _n_(396429, "display_unique_visits", lambda: display_unique_visits), _n_(396430, "hostname", lambda: hostname)),)
                _l_(396433)
        except _n_(396435, "FieldError", lambda: FieldError):
            _l_(396439)

            _c_(396437, _n_(396436, "print", lambda: print), 'There was a field error.')
            _l_(396438)