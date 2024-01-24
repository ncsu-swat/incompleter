# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72392145/matplotlib-typeerror-plotaccessor-pie-takes-1-positional-argument-but-2-were
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(567502)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(567504)

except ImportError:
    pass

required_cols =["Country",
               "Region",
               "Population",
               "Coastline (coast/area ratio)",
               "GDP ($ per capita)",
               "Literacy (%)",
               "Birthrate"]
_l_(567505)

countries = _c_(567509, _a_(567507, _n_(567506, "pd", lambda: pd), "read_csv"), "datasets/countries_of_the_world.csv",
                       usecols = _n_(567508, "required_cols", lambda: required_cols),
                       decimal = ",")
_l_(567510)

_c_(567513, _a_(567512, _n_(567511, "countries", lambda: countries), "rename"), columns = {"GDP ($ per capita)": "PerCapitaGDP",
                           "Coastline (coast/area ratio)" : "CoastLineAreaRatio",
                           "Literacy (%)" : "LiteracyRate"},
                 inplace = True)
_l_(567514)

countries = _c_(567517, _a_(567516, _n_(567515, "countries", lambda: countries), "dropna"))
_l_(567518)

_c_(567521, _a_(567520, _n_(567519, "countries", lambda: countries), "head"))
_l_(567522)

_c_(567526, _a_(567525, _a_(567524, _n_(567523, "countries", lambda: countries), "Region"), "unique"))
_l_(567527)

avg_by_region = _c_(567532, _a_(567531, _c_(567530, _a_(567529, _n_(567528, "countries", lambda: countries), "groupby"), by = "Region"), "mean"))
_l_(567533)

_n_(567534, "avg_by_region", lambda: avg_by_region)
_l_(567535)

_c_(567539, _a_(567538, _a_(567537, _n_(567536, "avg_by_region", lambda: avg_by_region), "Birthrate"), "plot"), kind = "bar")
_l_(567540)

_c_(567543, _a_(567542, _n_(567541, "plt", lambda: plt), "show"))
_l_(567544)

_c_(567548, _a_(567547, _a_(567546, _n_(567545, "avg_by_region", lambda: avg_by_region), "Birthrate"), "plot"), kind = "barh",
                            title = "Avg. Birthrate by Region")
_l_(567549)
_c_(567552, _a_(567551, _n_(567550, "plt", lambda: plt), "show"))
_l_(567553)

pop_by_region = _c_(567558, _a_(567557, _c_(567556, _a_(567555, _n_(567554, "countries", lambda: countries)[["Region", "Population"]], "groupby"), by = "Region"), "sum"))
_l_(567559)



_c_(567563, _a_(567562, _a_(567561, _n_(567560, "pop_by_region", lambda: pop_by_region), "plot"), "pie"), "Population",
                      figsize = (8, 8))
_l_(567564)
_c_(567567, _a_(567566, _n_(567565, "plt", lambda: plt), "show"))
_l_(567568)

_c_(567572, _a_(567571, _a_(567570, _n_(567569, "pop_by_region", lambda: pop_by_region), "plot"), "pie"), "Population",
                      figsize = (8, 8),
                      legends = False,
                      cmap = "Set3")
_l_(567573)

_c_(567576, _a_(567575, _n_(567574, "plt", lambda: plt), "show"))
_l_(567577)