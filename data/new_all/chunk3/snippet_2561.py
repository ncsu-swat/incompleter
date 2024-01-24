# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71626403/dash-plotly-error-typeerror-object-of-type-dataframe-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dash_bootstrap_components as dbc
    _l_(556465)

except ImportError:
    pass
try:
    from dash import dcc
    _l_(556467)

except ImportError:
    pass
try:
    import dash_html_components as html
    _l_(556469)

except ImportError:
    pass
try:
    from dash import dash_table
    _l_(556471)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(556473)

except ImportError:
    pass
try:
    import numpy as np
    _l_(556475)

except ImportError:
    pass

def getData():
    _l_(556479)

    aux = _c_(556477, _n_(556476, "preprocess", lambda: preprocess))
    _l_(556478)
    return aux

def back_to_df(dictio):
    _l_(556486)

    aux = _c_(556484, _a_(556482, _a_(556481, _n_(556480, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(556483, "dictio", lambda: dictio))
    _l_(556485)
    return aux

tblcols  =[{"name": _n_(556487, "i", lambda: i), "id": _n_(556488, "i", lambda: i)} for i in _a_(556493, _c_(556492, _n_(556489, "back_to_df", lambda: back_to_df), _c_(556491, _n_(556490, "getData", lambda: getData))), "columns")]
_l_(556494)

app = _c_(556501, _a_(556496, _n_(556495, "dash", lambda: dash), "Dash"), _n_(556497, "__name__", lambda: __name__), external_stylesheets=[_a_(556500, _a_(556499, _n_(556498, "dbc", lambda: dbc), "themes"), "BOOTSTRAP")])
_l_(556502)
body = _c_(556526, _a_(556504, _n_(556503, "html", lambda: html), "Div"), [
    _c_(556507, _a_(556506, _n_(556505, "html", lambda: html), "H1"), "Live rates")
    , _c_(556525, _a_(556509, _n_(556508, "dbc", lambda: dbc), "Row"), [
            _c_(556524, _a_(556511, _n_(556510, "dbc", lambda: dbc), "Col"), _c_(556523, _a_(556513, _n_(556512, "html", lambda: html), "Div"), [_c_(556516, _a_(556515, _n_(556514, "dcc", lambda: dcc), "Interval"), 'graph-update', interval = 80, n_intervals = 0),
      _c_(556522, _a_(556518, _n_(556517, "dash_table", lambda: dash_table), "DataTable"), id = 'table',
          data = _c_(556520, _n_(556519, "getData", lambda: getData)),
          columns=_n_(556521, "tblcols", lambda: tblcols),
          page_size= 10,
          style_table={'overflowX': 'auto'},
      )]),width=3)
            ])
        ])
_l_(556527)
_n_(556528, "app", lambda: app).layout = _c_(556532, _a_(556530, _n_(556529, "html", lambda: html), "Div"), [_n_(556531, "body", lambda: body)])
_l_(556533)

@_c_(556544, _a_(556535, _n_(556534, "app", lambda: app), "callback"), _c_(556539, _a_(556538, _a_(556537, _n_(556536, "dash", lambda: dash), "dependencies"), "Output"), 'table','data'),
        [_c_(556543, _a_(556542, _a_(556541, _n_(556540, "dash", lambda: dash), "dependencies"), "Input"), 'graph-update', 'n_intervals')])
def updateTable(n):
    _l_(556548)

    aux = _c_(556546, _n_(556545, "getData", lambda: getData))
    _l_(556547)
    return aux

if _n_(556549, "__name__", lambda: __name__) == "__main__":
    _l_(556554)

    _c_(556552, _a_(556551, _n_(556550, "app", lambda: app), "run_server"), debug = False, port = 8010)
    _l_(556553)