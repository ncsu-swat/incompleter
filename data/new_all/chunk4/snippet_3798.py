# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66828430/django-type-error-an-integer-is-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(600445)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(600447)

except ImportError:
    pass
try:
    from store.models import product, customer
    _l_(600449)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(600451)

except ImportError:
    pass

User = _a_(600453, _n_(600452, "settings", lambda: settings), "AUTH_USER_MODEL")
_l_(600454)
class CartManager(_a_(600456, _n_(600455, "models", lambda: models), "Manager")):
    _l_(600523)

    def new_or_get(self, request):
        _l_(600505)

        cart_id = _c_(600460, _a_(600459, _a_(600458, _n_(600457, "request", lambda: request), "session"), "get"), "cart_id", default= None)
        _l_(600461)
        qs = _c_(600467, _a_(600465, _c_(600464, _a_(600463, _n_(600462, "self", lambda: self), "get_queryset")), "filter"), id =_n_(600466, "cart_id", lambda: cart_id))
        _l_(600468)
        if _c_(600471, _a_(600470, _n_(600469, "qs", lambda: qs), "count"))==1:
            _l_(600504)

            new_obj = False
            _l_(600472)
            cart_obj = _c_(600475, _a_(600474, _n_(600473, "qs", lambda: qs), "first"))
            _l_(600476)
            if _c_(600480, _a_(600479, _a_(600478, _n_(600477, "request", lambda: request), "user"), "is_authenticated")) and _a_(600482, _n_(600481, "cart_obj", lambda: cart_obj), "user") is None:
                _l_(600500)

                _n_(600483, "cart_obj", lambda: cart_obj)-_c_(600485, _n_(600484, "save", lambda: save))
                _l_(600486)
            else:
                cart_obj = _c_(600492, _a_(600489, _a_(600488, _n_(600487, "cart", lambda: cart), "objects"), "new"), user=_a_(600491, _n_(600490, "request", lambda: request), "user"))
                _l_(600493)
                new_obj = True
                _l_(600494)
                _a_(600496, _n_(600495, "request", lambda: request), "session")['cart_id'] = _a_(600498, _n_(600497, "cart_obj", lambda: cart_obj), "id")
                _l_(600499)
            aux = _n_(600501, "cart_obj", lambda: cart_obj), _n_(600502, "new_obj", lambda: new_obj)
            _l_(600503)
            return aux

    def new(self, user = None):
        _l_(600522)

        user_obj = None
        _l_(600506)
        if _n_(600507, "user", lambda: user) is not None:
            _l_(600514)

            if _n_(600508, "user", lambda: user) is _c_(600510, _n_(600509, "authenticated", lambda: authenticated)):
                _l_(600513)

                user_obj = _n_(600511, "user", lambda: user)
                _l_(600512)
        aux = _c_(600520, _a_(600518, _a_(600517, _a_(600516, _n_(600515, "self", lambda: self), "model"), "objects"), "create"), user=_n_(600519, "user_obj", lambda: user_obj))
        _l_(600521)
        return aux

class cart(_a_(600525, _n_(600524, "models", lambda: models), "Model")):
    _l_(600558)

    user = _c_(600531, _a_(600527, _n_(600526, "models", lambda: models), "ForeignKey"), _n_(600528, "User", lambda: User), blank = True, null=True, on_delete=_a_(600530, _n_(600529, "models", lambda: models), "CASCADE"))
    _l_(600532)
    product = _c_(600535, _a_(600534, _n_(600533, "models", lambda: models), "ManyToManyField"), 'store.product')
    _l_(600536)
    total = _c_(600539, _a_(600538, _n_(600537, "models", lambda: models), "DecimalField"), default = 0.0, max_digits = 50.00, decimal_places = 2)
    _l_(600540)
    updated = _c_(600543, _a_(600542, _n_(600541, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(600544)
    timestamp = _c_(600547, _a_(600546, _n_(600545, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(600548)
    objects = _c_(600550, _n_(600549, "CartManager", lambda: CartManager))
    _l_(600551)

    def __str__(self):
        _l_(600557)

        aux = _c_(600555, _n_(600552, "str", lambda: str), _a_(600554, _n_(600553, "self", lambda: self), "id"))
        _l_(600556)
        return aux