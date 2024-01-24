# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56353632/attributeerror-at-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Category(_a_(545564, _n_(545563, "models", lambda: models), "Model")):
    _l_(545568)

    name = _c_(545566, _a_(545565, models, "CharField"), max_length=100)
    _l_(545567)

class Tag(_a_(545570, _n_(545569, "models", lambda: models), "Model")):
    _l_(545574)

    tag_name = _c_(545572, _a_(545571, models, "CharField"), max_length=30)
    _l_(545573)

class FileUp(_a_(545576, _n_(545575, "models", lambda: models), "Model")):
    _l_(545594)

    name = _c_(545580, _a_(545577, models, "ForeignKey"), _n_(545578, "Category", lambda: Category), on_delete=_a_(545579, models, "CASCADE"))
    _l_(545581)
    file = _c_(545583, _a_(545582, models, "FileField"), upload_to='path')
    _l_(545584)
    tags = _c_(545587, _a_(545585, models, "ManyToManyField"), _n_(545586, "Tag", lambda: Tag))
    _l_(545588)

    def __str__(self):
        _l_(545593)

        aux = _a_(545591, _a_(545590, _n_(545589, "self", lambda: self), "name"), "name")
        _l_(545592)
        return aux