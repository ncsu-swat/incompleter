# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62930892/if-model-meta-abstract-attributeerror-type-object-productobject-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(545857)

except ImportError:
    pass
try:
    from .models import Product, Fridge, Recipe, ProductObject
    _l_(545859)

except ImportError:
    pass
try:
    from tinymce.widgets import TinyMCE
    _l_(545861)

except ImportError:
    pass
try:
    from django.db import models
    _l_(545863)

except ImportError:
    pass
# Register your models here.


class RecipeAdmin(_a_(545865, _n_(545864, "admin", lambda: admin), "ModelAdmin")):
    _l_(545870)

    formfield_overrides = {
        _a_(545867, _n_(545866, "models", lambda: models), "TextField"): {'widget': _n_(545868, "TinyMCE", lambda: TinyMCE)}
    }
    _l_(545869)

_c_(545877, _a_(545873, _a_(545872, _n_(545871, "admin", lambda: admin), "site"), "register"), [_n_(545874, "Product", lambda: Product), _n_(545875, "Fridge", lambda: Fridge), _n_(545876, "ProductObject", lambda: ProductObject)])
_l_(545878)
_c_(545884, _a_(545881, _a_(545880, _n_(545879, "admin", lambda: admin), "site"), "register"), _n_(545882, "Recipe", lambda: Recipe), _n_(545883, "RecipeAdmin", lambda: RecipeAdmin))
_l_(545885)