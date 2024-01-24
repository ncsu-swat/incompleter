# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53198653/super-new-cls-args-kwargs-reports-an-error-typeerror-object-take
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Personne:
    _l_(567016)

    def __init__(self, nom, prenom):
        _l_(567001)

        _c_(566993, _n_(566992, "print", lambda: print), "Appel de la méthode __init__")
        _l_(566994)
        _n_(566995, "self", lambda: self).nom = _n_(566996, "nom", lambda: nom)
        _l_(566997)
        _n_(566998, "self", lambda: self).prenom = _n_(566999, "prenom", lambda: prenom)
        _l_(567000)

    def __new__(cls, nom, prenom):
        _l_(567015)

        _c_(567006, _n_(567002, "print", lambda: print), _c_(567005, _a_(567003, "Appel de la méthode __new__ de la classe {}", "format"), _n_(567004, "cls", lambda: cls)))
        _l_(567007)
        aux = _c_(567013, _a_(567009, _n_(567008, "object", lambda: object), "__new__"), _n_(567010, "cls", lambda: cls), _n_(567011, "nom", lambda: nom), _n_(567012, "prenom", lambda: prenom))
        _l_(567014)
        return aux

personne = _c_(567018, _n_(567017, "Personne", lambda: Personne), "Doe", "John")
_l_(567019)