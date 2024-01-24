# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50145204/im-getting-this-error-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(450876)

except ImportError:
    pass
try:
    import sys
    _l_(450878)

except ImportError:
    pass

class Player:
    _l_(450980)


    def __init__(self):
        _l_(450901)

        _n_(450879, "self", lambda: self).level = 1
        _l_(450880)
        _n_(450881, "self", lambda: self).exp = 0
        _l_(450882)
        _n_(450883, "self", lambda: self).gold = 0
        _l_(450884)
        _n_(450885, "self", lambda: self).maxhp = 20
        _l_(450886)
        _n_(450887, "self", lambda: self).hp = _a_(450889, _n_(450888, "self", lambda: self), "maxhp")
        _l_(450890)
        _n_(450891, "self", lambda: self).attack = 1
        _l_(450892)
        _n_(450893, "self", lambda: self).weapon = ""
        _l_(450894)
        _n_(450895, "self", lambda: self).armor = ""
        _l_(450896)
        _n_(450897, "self", lambda: self).weaponsOwned = {}
        _l_(450898)
        _n_(450899, "self", lambda: self).armorsOwned = {}
        _l_(450900)

    def checkHp(self):
        _l_(450912)

        _n_(450902, "self", lambda: self).hp = _c_(450910, _n_(450903, "max", lambda: max), 0, _c_(450909, _n_(450904, "min", lambda: min), _a_(450906, _n_(450905, "self", lambda: self), "hp"), _a_(450908, _n_(450907, "self", lambda: self), "maxhp")))
        _l_(450911)

    def deadCheck(self):
        _l_(450923)

        if _a_(450914, _n_(450913, "self", lambda: self), "hp") == 0:
            _l_(450922)

            _c_(450916, _n_(450915, "print", lambda: print), "You died!")
            _l_(450917)
            _c_(450920, _a_(450919, _n_(450918, "sys", lambda: sys), "exit"))
            _l_(450921)

    def equipArmor(self):
        _l_(450979)

        for armor in _a_(450925, _n_(450924, "self", lambda: self), "armorsOwned"):
            _l_(450950)

            select = 1
            _l_(450926)
            if _a_(450928, _n_(450927, "self", lambda: self), "armor") == _n_(450929, "armor", lambda: armor):
                _l_(450948)

                _c_(450937, _n_(450930, "print", lambda: print), _c_(450933, _n_(450931, "str", lambda: str), _n_(450932, "select", lambda: select)) + ". " + _c_(450936, _n_(450934, "str", lambda: str), _n_(450935, "armor", lambda: armor)["Name"]) + " (Equipped)")
                _l_(450938)
            else:
                _c_(450946, _n_(450939, "print", lambda: print), _c_(450942, _n_(450940, "str", lambda: str), _n_(450941, "select", lambda: select)) + ". " + _c_(450945, _n_(450943, "str", lambda: str), _n_(450944, "armor", lambda: armor)["Name"]))
                _l_(450947)
            select += 1
            _l_(450949)
        armor_choice = _c_(450952, _n_(450951, "input", lambda: input), "Type the name of the armor you would like to equip\n")
        _l_(450953)
        for i in _a_(450955, _n_(450954, "self", lambda: self), "armorsOwned"):
            _l_(450978)

            if _n_(450956, "armor_choice", lambda: armor_choice) == _n_(450957, "i", lambda: i)["Name"]:
                _l_(450977)

                if _a_(450959, _n_(450958, "self", lambda: self), "armor") == _n_(450960, "i", lambda: i):
                    _l_(450976)

                    _c_(450962, _n_(450961, "print", lambda: print), "You already have that equipped")
                    _l_(450963)
                else:
                    _n_(450964, "self", lambda: self).armor = _n_(450965, "i", lambda: i)["Name"]
                    _l_(450966)
                    _c_(450971, _n_(450967, "print", lambda: print), _c_(450970, _a_(450968, "You equipped the {}", "format"), _n_(450969, "i", lambda: i)["Name"]))
                    _l_(450972)
                    _n_(450973, "self", lambda: self).maxhp += _n_(450974, "i", lambda: i)["Effect"]
                    _l_(450975)

class Enemy:
    _l_(451013)


    def __init__(self, attack, maxhp, exp, gold):
        _l_(450996)

        _n_(450981, "self", lambda: self).exp = _n_(450982, "exp", lambda: exp)
        _l_(450983)
        _n_(450984, "self", lambda: self).gold = _n_(450985, "gold", lambda: gold)
        _l_(450986)
        _n_(450987, "self", lambda: self).maxhp = _n_(450988, "maxhp", lambda: maxhp)
        _l_(450989)
        _n_(450990, "self", lambda: self).hp = _n_(450991, "maxhp", lambda: maxhp)
        _l_(450992)
        _n_(450993, "self", lambda: self).attack = _n_(450994, "attack", lambda: attack)
        _l_(450995)

    def checkHp(self):
        _l_(451007)

        _n_(450997, "self", lambda: self).hp = _c_(451005, _n_(450998, "max", lambda: max), 0, _c_(451004, _n_(450999, "min", lambda: min), _a_(451001, _n_(451000, "self", lambda: self), "hp"), _a_(451003, _n_(451002, "self", lambda: self), "maxhp")))
        _l_(451006)

    def enemyDeadCheck(self):
        _l_(451012)

        if _a_(451009, _n_(451008, "self", lambda: self), "hp") == 0:
            _l_(451011)

            aux = True
            _l_(451010)
            return aux

class Shop:
    _l_(451015)


    armors = {"BronzeArmor":{"Name": "Bronze armor",
                             "Cost": 30,
                             "Effect": 10},
              "SilverArmor":{"Name": "Silver armor",
                             "Cost": 75,
                             "Effect": 20}}
    _l_(451014)

character = _c_(451017, _n_(451016, "Player", lambda: Player))
_l_(451018)
_c_(451024, _a_(451021, _a_(451020, _n_(451019, "character", lambda: character), "armorsOwned"), "update"), _a_(451023, _n_(451022, "Shop", lambda: Shop), "armors")["BronzeArmor"])
_l_(451025)
_c_(451028, _a_(451027, _n_(451026, "character", lambda: character), "equipArmor"))
_l_(451029)