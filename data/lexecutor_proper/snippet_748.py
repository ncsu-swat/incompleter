# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df = _n_(64644, "df", lambda: df)/_c_(64651, _a_(64648, _c_(64647, _a_(64646, _n_(64645, "df", lambda: df), "max")), "astype"), _a_(64650, _n_(64649, "np", lambda: np), "float64"))
_l_(64652)

df = _n_(64653, "df", lambda: df)/_c_(64664, _a_(64661, _a_(64655, _n_(64654, "df", lambda: df), "loc")[_c_(64660, _a_(64659, _c_(64658, _a_(64657, _n_(64656, "df", lambda: df), "abs")), "idxmax"))], "astype"), _a_(64663, _n_(64662, "np", lambda: np), "float64"))
_l_(64665)

