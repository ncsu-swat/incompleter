# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38146756/typeerror-cant-convert-io-textiowrapper-object-to-str-implicitly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(652728)

except ImportError:
    pass
try:
    import pandas as pa
    _l_(652730)

except ImportError:
    pass

# opening the file
dossier = "Plip"
_l_(652731)
fichier = "plop.txt"
_l_(652732)
fichier = _c_(652736, _n_(652733, "open", lambda: open), _n_(652734, "dossier", lambda: dossier) + "/" + _n_(652735, "fichier", lambda: fichier))
_l_(652737)
data = _c_(652740, _a_(652739, _n_(652738, "fichier", lambda: fichier), "readlines"))
_l_(652741)

# creating the data frame
Pair = []
_l_(652742)
Impair = []
_l_(652743)
for m in _n_(652744, "data", lambda: data):
    _l_(652763)

    impair = _c_(652747, _n_(652745, "int", lambda: int), _n_(652746, "m", lambda: m)[0:1])
    _l_(652748)
    pair = _c_(652751, _n_(652749, "int", lambda: int), _n_(652750, "m", lambda: m)[2:3])
    _l_(652752)
    _c_(652756, _a_(652754, _n_(652753, "Impair", lambda: Impair), "append"), _n_(652755, "impair", lambda: impair))
    _l_(652757)
    _c_(652761, _a_(652759, _n_(652758, "Pair", lambda: Pair), "append"), _n_(652760, "pair", lambda: pair))
    _l_(652762)

M = _c_(652770, _a_(652769, _c_(652768, _a_(652765, _n_(652764, "np", lambda: np), "array"), [_n_(652766, "Impair", lambda: Impair), _n_(652767, "Pair", lambda: Pair)]), "transpose"))
_l_(652771)
Table = _c_(652775, _a_(652773, _n_(652772, "pa", lambda: pa), "DataFrame"), _n_(652774, "M", lambda: M), columns = ["Impair", "Pair"])
_l_(652776)

#creating the .csv file
_c_(652781, _a_(652778, _n_(652777, "Table", lambda: Table), "to_csv"), _n_(652779, "dossier", lambda: dossier) + _n_(652780, "fichier", lambda: fichier) + ".csv")
_l_(652782)