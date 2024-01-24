# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59262525/python-attributeerror-str-object-has-no-attribute-keys
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import chart_studio.plotly as py
    _l_(549458)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(549460)

except ImportError:
    pass

df = _c_(549463, _a_(549462, _n_(549461, "pd", lambda: pd), "read_csv"), 'MS.csv')
_l_(549464)

data = [ _c_(549475, _n_(549465, "dict", lambda: dict), type = 'choropleth',
       locations = _n_(549466, "df", lambda: df)['CODE'],
       z = _n_(549467, "df", lambda: df)['MS'],
       text = _n_(549468, "df", lambda: df)['COUNTRY'],
       colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
           [0.6,"rgb(00, 120, 245)"],[0.7,"rgb(06, 130, 247)"],[1,"rgb(255, 255, 259)"]],
       autocolorscale = False,
       reversescale = True,
       marker = _c_(549472, _n_(549469, "dict", lambda: dict), line = _c_(549471, _n_(549470, "dict", lambda: dict), color = 'rgb(180,180,180)',
               width = 0.5
           ) ),
       colorbar = _c_(549474, _n_(549473, "dict", lambda: dict), autotick = False,
           tickprefix = None,
           title = 'ASes'),
     ) ]
_l_(549476)

layout = _c_(549482, _n_(549477, "dict", lambda: dict), title = 'MS COUNTRY',
   geo = _c_(549481, _n_(549478, "dict", lambda: dict), showframe = False,
       showcoastlines = False,
       projection = _c_(549480, _n_(549479, "dict", lambda: dict), type = 'Mercator'
       )
   )
)
_l_(549483)

fig = _c_(549487, _n_(549484, "dict", lambda: dict), data=_n_(549485, "data", lambda: data), layout=_n_(549486, "layout", lambda: layout) )
_l_(549488)
_c_(549492, _a_(549490, _n_(549489, "py", lambda: py), "plot"), _n_(549491, "fig", lambda: fig), validate=False, filename='d3-world-map' )
_l_(549493)