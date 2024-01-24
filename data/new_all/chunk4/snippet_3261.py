# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76595047/typeerror-guerrier-init-missing-1-required-positional-argument-armure
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Personnage:
    _l_(621747)

    def __init__(self, nom, sexe, couleur, pdv, experience):
        _l_(621734)

        _n_(621719, "self", lambda: self).nom = _n_(621720, "nom", lambda: nom)
        _l_(621721)
        _n_(621722, "self", lambda: self).sexe = _n_(621723, "sexe", lambda: sexe)
        _l_(621724)
        _n_(621725, "self", lambda: self).couleur = _n_(621726, "couleur", lambda: couleur)
        _l_(621727)
        _n_(621728, "self", lambda: self).pdv = _n_(621729, "pdv", lambda: pdv)
        _l_(621730)
        _n_(621731, "self", lambda: self).experience = _n_(621732, "experience", lambda: experience)
        _l_(621733)

    def attaquer(self):
        _l_(621740)

        _c_(621738, _n_(621735, "print", lambda: print), f"{_a_(621737, _n_(621736, 'self', lambda: self), 'nom')} attaque l'ennemi.")
        _l_(621739)

    def seDefendre(self):
        _l_(621746)

        _c_(621744, _n_(621741, "print", lambda: print), f"{_a_(621743, _n_(621742, 'self', lambda: self), 'nom')} se defend contre l'attaque ennemie.")
        _l_(621745)


class Guerrier(_n_(621748, "Personnage", lambda: Personnage)):
    _l_(621781)

    def __init__(self, nom, sexe, couleur, pdv, experience, force, armure):
        _l_(621764)

        _c_(621756, _a_(621750, _n_(621749, "super", lambda: super)(), "__init__"), _n_(621751, "nom", lambda: nom), _n_(621752, "sexe", lambda: sexe), _n_(621753, "couleur", lambda: couleur), _n_(621754, "pdv", lambda: pdv), _n_(621755, "experience", lambda: experience))
        _l_(621757)
        _n_(621758, "self", lambda: self).force = _n_(621759, "force", lambda: force)
        _l_(621760)
        _n_(621761, "self", lambda: self).armure = _n_(621762, "armure", lambda: armure)
        _l_(621763)

    def attaquer(self):
        _l_(621772)

        _c_(621770, _n_(621765, "print", lambda: print), f"{_a_(621767, _n_(621766, 'self', lambda: self), 'nom')} assene un puissant coup avec sa force de {_a_(621769, _n_(621768, 'self', lambda: self), 'force')}.")
        _l_(621771)

    def seDefendre(self):
        _l_(621780)

        _c_(621778, _n_(621773, "print", lambda: print), f"{_a_(621775, _n_(621774, 'self', lambda: self), 'nom')} se protege avec son armure de {_a_(621777, _n_(621776, 'self', lambda: self), 'armure')}.")
        _l_(621779)


class Mage(_n_(621782, "Personnage", lambda: Personnage)):
    _l_(621805)

    def __init__(self, nom, sexe, couleur, pdv, experience, intelligence, sorts):
        _l_(621798)

        _c_(621790, _a_(621784, _n_(621783, "super", lambda: super)(), "__init__"), _n_(621785, "nom", lambda: nom), _n_(621786, "sexe", lambda: sexe), _n_(621787, "couleur", lambda: couleur), _n_(621788, "pdv", lambda: pdv), _n_(621789, "experience", lambda: experience))
        _l_(621791)
        _n_(621792, "self", lambda: self).intelligence = _n_(621793, "intelligence", lambda: intelligence)
        _l_(621794)
        _n_(621795, "self", lambda: self).sorts = _n_(621796, "sorts", lambda: sorts)
        _l_(621797)

    def lancer_sort(self):
        _l_(621804)

        _c_(621802, _n_(621799, "print", lambda: print), f"{_a_(621801, _n_(621800, 'self', lambda: self), 'nom')} lance un sort puissant avec son intelligence.")
        _l_(621803)

class GuerrierMage(_n_(621806, "Guerrier", lambda: Guerrier), _n_(621807, "Mage", lambda: Mage)):
    _l_(621831)

    def __init__(self, nom, sexe, couleur, pdv, experience, force, armure):
        _l_(621830)

        _c_(621817, _a_(621809, _n_(621808, "Guerrier", lambda: Guerrier), "__init__"), _n_(621810, "nom", lambda: nom), _n_(621811, "sexe", lambda: sexe), _n_(621812, "couleur", lambda: couleur), _n_(621813, "pdv", lambda: pdv), _n_(621814, "experience", lambda: experience), _n_(621815, "force", lambda: force), _n_(621816, "armure", lambda: armure))
        _l_(621818)
        _c_(621828, _a_(621820, _n_(621819, "Mage", lambda: Mage), "__init__"), _n_(621821, "nom", lambda: nom), _n_(621822, "sexe", lambda: sexe), _n_(621823, "couleur", lambda: couleur), _n_(621824, "pdv", lambda: pdv), _n_(621825, "experience", lambda: experience),_n_(621826, "intelligence", lambda: intelligence),_n_(621827, "sorts", lambda: sorts))
        _l_(621829)


# Creation d'une instance de la classe GuerrierMage
guerriermage1 = _c_(621833, _n_(621832, "GuerrierMage", lambda: GuerrierMage), "GuerrierMage1", "masculin", "rouge", 100, 10, 8, "arrmure")
_l_(621834)