# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62174465/typeerror-dict-object-is-not-callable-with-ordereddict-and-multiple-inheritan
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import OrderedDict
    _l_(469822)

except ImportError:
    pass
try:
    from abc import ABC, abstractmethod
    _l_(469824)

except ImportError:
    pass

class Dumpable(_n_(469825, "ABC", lambda: ABC)):
    _l_(469838)

    def __init__(self):
        _l_(469832)

        _n_(469826, "self", lambda: self).dump_settings = None
        _l_(469827)
        _c_(469830, _a_(469829, _n_(469828, "super", lambda: super)(), "__init__"))
        _l_(469831)

    def dump_settings(self, settings ):
        _l_(469837)

        _n_(469833, "self", lambda: self).dump_settings = _n_(469834, "settings", lambda: settings)
        _l_(469835)
        pass
        _l_(469836)


class ItemSet(_n_(469839, "OrderedDict", lambda: OrderedDict), _n_(469840, "Dumpable", lambda: Dumpable)):
    _l_(469866)

    def __init__(self , allow_substitution : _n_(469841, "bool", lambda: bool) = False ):
        _l_(469858)

        _c_(469846, _a_(469845, _n_(469842, "super", lambda: super)(_n_(469843, "OrderedDict", lambda: OrderedDict), _n_(469844, "self", lambda: self)), "__init__"))
        _l_(469847)
        _c_(469852, _a_(469851, _n_(469848, "super", lambda: super)(_n_(469849, "Dumpable", lambda: Dumpable),  _n_(469850, "self", lambda: self)), "__init__"))
        _l_(469853)
        # also substituting two calls above with the
        # following, do not change behavior:
        # super().__init__()
        _n_(469854, "self", lambda: self).allow_substitution = _n_(469855, "allow_substitution", lambda: allow_substitution)
        _l_(469856)
        pass
        _l_(469857)

    def dump_settings(self,settings):
        _l_(469865)

        _c_(469862, _a_(469860, _n_(469859, "super", lambda: super)(), "dump_settings"), _n_(469861, "settings", lambda: settings))
        _l_(469863)
        pass
        _l_(469864)

itemset = _c_(469868, _n_(469867, "ItemSet", lambda: ItemSet))
_l_(469869)
output = _c_(469871, _n_(469870, "open", lambda: open), "output.txt", "w", encoding="utf-8")
_l_(469872)
d= _c_(469875, _n_(469873, "dict", lambda: dict), output = _n_(469874, "output", lambda: output) , html = False )
_l_(469876)
_c_(469881, _n_(469877, "print", lambda: print), _c_(469880, _n_(469878, "repr", lambda: repr), _n_(469879, "d", lambda: d)))
_l_(469882)
# this call seems to have no problems:
_c_(469886, _a_(469884, _n_(469883, "itemset", lambda: itemset), "dump_settings"), _n_(469885, "d", lambda: d))
_l_(469887)
_c_(469892, _n_(469888, "print", lambda: print), _c_(469891, _n_(469889, "repr", lambda: repr), _n_(469890, "d", lambda: d)))
_l_(469893)
# note that the given error "'dict' object is not callable"
# has nothing to do with 'd' param because if you change
# in the followin the 'd' with a non-dictionary object,
# the error remains, for example:
# itemset.dump_settings('hello')
_c_(469897, _a_(469895, _n_(469894, "itemset", lambda: itemset), "dump_settings"), _n_(469896, "d", lambda: d))
_l_(469898)
_c_(469901, _a_(469900, _n_(469899, "output", lambda: output), "close"))
_l_(469902)