# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(699026)

except ImportError:
    pass

class Category(_a_(699028, _n_(699027, "models", lambda: models), "Model")):
    _l_(699040)

    name = _c_(699031, _a_(699030, _n_(699029, "models", lambda: models), "CharField"), max_length = 20, unique = True)
    _l_(699032)

    def __str__(self):
        _l_(699036)

        aux = _a_(699034, _n_(699033, "self", lambda: self), "name")
        _l_(699035)
        return aux

    class Meta:
        _l_(699039)

        verbose_name = "Категория"
        _l_(699037)
        verbose_name_plural = "Категории"
        _l_(699038)

class Item(_a_(699042, _n_(699041, "models", lambda: models), "Model")):
    _l_(699077)

    category = _c_(699048, _a_(699044, _n_(699043, "models", lambda: models), "ForeignKey"), _n_(699045, "Category", lambda: Category), on_delete = _a_(699047, _n_(699046, "models", lambda: models), "CASCADE"))
    _l_(699049)
    name = _c_(699052, _a_(699051, _n_(699050, "models", lambda: models), "CharField"), max_length = 20, default = "Unknown")
    _l_(699053)
    item_desc = _c_(699056, _a_(699055, _n_(699054, "models", lambda: models), "TextField"), default = "Empty")
    _l_(699057)
    publish_date = _c_(699060, _a_(699059, _n_(699058, "models", lambda: models), "DateTimeField"), auto_now = True)
    _l_(699061)
    price = _c_(699064, _a_(699063, _n_(699062, "models", lambda: models), "CharField"), max_length = 20, default = 0)
    _l_(699065)
    quanty = _c_(699068, _a_(699067, _n_(699066, "models", lambda: models), "CharField"), max_length = 10000, default = 0)
    _l_(699069)

    def __str__(self):
        _l_(699073)

        aux = _a_(699071, _n_(699070, "self", lambda: self), "name") + "  "
        _l_(699072)
        return aux

    class Meta:
        _l_(699076)

        verbose_name = "Предмет"
        _l_(699074)
        verbose_name_plural = "Предметы"
        _l_(699075)

class Comment(_a_(699079, _n_(699078, "models", lambda: models), "Model")):
    _l_(699106)

    item = _c_(699085, _a_(699081, _n_(699080, "models", lambda: models), "ForeignKey"), _n_(699082, "Item", lambda: Item), on_delete = _a_(699084, _n_(699083, "models", lambda: models), "CASCADE"))
    _l_(699086)
    author_name = _c_(699089, _a_(699088, _n_(699087, "models", lambda: models), "CharField"), max_length = 20, unique = True)
    _l_(699090)
    comment_text = _c_(699093, _a_(699092, _n_(699091, "models", lambda: models), "TextField"), default = "Empty")
    _l_(699094)
    publish_date = _c_(699097, _a_(699096, _n_(699095, "models", lambda: models), "DateTimeField"), auto_now = True)
    _l_(699098)

    def __str__(self):
        _l_(699102)

        aux = _a_(699100, _n_(699099, "self", lambda: self), "author_name") + "  "
        _l_(699101)
        return aux

    class Meta:
        _l_(699105)

        verbose_name = "Комментарий"
        _l_(699103)
        verbose_name_plural = "Комментарии"
        _l_(699104)