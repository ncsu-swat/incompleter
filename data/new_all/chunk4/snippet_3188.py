# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77670448/plotly-creating-charts-using-excel-data-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import plotly.express as px
    _l_(583648)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(583650)

except ImportError:
    pass
kleb = _c_(583653, _a_(583652, _n_(583651, "pd", lambda: pd), "read_excel"), "/content/skrzypce_k_bufory.xlsx")
_l_(583654)
df = _c_(583658, _a_(583657, _a_(583656, _n_(583655, "px", lambda: px), "data"), "kleb"))
_l_(583659)
fig = _c_(583665, _a_(583661, _n_(583660, "px", lambda: px), "violin"), _n_(583662, "df", lambda: df), y="% coverage", color="Amount", violinmode='overlay', hover_data=_a_(583664, _n_(583663, "kleb", lambda: kleb), "columns"))
_l_(583666)
_c_(583669, _a_(583668, _n_(583667, "fig", lambda: fig), "show"))
_l_(583670)