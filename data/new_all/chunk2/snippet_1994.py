# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71565180/typeerror-a-bytes-like-object-is-required-not-binary-when-using-boto3-and-dy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
async def authenticate(email: _n_(425360, "str", lambda: str) = _c_(425362, _n_(425361, "Form", lambda: Form), ...), password: _n_(425363, "str", lambda: str) = _c_(425365, _n_(425364, "Form", lambda: Form), ...)):
    _l_(425378)

    response = _c_(425369, _a_(425367, _n_(425366, "table", lambda: table), "get_item"), Key={'email': _n_(425368, "email", lambda: email)})
    _l_(425370)
    item = _n_(425371, "response", lambda: response)['Item']
    _l_(425372)
    stored_salt = _n_(425373, "item", lambda: item)['salt']
    _l_(425374)
    stored_password = _n_(425375, "item", lambda: item)['password']
    _l_(425376)
    ...
    _l_(425377)