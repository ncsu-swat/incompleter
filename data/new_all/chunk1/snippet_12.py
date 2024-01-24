# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(413552)

except ImportError:
    pass

# Create your models here.
class Categorie(_a_(413554, _n_(413553, "models", lambda: models), "Model")):
    _l_(413563)

    nom = _c_(413557, _a_(413556, _n_(413555, "models", lambda: models), "CharField"), max_length=30)
    _l_(413558)

    def __str__(self):
        _l_(413562)

        aux = _a_(413560, _n_(413559, "self", lambda: self), "nom")
        _l_(413561)
        return aux


class Article(_a_(413565, _n_(413564, "models", lambda: models), "Model")):
    _l_(413590)

    titre=_c_(413568, _a_(413567, _n_(413566, "models", lambda: models), "CharField"), max_length=100)
    _l_(413569)
    auteur=_c_(413572, _a_(413571, _n_(413570, "models", lambda: models), "CharField"), max_length=42)
    _l_(413573)
    contenu=_c_(413576, _a_(413575, _n_(413574, "models", lambda: models), "TextField"), null=True)
    _l_(413577)
    date=_c_(413580, _a_(413579, _n_(413578, "models", lambda: models), "DateTimeField"), auto_now_add=True,
        auto_now=False,
        verbose_name="Date de parution"
    )
    _l_(413581)
    categorie = _c_(413584, _a_(413583, _n_(413582, "models", lambda: models), "ForeignKey"), 'Categorie')
    _l_(413585)

    def __str__(self):
        _l_(413589)

        aux = _a_(413587, _n_(413586, "self", lambda: self), "titre")
        _l_(413588)
        return aux