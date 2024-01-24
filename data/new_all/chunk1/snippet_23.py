# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51770485/typeerror-object-of-type-dataframe-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import dash
    _l_(418987)

except ImportError:
    pass
try:
    import numpy as np
    _l_(418989)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(418991)

except ImportError:
    pass
try:
    import plotly.offline as py
    _l_(418993)

except ImportError:
    pass
try:
    import plotly.graph_objs as go
    _l_(418995)

except ImportError:
    pass
try:
    import psycopg2 as pg2
    _l_(418997)

except ImportError:
    pass
try:
    import datetime
    _l_(418999)

except ImportError:
    pass

conn = _c_(419003, _a_(419001, _n_(419000, "pg2", lambda: pg2), "connect"), database='X',user='X',password=_n_(419002, "secret", lambda: secret))
_l_(419004)

cur = _c_(419007, _a_(419006, _n_(419005, "conn", lambda: conn), "cursor"))
_l_(419008)

_c_(419011, _a_(419010, _n_(419009, "cur", lambda: cur), "execute"), "SELECT * FROM times;")
_l_(419012)
a = _c_(419015, _a_(419014, _n_(419013, "cur", lambda: cur), "fetchall"))
_l_(419016)
_c_(419019, _n_(419017, "str", lambda: str), _n_(419018, "a", lambda: a))
_l_(419020)


df = _c_(419026, _a_(419022, _n_(419021, "pd", lambda: pd), "DataFrame"), [[_n_(419023, "ij", lambda: ij) for ij in _n_(419024, "i", lambda: i)] for i in _n_(419025, "a", lambda: a)])
_l_(419027)
_c_(419030, _a_(419029, _n_(419028, "df", lambda: df), "to_json"))
_l_(419031)
_c_(419034, _a_(419033, _n_(419032, "df", lambda: df), "rename"), columns={0: "Serial Number", 1: "Status", 2: "Date", 3: "Time", 4: "Number"}, inplace=True);
_l_(419035)

x = _n_(419036, "df", lambda: df)["Date"]
_l_(419037)
data = [_c_(419042, _a_(419039, _n_(419038, "go", lambda: go), "Scatter"), x=_n_(419040, "x", lambda: x),
            y=_n_(419041, "df", lambda: df)["Status"])]
_l_(419043)

layout = _c_(419056, _a_(419045, _n_(419044, "go", lambda: go), "Layout"), title="Server Data Visualization",
                   xaxis = _c_(419053, _n_(419046, "dict", lambda: dict), range = [_c_(419049, _a_(419048, _n_(419047, "df", lambda: df), "head"), 1),
                            _c_(419052, _a_(419051, _n_(419050, "df", lambda: df), "tail"), 1)]),
                    yaxis=_c_(419055, _n_(419054, "dict", lambda: dict), title = "Status"))
_l_(419057)

fig = _c_(419062, _a_(419059, _n_(419058, "go", lambda: go), "Figure"), data = _n_(419060, "data", lambda: data), layout = _n_(419061, "layout", lambda: layout))
_l_(419063)
_c_(419067, _a_(419065, _n_(419064, "py", lambda: py), "plot"), _n_(419066, "fig", lambda: fig))
_l_(419068)