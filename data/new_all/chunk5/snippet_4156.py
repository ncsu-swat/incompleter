# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62234344/why-does-my-code-say-nameerror-name-self-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(698497)

except ImportError:
    pass
def getName():
    _l_(698519)

    syllables = ['en','da','fu','ka','re','toh','ko','noh','tuk','el','kar']
    _l_(698498)
    firstName = _c_(698502, _a_(698500, _n_(698499, "random", lambda: random), "choice"), _n_(698501, "syllables", lambda: syllables))
    _l_(698503)
    secondName = _c_(698507, _a_(698505, _n_(698504, "random", lambda: random), "choice"), _n_(698506, "syllables", lambda: syllables))
    _l_(698508)
    thirdName = _c_(698512, _a_(698510, _n_(698509, "random", lambda: random), "choice"), _n_(698511, "syllables", lambda: syllables))
    _l_(698513)
    global generatedName
    _l_(698514)
    generatedName = _n_(698515, "firstName", lambda: firstName)+'-'+_n_(698516, "secondName", lambda: secondName)+'-'+_n_(698517, "thirdName", lambda: thirdName)
    _l_(698518)



# Classes-all creatures have names generated the same way and have the same amount of health.
# The way I have selected how each subclass will be randomly chosen is having the code select a random value
# from the list and depending on which is chosen it will give a subclass.
class preset():
    _l_(698532)

    def _init_(self, creature, name, health=100):
        _l_(698531)

        _n_(698520, "self", lambda: self).name = _n_(698521, "generatedName", lambda: generatedName)
        _l_(698522)
        _n_(698523, "self", lambda: self).health = 100
        _l_(698524)
        _c_(698526, _n_(698525, "getName", lambda: getName))
        _l_(698527)
        _n_(698528, "self", lambda: self).name=_n_(698529, "generatedName", lambda: generatedName)
        _l_(698530)


#Gives different attributes to each sub-class        
class barbarian(_n_(698533, "preset", lambda: preset)):
    _l_(698580)

    def _init_(self, name, power=70, specialAttackPower=20, speed=50):
        _l_(698553)

        _c_(698539, _a_(698535, _n_(698534, "preset", lambda: preset), "_init_"), _n_(698536, "self", lambda: self), _n_(698537, "creature", lambda: creature), _n_(698538, "name", lambda: name), health=100)
        _l_(698540)
        _n_(698541, "self", lambda: self).power = _n_(698542, "power", lambda: power)
        _l_(698543)
        _n_(698544, "self", lambda: self).specialAttackPower = _n_(698545, "specialAttackPower", lambda: specialAttackPower)
        _l_(698546)
        _n_(698547, "self", lambda: self).speed = _n_(698548, "speed", lambda: speed)
        _l_(698549)
        _n_(698550, "self", lambda: self).name = _n_(698551, "name", lambda: name)
        _l_(698552)

    def returnBarbarianStats():
        _l_(698579)

        _c_(698557, _n_(698554, "print", lambda: print), _a_(698556, _n_(698555, "self", lambda: self), "name"),"the barbarian's stats:")
        _l_(698558)
        _c_(698562, _n_(698559, "print", lambda: print), "Health:",_a_(698561, _n_(698560, "self", lambda: self), "health"))
        _l_(698563)
        _c_(698567, _n_(698564, "print", lambda: print), "Power damage:",_a_(698566, _n_(698565, "self", lambda: self), "power"))
        _l_(698568)
        _c_(698572, _n_(698569, "print", lambda: print), "Special attack power damage:",_a_(698571, _n_(698570, "self", lambda: self), "specialAttackPower"))
        _l_(698573)
        _c_(698577, _n_(698574, "print", lambda: print), "Speed:",_a_(698576, _n_(698575, "self", lambda: self), "speed"))
        _l_(698578)

class elf(_n_(698581, "preset", lambda: preset)):
    _l_(698599)

    def _init_(self, name, power=30, specialAttackPower=60, speed=10):
        _l_(698598)

        _c_(698587, _a_(698583, _n_(698582, "preset", lambda: preset), "_init_"), _n_(698584, "self", lambda: self), _n_(698585, "creature", lambda: creature), _n_(698586, "name", lambda: name), health=100)
        _l_(698588)
        _n_(698589, "self", lambda: self).power = _n_(698590, "power", lambda: power)
        _l_(698591)
        _n_(698592, "self", lambda: self).specialAttackPower = _n_(698593, "specialAttackPower", lambda: specialAttackPower)
        _l_(698594)
        _n_(698595, "self", lambda: self).speed = _n_(698596, "speed", lambda: speed)
        _l_(698597)

class wizard(_n_(698600, "preset", lambda: preset)):
    _l_(698618)

    def _init_(self, name, power=50, specialAttackPower=70, speed=30):
        _l_(698617)

        _c_(698606, _a_(698602, _n_(698601, "preset", lambda: preset), "_init_"), _n_(698603, "self", lambda: self), _n_(698604, "creature", lambda: creature), _n_(698605, "name", lambda: name), health=100)
        _l_(698607)
        _n_(698608, "self", lambda: self).power = _n_(698609, "power", lambda: power)
        _l_(698610)
        _n_(698611, "self", lambda: self).specialAttackPower = _n_(698612, "specialAttackPower", lambda: specialAttackPower)
        _l_(698613)
        _n_(698614, "self", lambda: self).speed = _n_(698615, "speed", lambda: speed)
        _l_(698616)

class dragon(_n_(698619, "preset", lambda: preset)):
    _l_(698637)

    def _init_(self, name, power=90, specialAttackPower=40, speed=50):
        _l_(698636)

        _c_(698625, _a_(698621, _n_(698620, "preset", lambda: preset), "_init_"), _n_(698622, "self", lambda: self), _n_(698623, "creature", lambda: creature), _n_(698624, "name", lambda: name), health=100)
        _l_(698626)
        _n_(698627, "self", lambda: self).power = _n_(698628, "power", lambda: power)
        _l_(698629)
        _n_(698630, "self", lambda: self).specialAttackPower = _n_(698631, "specialAttackPower", lambda: specialAttackPower)
        _l_(698632)
        _n_(698633, "self", lambda: self).speed = _n_(698634, "speed", lambda: speed)
        _l_(698635)

class knight(_n_(698638, "preset", lambda: preset)):
    _l_(698656)

    def _init_(self, name, power=60, specialAttackPower=10, speed=60):
        _l_(698655)

        _c_(698644, _a_(698640, _n_(698639, "preset", lambda: preset), "_init_"), _n_(698641, "self", lambda: self), _n_(698642, "creature", lambda: creature), _n_(698643, "name", lambda: name), health=100)
        _l_(698645)
        _n_(698646, "self", lambda: self).power = _n_(698647, "power", lambda: power)
        _l_(698648)
        _n_(698649, "self", lambda: self).specialAttackPower = _n_(698650, "specialAttackPower", lambda: specialAttackPower)
        _l_(698651)
        _n_(698652, "self", lambda: self).speed = _n_(698653, "speed", lambda: speed)
        _l_(698654)

#10 randomly generated characters.
i = 0
_l_(698657)
army = []
_l_(698658)
while _n_(698659, "i", lambda: i) < 10:
    _l_(698708)

    creatures = ['barbarian','elf','wizard','dragon','knight']
    _l_(698660)
    creatureType = _c_(698664, _a_(698662, _n_(698661, "random", lambda: random), "choice"), _n_(698663, "creatures", lambda: creatures))
    _l_(698665)
    if _n_(698666, "creatureType", lambda: creatureType) == 'barbarian':
        _l_(698705)

        _c_(698671, _a_(698668, _n_(698667, "army", lambda: army), "append"), _c_(698670, _n_(698669, "barbarian", lambda: barbarian)))
        _l_(698672)
    elif _n_(698673, "creatureType", lambda: creatureType) == 'elf':
        _l_(698704)

        _c_(698678, _a_(698675, _n_(698674, "army", lambda: army), "append"), _c_(698677, _n_(698676, "elf", lambda: elf)))
        _l_(698679)
    elif _n_(698680, "creatureType", lambda: creatureType) == 'wizard':
        _l_(698703)

        _c_(698685, _a_(698682, _n_(698681, "army", lambda: army), "append"), _c_(698684, _n_(698683, "wizard", lambda: wizard)))
        _l_(698686)
    elif _n_(698687, "creatureType", lambda: creatureType) == 'dragon':
        _l_(698702)

        _c_(698692, _a_(698689, _n_(698688, "army", lambda: army), "append"), _c_(698691, _n_(698690, "dragon", lambda: dragon)))
        _l_(698693)
    elif _n_(698694, "creatureType", lambda: creatureType) == 'knight':
        _l_(698701)

        _c_(698699, _a_(698696, _n_(698695, "army", lambda: army), "append"), _c_(698698, _n_(698697, "knight", lambda: knight)))
        _l_(698700)
    i = _n_(698706, "i", lambda: i) + 1
    _l_(698707)

_c_(698711, _a_(698710, _n_(698709, "barbarian", lambda: barbarian), "returnBarbarianStats"))
_l_(698712)