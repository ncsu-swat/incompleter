# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/22664491/typeerror-unsupported-operand-types-for-float-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(441733)

except ImportError:
    pass
initial_val = _c_(441735, _n_(441734, "str", lambda: str), 10)
_l_(441736)
attr_c1_stre = ("Character 1's Strength: ",_c_(441745, _n_(441737, "str", lambda: str), _c_(441740, _a_(441739, _n_(441738, "random", lambda: random), "randint"), 1,12)/_c_(441743, _a_(441742, _n_(441741, "random", lambda: random), "randint"), 1,4)     + _n_(441744, "initial_val", lambda: initial_val)))
_l_(441746)
attr_c1_skill = ("Character 1's Skill: ",_c_(441755, _n_(441747, "str", lambda: str), _c_(441750, _a_(441749, _n_(441748, "random", lambda: random), "randint"), 1,12)/_c_(441753, _a_(441752, _n_(441751, "random", lambda: random), "randint"), 1,4) +     _n_(441754, "initial_val", lambda: initial_val)))
_l_(441756)
attr_c2_stre = ("Character 2's Strength: ",_c_(441765, _n_(441757, "str", lambda: str), _c_(441760, _a_(441759, _n_(441758, "random", lambda: random), "randint"), 1,12)/_c_(441763, _a_(441762, _n_(441761, "random", lambda: random), "randint"), 1,4)     + _n_(441764, "initial_val", lambda: initial_val)))
_l_(441766)
attr_c2_skill = ("Character 2's Skill: ",_c_(441775, _n_(441767, "str", lambda: str), _c_(441770, _a_(441769, _n_(441768, "random", lambda: random), "randint"), 1,12)/_c_(441773, _a_(441772, _n_(441771, "random", lambda: random), "randint"), 1,4) +     _n_(441774, "initial_val", lambda: initial_val)))
_l_(441776)
_c_(441778, _n_(441777, "print", lambda: print), "attr_c1_stre", "\nattr_c1_skil", "\n\nattr_c2_stre","\nattr_c2_skill")
_l_(441779)
file = _c_(441781, _n_(441780, "open", lambda: open), "Attribute.txt", "w")
_l_(441782)
_c_(441786, _a_(441784, _n_(441783, "file", lambda: file), "write"), _n_(441785, "attributes", lambda: attributes))
_l_(441787)
_c_(441790, _a_(441789, _n_(441788, "file", lambda: file), "close"))
_l_(441791)
_c_(441793, _n_(441792, "input", lambda: input), "\n\nPress enter to exit")
_l_(441794)