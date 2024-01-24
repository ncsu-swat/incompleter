# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34777773/typeerror-object-takes-no-parameters-after-defining-new
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Personne:
    _l_(413372)

    def __init__(self, nom, prenom):
        _l_(413357)

        _c_(413349, _n_(413348, "print", lambda: print), "Appel de la méthode __init__")
        _l_(413350)
        _n_(413351, "self", lambda: self).nom = _n_(413352, "nom", lambda: nom)
        _l_(413353)
        _n_(413354, "self", lambda: self).prenom = _n_(413355, "prenom", lambda: prenom)
        _l_(413356)

    def __new__(cls, nom, prenom):
        _l_(413371)

        _c_(413362, _n_(413358, "print", lambda: print), _c_(413361, _a_(413359, "Appel de la méthode __new__ de la classe {}", "format"), _n_(413360, "cls", lambda: cls)))
        _l_(413363)
        aux = _c_(413369, _a_(413365, _n_(413364, "object", lambda: object), "__new__"), _n_(413366, "cls", lambda: cls), _n_(413367, "nom", lambda: nom), _n_(413368, "prenom", lambda: prenom))
        _l_(413370)
        return aux

personne = _c_(413374, _n_(413373, "Personne", lambda: Personne), "Doe", "John")
_l_(413375)