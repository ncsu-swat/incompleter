# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Article(_a_(383049, _n_(383048, "models", lambda: models), "Model")):
    _l_(383066)

    titre=_c_(383051, _a_(383050, models, "CharField"), max_length=100)
    _l_(383052)
    auteur=_c_(383054, _a_(383053, models, "CharField"), max_length=42)
    _l_(383055)
    contenu=_c_(383057, _a_(383056, models, "TextField"), null=True)
    _l_(383058)
    date=_c_(383060, _a_(383059, models, "DateTimeField"), auto_now_add=True,
        auto_now=False,
        verbose_name="Date de parution"
    )
    _l_(383061)

    def __str__(self):
        _l_(383065)

        aux = _a_(383063, _n_(383062, "self", lambda: self), "titre")
        _l_(383064)
        return aux