# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43523115/typeerror-ufunc-isnan-not-supported-for-the-input-types-seaborn-heatmap
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(393397)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(393399)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(393401)

except ImportError:
    pass

df = _c_(393404, _a_(393403, _n_(393402, "pd", lambda: pd), "read_table"), r"C:\Results.CST", sep='\s+',header=11, engine = 'python')
_l_(393405)
df2 = _n_(393406, "cridim", lambda: cridim)[['Bottom','Location_X','Location_Y',]]  # Bottom , location X and Location  Y are my column labels
_l_(393407)  # Bottom , location X and Location  Y are my column labels
df3 = _c_(393410, _a_(393409, _n_(393408, "df2", lambda: df2), "pivot"), 'Location_X','Location_Y','Bottom') # create pivot table for results
_l_(393411) # create pivot table for results

_c_(393414, _a_(393413, _n_(393412, "plt", lambda: plt), "figure"), figsize=(15,15)) 
_l_(393415) 
pivot_table = _n_(393416, "df3", lambda: df3)
_l_(393417)
_c_(393420, _a_(393419, _n_(393418, "plt", lambda: plt), "xlabel"), 'X',size = 10) 
_l_(393421) 
_c_(393424, _a_(393423, _n_(393422, "plt", lambda: plt), "ylabel"), 'Y',size = 10) 
_l_(393425) 
_c_(393428, _a_(393427, _n_(393426, "plt", lambda: plt), "title"), 'btm CD',size = 10) 
_l_(393429) 
_c_(393433, _a_(393431, _n_(393430, "sns", lambda: sns), "heatmap"), _n_(393432, "pivot_table", lambda: pivot_table), annot=False, fmt=".1f", linewidths = 0.5, square = True, cmap = 'RdYlBu', vmin=2900, vmax = 3500) 
_l_(393434) 
_c_(393437, _a_(393436, _n_(393435, "plt", lambda: plt), "show"))
_l_(393438)