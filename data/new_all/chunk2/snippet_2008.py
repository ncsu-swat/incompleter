# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70557770/prettytable-if-lenself-rows-in-0-lencolumn-attributeerror-str-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from prettytable import *
    _l_(456158)

except ImportError:
    pass

table = _n_(456159, "PrettyTable", lambda: PrettyTable)
_l_(456160)

_c_(456163, _a_(456162, _n_(456161, "table", lambda: table), "add_column"), "", "Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) 
_l_(456164) 
_c_(456167, _a_(456166, _n_(456165, "table", lambda: table), "add_column"), "", "Type", ["Electric Type", "Water Type", "Fire Type"])
_l_(456168)

_c_(456171, _n_(456169, "print", lambda: print), _n_(456170, "table", lambda: table))
_l_(456172)