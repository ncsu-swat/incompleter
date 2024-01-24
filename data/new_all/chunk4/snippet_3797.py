# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66836972/python-validate-email-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from validate_email import validate_email
    _l_(591269)

except ImportError:
    pass
is_valid = _c_(591271, _n_(591270, "validate_email", lambda: validate_email), 'example@example.com',verify=True)
_l_(591272)