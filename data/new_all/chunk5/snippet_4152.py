# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62234344/why-does-my-code-say-nameerror-name-self-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(701454)

except ImportError:
    pass
def getName():
    _l_(701476)

    syllables = ['en','da','fu','ka','re','toh','ko','noh','tuk','el','kar']
    _l_(701455)
    firstName = _c_(701459, _a_(701457, _n_(701456, "random", lambda: random), "choice"), _n_(701458, "syllables", lambda: syllables))
    _l_(701460)
    secondName = _c_(701464, _a_(701462, _n_(701461, "random", lambda: random), "choice"), _n_(701463, "syllables", lambda: syllables))
    _l_(701465)
    thirdName = _c_(701469, _a_(701467, _n_(701466, "random", lambda: random), "choice"), _n_(701468, "syllables", lambda: syllables))
    _l_(701470)
    global generatedName
    _l_(701471)
    generatedName = _n_(701472, "firstName", lambda: firstName)+'-'+_n_(701473, "secondName", lambda: secondName)+'-'+_n_(701474, "thirdName", lambda: thirdName)
    _l_(701475)



# Classes-all creatures have names generated the same way and have the same amount of health.
# The way I have selected how each subclass will be randomly chosen is having the code select a random value
# from the list and depending on which is chosen it will give a subclass.
class preset():
    _l_(701489)

    def _init_(self, creature, name, health=100):
        _l_(701488)

        _n_(701477, "self", lambda: self).name = _n_(701478, "generatedName", lambda: generatedName)
        _l_(701479)
        _n_(701480, "self", lambda: self).health = 100
        _l_(701481)
        _c_(701483, _n_(701482, "getName", lambda: getName))
        _l_(701484)
        _n_(701485, "self", lambda: self).name=_n_(701486, "generatedName", lambda: generatedName)
        _l_(701487)


#Gives different attributes to each sub-class        
class barbarian(_n_(701490, "preset", lambda: preset)):
    _l_(701537)

    def _init_(self, name, power=70, specialAttackPower=20, speed=50):
        _l_(701510)

        _c_(701496, _a_(701492, _n_(701491, "preset", lambda: preset), "_init_"), _n_(701493, "self", lambda: self), _n_(701494, "creature", lambda: creature), _n_(701495, "name", lambda: name), health=100)
        _l_(701497)
        _n_(701498, "self", lambda: self).power = _n_(701499, "power", lambda: power)
        _l_(701500)
        _n_(701501, "self", lambda: self).specialAttackPower = _n_(701502, "specialAttackPower", lambda: specialAttackPower)
        _l_(701503)
        _n_(701504, "self", lambda: self).speed = _n_(701505, "speed", lambda: speed)
        _l_(701506)
        _n_(701507, "self", lambda: self).name = _n_(701508, "name", lambda: name)
        _l_(701509)

    def returnBarbarianStats():
        _l_(701536)

        _c_(701514, _n_(701511, "print", lambda: print), _a_(701513, _n_(701512, "self", lambda: self), "name"),"the barbarian's stats:")
        _l_(701515)
        _c_(701519, _n_(701516, "print", lambda: print), "Health:",_a_(701518, _n_(701517, "self", lambda: self), "health"))
        _l_(701520)
        _c_(701524, _n_(701521, "print", lambda: print), "Power damage:",_a_(701523, _n_(701522, "self", lambda: self), "power"))
        _l_(701525)
        _c_(701529, _n_(701526, "print", lambda: print), "Special attack power damage:",_a_(701528, _n_(701527, "self", lambda: self), "specialAttackPower"))
        _l_(701530)
        _c_(701534, _n_(701531, "print", lambda: print), "Speed:",_a_(701533, _n_(701532, "self", lambda: self), "speed"))
        _l_(701535)

class elf(_n_(701538, "preset", lambda: preset)):
    _l_(701556)

    def _init_(self, name, power=30, specialAttackPower=60, speed=10):
        _l_(701555)

        _c_(701544, _a_(701540, _n_(701539, "preset", lambda: preset), "_init_"), _n_(701541, "self", lambda: self), _n_(701542, "creature", lambda: creature), _n_(701543, "name", lambda: name), health=100)
        _l_(701545)
        _n_(701546, "self", lambda: self).power = _n_(701547, "power", lambda: power)
        _l_(701548)
        _n_(701549, "self", lambda: self).specialAttackPower = _n_(701550, "specialAttackPower", lambda: specialAttackPower)
        _l_(701551)
        _n_(701552, "self", lambda: self).speed = _n_(701553, "speed", lambda: speed)
        _l_(701554)

class wizard(_n_(701557, "preset", lambda: preset)):
    _l_(701575)

    def _init_(self, name, power=50, specialAttackPower=70, speed=30):
        _l_(701574)

        _c_(701563, _a_(701559, _n_(701558, "preset", lambda: preset), "_init_"), _n_(701560, "self", lambda: self), _n_(701561, "creature", lambda: creature), _n_(701562, "name", lambda: name), health=100)
        _l_(701564)
        _n_(701565, "self", lambda: self).power = _n_(701566, "power", lambda: power)
        _l_(701567)
        _n_(701568, "self", lambda: self).specialAttackPower = _n_(701569, "specialAttackPower", lambda: specialAttackPower)
        _l_(701570)
        _n_(701571, "self", lambda: self).speed = _n_(701572, "speed", lambda: speed)
        _l_(701573)

class dragon(_n_(701576, "preset", lambda: preset)):
    _l_(701594)

    def _init_(self, name, power=90, specialAttackPower=40, speed=50):
        _l_(701593)

        _c_(701582, _a_(701578, _n_(701577, "preset", lambda: preset), "_init_"), _n_(701579, "self", lambda: self), _n_(701580, "creature", lambda: creature), _n_(701581, "name", lambda: name), health=100)
        _l_(701583)
        _n_(701584, "self", lambda: self).power = _n_(701585, "power", lambda: power)
        _l_(701586)
        _n_(701587, "self", lambda: self).specialAttackPower = _n_(701588, "specialAttackPower", lambda: specialAttackPower)
        _l_(701589)
        _n_(701590, "self", lambda: self).speed = _n_(701591, "speed", lambda: speed)
        _l_(701592)

class knight(_n_(701595, "preset", lambda: preset)):
    _l_(701613)

    def _init_(self, name, power=60, specialAttackPower=10, speed=60):
        _l_(701612)

        _c_(701601, _a_(701597, _n_(701596, "preset", lambda: preset), "_init_"), _n_(701598, "self", lambda: self), _n_(701599, "creature", lambda: creature), _n_(701600, "name", lambda: name), health=100)
        _l_(701602)
        _n_(701603, "self", lambda: self).power = _n_(701604, "power", lambda: power)
        _l_(701605)
        _n_(701606, "self", lambda: self).specialAttackPower = _n_(701607, "specialAttackPower", lambda: specialAttackPower)
        _l_(701608)
        _n_(701609, "self", lambda: self).speed = _n_(701610, "speed", lambda: speed)
        _l_(701611)

#10 randomly generated characters.
i = 0
_l_(701614)
army = []
_l_(701615)
while _n_(701616, "i", lambda: i) < 10:
    _l_(701665)

    creatures = ['barbarian','elf','wizard','dragon','knight']
    _l_(701617)
    creatureType = _c_(701621, _a_(701619, _n_(701618, "random", lambda: random), "choice"), _n_(701620, "creatures", lambda: creatures))
    _l_(701622)
    if _n_(701623, "creatureType", lambda: creatureType) == 'barbarian':
        _l_(701662)

        _c_(701628, _a_(701625, _n_(701624, "army", lambda: army), "append"), _c_(701627, _n_(701626, "barbarian", lambda: barbarian)))
        _l_(701629)
    elif _n_(701630, "creatureType", lambda: creatureType) == 'elf':
        _l_(701661)

        _c_(701635, _a_(701632, _n_(701631, "army", lambda: army), "append"), _c_(701634, _n_(701633, "elf", lambda: elf)))
        _l_(701636)
    elif _n_(701637, "creatureType", lambda: creatureType) == 'wizard':
        _l_(701660)

        _c_(701642, _a_(701639, _n_(701638, "army", lambda: army), "append"), _c_(701641, _n_(701640, "wizard", lambda: wizard)))
        _l_(701643)
    elif _n_(701644, "creatureType", lambda: creatureType) == 'dragon':
        _l_(701659)

        _c_(701649, _a_(701646, _n_(701645, "army", lambda: army), "append"), _c_(701648, _n_(701647, "dragon", lambda: dragon)))
        _l_(701650)
    elif _n_(701651, "creatureType", lambda: creatureType) == 'knight':
        _l_(701658)

        _c_(701656, _a_(701653, _n_(701652, "army", lambda: army), "append"), _c_(701655, _n_(701654, "knight", lambda: knight)))
        _l_(701657)
    i = _n_(701663, "i", lambda: i) + 1
    _l_(701664)

_c_(701668, _a_(701667, _n_(701666, "barbarian", lambda: barbarian), "returnBarbarianStats"))
_l_(701669)