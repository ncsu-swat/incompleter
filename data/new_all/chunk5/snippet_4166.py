# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(701088)

except ImportError:
    pass

class Category(_a_(701090, _n_(701089, "models", lambda: models), "Model")):
    _l_(701102)

    name = _c_(701093, _a_(701092, _n_(701091, "models", lambda: models), "CharField"), max_length = 20, unique = True)
    _l_(701094)

    def __str__(self):
        _l_(701098)

        aux = _a_(701096, _n_(701095, "self", lambda: self), "name")
        _l_(701097)
        return aux

    class Meta:
        _l_(701101)

        verbose_name = "Категория"
        _l_(701099)
        verbose_name_plural = "Категории"
        _l_(701100)

class Item(_a_(701104, _n_(701103, "models", lambda: models), "Model")):
    _l_(701139)

    category = _c_(701110, _a_(701106, _n_(701105, "models", lambda: models), "ForeignKey"), _n_(701107, "Category", lambda: Category), on_delete = _a_(701109, _n_(701108, "models", lambda: models), "CASCADE"))
    _l_(701111)
    name = _c_(701114, _a_(701113, _n_(701112, "models", lambda: models), "CharField"), max_length = 20, default = "Unknown")
    _l_(701115)
    item_desc = _c_(701118, _a_(701117, _n_(701116, "models", lambda: models), "TextField"), default = "Empty")
    _l_(701119)
    publish_date = _c_(701122, _a_(701121, _n_(701120, "models", lambda: models), "DateTimeField"), auto_now = True)
    _l_(701123)
    price = _c_(701126, _a_(701125, _n_(701124, "models", lambda: models), "CharField"), max_length = 20, default = 0)
    _l_(701127)
    quanty = _c_(701130, _a_(701129, _n_(701128, "models", lambda: models), "CharField"), max_length = 10000, default = 0)
    _l_(701131)

    def __str__(self):
        _l_(701135)

        aux = _a_(701133, _n_(701132, "self", lambda: self), "name") + "  "
        _l_(701134)
        return aux

    class Meta:
        _l_(701138)

        verbose_name = "Предмет"
        _l_(701136)
        verbose_name_plural = "Предметы"
        _l_(701137)

class Comment(_a_(701141, _n_(701140, "models", lambda: models), "Model")):
    _l_(701168)

    item = _c_(701147, _a_(701143, _n_(701142, "models", lambda: models), "ForeignKey"), _n_(701144, "Item", lambda: Item), on_delete = _a_(701146, _n_(701145, "models", lambda: models), "CASCADE"))
    _l_(701148)
    author_name = _c_(701151, _a_(701150, _n_(701149, "models", lambda: models), "CharField"), max_length = 20, unique = True)
    _l_(701152)
    comment_text = _c_(701155, _a_(701154, _n_(701153, "models", lambda: models), "TextField"), default = "Empty")
    _l_(701156)
    publish_date = _c_(701159, _a_(701158, _n_(701157, "models", lambda: models), "DateTimeField"), auto_now = True)
    _l_(701160)

    def __str__(self):
        _l_(701164)

        aux = _a_(701162, _n_(701161, "self", lambda: self), "author_name") + "  "
        _l_(701163)
        return aux

    class Meta:
        _l_(701167)

        verbose_name = "Комментарий"
        _l_(701165)
        verbose_name_plural = "Комментарии"
        _l_(701166)