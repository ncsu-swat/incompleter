# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54274101/holoviews-opts-for-plots-throwing-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(470446)

except ImportError:
    pass
try:
    import holoviews as hv
    _l_(470448)

except ImportError:
    pass
try:
    from holoviews import opts
    _l_(470450)

except ImportError:
    pass
_c_(470453, _a_(470452, _n_(470451, "hv", lambda: hv), "extension"), 'bokeh', 'matplotlib')
_l_(470454)
_c_(470457, _a_(470456, _n_(470455, "hv", lambda: hv), "notebook_extension"), 'bokeh','matplotlib')
_l_(470458)

# Declaring data
filepath = 'somefilepath+somefile.csv'
_l_(470459)
df  = _c_(470463, _a_(470461, _n_(470460, "pd", lambda: pd), "read_csv"), _n_(470462, "filepath", lambda: filepath), skipinitialspace = True, encoding = 'utf-8')
_l_(470464)
curves = _c_(470475, _a_(470466, _n_(470465, "hv", lambda: hv), "HoloMap"), {_n_(470467, "col", lambda: col): _c_(470472, _a_(470469, _n_(470468, "hv", lambda: hv), "Curve"), _n_(470470, "df", lambda: df), 'Index', _n_(470471, "col", lambda: col)) for col in _a_(470474, _n_(470473, "df", lambda: df), "columns")},
               kdims='Column')
_l_(470476)

_c_(470485, _a_(470478, _n_(470477, "curves", lambda: curves), "opts"), _c_(470481, _a_(470480, _n_(470479, "opts", lambda: opts), "Area"), color='#fff8dc', line_width=2),
    _c_(470484, _a_(470483, _n_(470482, "opts", lambda: opts), "Curve"), color='black'))
_l_(470486)