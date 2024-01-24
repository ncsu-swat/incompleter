# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63430336/python-bokeh-pandas-attributeerror-unexpected-attribute-responsive-to-fig
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bokeh.plotting import Figure, output_file, show
    _l_(555252)

except ImportError:
    pass
try:
    import pandas
    _l_(555254)

except ImportError:
    pass

file="adbe.csv"
_l_(555255)

df=_c_(555259, _a_(555257, _n_(555256, "pandas", lambda: pandas), "read_csv"), _n_(555258, "file", lambda: file), parse_dates=["Date"])
_l_(555260)

p=_c_(555262, _n_(555261, "figure", lambda: figure), width=500, height=500, x_axis_type="datetime", responsive = True)
_l_(555263)

_c_(555268, _a_(555265, _n_(555264, "p", lambda: p), "line"), _n_(555266, "df", lambda: df)["Date"],_n_(555267, "df", lambda: df)["Close"],color="Orange", alpha=0.5)
_l_(555269)

_c_(555271, _n_(555270, "output_file", lambda: output_file), "Time_Series.html")
_l_(555272)
_c_(555275, _n_(555273, "show", lambda: show), _n_(555274, "p", lambda: p))
_l_(555276)