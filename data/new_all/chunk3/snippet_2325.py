# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50546057/nameerror-name-default-string-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TripleString:
    _l_(575826)


    # intended class constants

    MIN_LEN = 1
    _l_(575823)
    MAX_LEN = 50
    _l_(575824)
    DEFAULT_STRING = "(undefined)"
    _l_(575825)


# constructor method

def __init__(self, string1 = _n_(575827, "DEFAULT_STRING", lambda: DEFAULT_STRING), string2 = _n_(575828, "DEFAULT_STRING", lambda: DEFAULT_STRING),
            string3 = _n_(575829, "DEFAULT_STRING", lambda: DEFAULT_STRING)):
    _l_(575857)


    # assigning default values to the variables first

    _n_(575830, "self", lambda: self).string1 = _a_(575832, _n_(575831, "self", lambda: self), "DEFAULT_STRING")
    _l_(575833)

    _n_(575834, "self", lambda: self).string2 = _a_(575836, _n_(575835, "self", lambda: self), "DEFAULT_STRING")
    _l_(575837)

    _n_(575838, "self", lambda: self).string3 = _a_(575840, _n_(575839, "self", lambda: self), "DEFAULT_STRING")
    _l_(575841)

    # setting values using setter methods,

    _c_(575845, _a_(575843, _n_(575842, "self", lambda: self), "set_string1"), _n_(575844, "string1", lambda: string1))
    _l_(575846)

    _c_(575850, _a_(575848, _n_(575847, "self", lambda: self), "set_string2"), _n_(575849, "string2", lambda: string2))
    _l_(575851)

    _c_(575855, _a_(575853, _n_(575852, "self", lambda: self), "set_string3"), _n_(575854, "string3", lambda: string3))
    _l_(575856)


# mutator ("set") methods

def set_string1(self, string1):
    _l_(575868)

    if _c_(575861, _a_(575859, _n_(575858, "self", lambda: self), "valid_string"), _n_(575860, "string1", lambda: string1)):
        _l_(575866)

        _n_(575862, "self", lambda: self).string1 = _n_(575863, "string1", lambda: string1)
        _l_(575864)
        aux = True
        _l_(575865)

        return aux
    aux = False
    _l_(575867)

    return aux


def set_string2(self, string2):
    _l_(575879)

    if _c_(575872, _a_(575870, _n_(575869, "self", lambda: self), "valid_string"), _n_(575871, "string2", lambda: string2)):
        _l_(575877)

        _n_(575873, "self", lambda: self).string2 = _n_(575874, "string2", lambda: string2)
        _l_(575875)
        aux = True
        _l_(575876)

        return aux
    aux = False
    _l_(575878)

    return aux


def set_string3(self, string3):
    _l_(575890)

    if _c_(575883, _a_(575881, _n_(575880, "self", lambda: self), "valid_string"), _n_(575882, "string3", lambda: string3)):
        _l_(575888)

        _n_(575884, "self", lambda: self).string3 = _n_(575885, "string3", lambda: string3)
        _l_(575886)
        aux = True
        _l_(575887)

        return aux
    aux = False
    _l_(575889)

    return aux


# accessor ("get") methods

def get_string1(self):
    _l_(575894)

    aux = _a_(575892, _n_(575891, "self", lambda: self), "string1")
    _l_(575893)
    return aux


def get_string2(self):
    _l_(575898)

    aux = _a_(575896, _n_(575895, "self", lambda: self), "string2")
    _l_(575897)
    return aux


def get_string3(self):
    _l_(575902)

    aux = _a_(575900, _n_(575899, "self", lambda: self), "string3")
    _l_(575901)
    return aux


def to_string(self):
    _l_(575910)

    aux = _a_(575904, _n_(575903, "self", lambda: self), "string1") + ", " + _a_(575906, _n_(575905, "self", lambda: self), "string2") + ", " + _a_(575908, _n_(575907, "self", lambda: self), "string3")
    _l_(575909)
    return aux


# helper methods for entire class

def valid_string(self, the_str):
    _l_(575924)

    if _c_(575913, _n_(575911, "len", lambda: len), _n_(575912, "the_str", lambda: the_str)) >= _a_(575915, _n_(575914, "self", lambda: self), "MIN_LEN") and _c_(575918, _n_(575916, "len", lambda: len), _n_(575917, "the_str", lambda: the_str)) <= _a_(575920, _n_(575919, "self", lambda: self), "MAX_LEN"):
        _l_(575922)

        aux = True
        _l_(575921)
        return aux
    aux = False
    _l_(575923)

    return aux


# ------------- CLIENT --------------------------------------------------

# Create 4 TripleString objects and printing

triple_string_num_1 = _c_(575926, _n_(575925, "TripleString", lambda: TripleString))
_l_(575927)

_c_(575932, _n_(575928, "print", lambda: print), _c_(575931, _a_(575930, _n_(575929, "triple_string_num_1", lambda: triple_string_num_1), "to_string")))
_l_(575933)

triple_string_num_2 = _c_(575935, _n_(575934, "TripleString", lambda: TripleString), "Alice")
_l_(575936)

_c_(575941, _n_(575937, "print", lambda: print), _c_(575940, _a_(575939, _n_(575938, "triple_string_num_2", lambda: triple_string_num_2), "to_string")))
_l_(575942)

triple_string_num_3 = _c_(575944, _n_(575943, "TripleString", lambda: TripleString), "Bob", "Chris")
_l_(575945)

_c_(575950, _n_(575946, "print", lambda: print), _c_(575949, _a_(575948, _n_(575947, "triple_string_num_3", lambda: triple_string_num_3), "to_string")))
_l_(575951)

triple_string_num_4 = _c_(575953, _n_(575952, "TripleString", lambda: TripleString), "Oliver", "Laurel", "Thea")
_l_(575954)

_c_(575959, _n_(575955, "print", lambda: print), _c_(575958, _a_(575957, _n_(575956, "triple_string_num_4", lambda: triple_string_num_4), "to_string")))
_l_(575960)

_c_(575962, _n_(575961, "print", lambda: print), "")
_l_(575963)

# mutating values using setter methods

_c_(575966, _a_(575965, _n_(575964, "triple_string_num_1", lambda: triple_string_num_1), "set_string1"), "Lance")
_l_(575967)

_c_(575970, _a_(575969, _n_(575968, "triple_string_num_2", lambda: triple_string_num_2), "set_string2"), "XYZ")
_l_(575971)

_c_(575974, _a_(575973, _n_(575972, "triple_string_num_3", lambda: triple_string_num_3), "set_string1"), "Bobby")
_l_(575975)

_c_(575978, _a_(575977, _n_(575976, "triple_string_num_4", lambda: triple_string_num_4), "set_string2"), "Felicity")
_l_(575979)

_c_(575984, _n_(575980, "print", lambda: print), _c_(575983, _a_(575982, _n_(575981, "triple_string_num_1", lambda: triple_string_num_1), "to_string")))
_l_(575985)

_c_(575990, _n_(575986, "print", lambda: print), _c_(575989, _a_(575988, _n_(575987, "triple_string_num_2", lambda: triple_string_num_2), "to_string")))
_l_(575991)

_c_(575996, _n_(575992, "print", lambda: print), _c_(575995, _a_(575994, _n_(575993, "triple_string_num_3", lambda: triple_string_num_3), "to_string")))
_l_(575997)

_c_(576002, _n_(575998, "print", lambda: print), _c_(576001, _a_(576000, _n_(575999, "triple_string_num_4", lambda: triple_string_num_4), "to_string")))
_l_(576003)

_c_(576005, _n_(576004, "print", lambda: print), "")
_l_(576006)

# testing if validation working properly

if _c_(576009, _a_(576008, _n_(576007, "triple_string_num_4", lambda: triple_string_num_4), "set_string2"), ""):
    _l_(576022)


    _c_(576011, _n_(576010, "print", lambda: print), "successful in setting empty string for string2 of 4th object," + \
          "validation is not working properly")
    _l_(576012)

else:

    _c_(576014, _n_(576013, "print", lambda: print), "failed in setting empty string for string2 of 4th object," + \
        "validation is working properly")
    _l_(576015)

    _c_(576020, _n_(576016, "print", lambda: print), "Value after setting: ", _c_(576019, _a_(576018, _n_(576017, "triple_string_num_4", lambda: triple_string_num_4), "get_string2")))
    _l_(576021)