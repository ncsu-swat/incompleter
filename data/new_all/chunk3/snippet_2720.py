# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65325108/i-keep-getting-a-type-error-got-str-instead-of-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(540181)

except ImportError:
    pass
usernames_passwords = _c_(540183, _n_(540182, "open", lambda: open), "username_password.pck", "wb")
_l_(540184)
customer_login = []
_l_(540185)
_c_(540190, _a_(540187, _n_(540186, "pickle", lambda: pickle), "dump"), _n_(540188, "customer_login", lambda: customer_login), _n_(540189, "usernames_passwords", lambda: usernames_passwords), "wb")
_l_(540191)
_c_(540194, _a_(540193, _n_(540192, "usernames_passwords", lambda: usernames_passwords), "close"))
_l_(540195)