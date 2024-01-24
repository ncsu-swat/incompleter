# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56049519/attributeerror-module-pptx-chart-has-no-attribute-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pptx
    _l_(406363)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(406365)

except ImportError:
    pass

df = _c_(406368, _a_(406367, _n_(406366, "pd", lambda: pd), "read_excel"), "data.xlsx")
_l_(406369)

overall_report = _c_(406372, _a_(406371, _n_(406370, "pptx", lambda: pptx), "Presentation"), "pres.pptx")
_l_(406373)


pres_slide = _a_(406375, _n_(406374, "overall_report", lambda: overall_report), "slides")[1]
_l_(406376)

slide_chart = _a_(406379, _a_(406378, _n_(406377, "pres_slide", lambda: pres_slide), "shapes")[20], "chart")
_l_(406380)

#replace chart data with the data from the excel above
chart_data = _c_(406385, _a_(406384, _a_(406383, _a_(406382, _n_(406381, "pptx", lambda: pptx), "chart"), "data"), "CategoryChartData"))  
_l_(406386)  
_n_(406387, "chart_data", lambda: chart_data).categories = _c_(406391, _a_(406390, _a_(406389, _n_(406388, "df", lambda: df)["Question"], "values"), "tolist"))
_l_(406392)

df1 = _c_(406396, _a_(406395, _a_(406394, _n_(406393, "df", lambda: df), "iloc")[:,1:6], "copy"))
_l_(406397)

for col_idx, col in _c_(406401, _n_(406398, "enumerate", lambda: enumerate), _a_(406400, _n_(406399, "df1", lambda: df1), "columns")):
    _l_(406420)

    _c_(406409, _n_(406402, "print", lambda: print), _n_(406403, "col_idx", lambda: col_idx),_n_(406404, "col", lambda: col),_a_(406408, _a_(406406, _n_(406405, "df1", lambda: df1), "iloc")[:, _n_(406407, "col_idx", lambda: col_idx)], "values"))
    _l_(406410)
    _c_(406418, _a_(406412, _n_(406411, "chart_data", lambda: chart_data), "add_series"), _n_(406413, "col", lambda: col),_a_(406417, _a_(406415, _n_(406414, "df1", lambda: df1), "iloc")[:, _n_(406416, "col_idx", lambda: col_idx)], "values"))
    _l_(406419)

#update data
_c_(406424, _a_(406422, _n_(406421, "slide_chart", lambda: slide_chart), "replace_data"), _n_(406423, "chart_data", lambda: chart_data))
_l_(406425)