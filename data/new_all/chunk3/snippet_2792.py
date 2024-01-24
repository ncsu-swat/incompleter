# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62930892/if-model-meta-abstract-attributeerror-type-object-productobject-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models as m
    _l_(542041)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(542043)

except ImportError:
    pass
try:
    import datetime
    _l_(542045)

except ImportError:
    pass

def mounth():
    _l_(542056)

    now = _c_(542049, _a_(542048, _a_(542047, _n_(542046, "datetime", lambda: datetime), "datetime"), "now"))
    _l_(542050)
    aux = _n_(542051, "now", lambda: now) + _c_(542054, _a_(542053, _n_(542052, "datetime", lambda: datetime), "timedelta"), days=20)
    _l_(542055)
    return aux

class Product(_a_(542058, _n_(542057, "m", lambda: m), "Model")):
    _l_(542071)

    product_name = _c_(542061, _a_(542060, _n_(542059, "m", lambda: m), "CharField"), max_length=200)
    _l_(542062)
    product_calories = _c_(542065, _a_(542064, _n_(542063, "m", lambda: m), "PositiveIntegerField"), blank=True)
    _l_(542066)

    def __str__(self):
        _l_(542070)

        aux = _a_(542068, _n_(542067, "self", lambda: self), "product_name")
        _l_(542069)
        return aux


class Fridge(_a_(542073, _n_(542072, "m", lambda: m), "Model")):
    _l_(542087)

    OPTIONS = (
        ("1", "BASIC"),
        ("2", "PRO"),
        ("3", "KING"),
    )
    _l_(542074)

    fridge_owner = _c_(542081, _a_(542076, _n_(542075, "m", lambda: m), "ForeignKey"), _a_(542078, _n_(542077, "settings", lambda: settings), "AUTH_USER_MODEL"), on_delete=_a_(542080, _n_(542079, "m", lambda: m), "CASCADE"))
    _l_(542082)
    fridge_mode = _c_(542085, _a_(542084, _n_(542083, "m", lambda: m), "CharField"), max_length=5, choices=OPTIONS)
    _l_(542086)


class Recipe(_a_(542089, _n_(542088, "m", lambda: m), "Model")):
    _l_(542107)

    recipe_name = _c_(542092, _a_(542091, _n_(542090, "m", lambda: m), "CharField"), max_length=200)
    _l_(542093)
    recipe_products = _c_(542097, _a_(542095, _n_(542094, "m", lambda: m), "ManyToManyField"), _n_(542096, "Product", lambda: Product))
    _l_(542098)
    recipe_description = _c_(542101, _a_(542100, _n_(542099, "m", lambda: m), "TextField"))
    _l_(542102)

    def __str__(self):
        _l_(542106)

        aux = _a_(542104, _n_(542103, "self", lambda: self), "recipe_name")
        _l_(542105)
        return aux


class ProductObject():
    _l_(542132)

    product_obj_fridge = _c_(542113, _a_(542109, _n_(542108, "m", lambda: m), "ForeignKey"), _n_(542110, "Fridge", lambda: Fridge), on_delete=_a_(542112, _n_(542111, "m", lambda: m), "CASCADE"))
    _l_(542114)
    product_obj_product = _c_(542118, _a_(542116, _n_(542115, "m", lambda: m), "ManyToManyField"), _n_(542117, "Product", lambda: Product))
    _l_(542119)
    product_shelf_life = _c_(542124, _a_(542121, _n_(542120, "m", lambda: m), "DateField"), default=_c_(542123, _n_(542122, "mounth", lambda: mounth)))
    _l_(542125)
    product_count = _c_(542128, _a_(542127, _n_(542126, "m", lambda: m), "PositiveIntegerField"), default=1)
    _l_(542129)

    class Meta:
        _l_(542131)

        ordering = ('product_shelf_life', )
        _l_(542130)